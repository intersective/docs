import os
import re
import logging
import argparse
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# Allowed models for command-line choices, providing a clear range of options
ALLOWED_MODELS = ['gpt-4.1-nano', 'gpt-4o-mini', 'gpt-4.1-mini', 'o4-mini', 'gpt-4o']

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TechnicalSummaryGenerator")

# Load API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise EnvironmentError("Missing OPENAI_API_KEY in .env")
client = OpenAI(api_key=OPENAI_API_KEY)

def clean_input_text(text: str) -> str:
    """Clean input text by removing unwanted content while preserving JIRA issues structure."""
    lines = text.splitlines()
    useful = []
    for line in lines:
        # Remove media files, curl commands, and URLs but keep JIRA IDs for reference
        if re.search(r"(bandicam|\\.mkv|\\.jpeg|\\.mp4|curl|http[s]?:\\/\\/)", line, re.IGNORECASE):
            continue
        # Remove steps to replicate sections as they're not needed for technical summary
        if "Steps to Replicate" in line or "Expected Result" in line or "Actual Result" in line:
            continue
        useful.append(line.strip())
    return "\n".join(useful).strip()

def chunk_text(text: str, max_chars: int = 4000) -> list:
    """Split text into manageable chunks for processing."""
    paragraphs = text.split("\n\n")
    chunks, current = [], ""
    for para in paragraphs:
        if len(current) + len(para) < max_chars:
            current += para + "\n\n"
        else:
            if current.strip():
                chunks.append(current.strip())
            current = para + "\n\n"
    if current.strip():
        chunks.append(current.strip())
    return chunks

def create_technical_summary_prompt(chunk: str) -> str:
    """Create a single comprehensive prompt for detailed technical summarisation."""
    return f"""You are a senior technical release notes writer. Your job is to convert JIRA issues into comprehensive, detailed technical summaries suitable for production-level release notes.

CRITICAL: All content MUST use British English spelling (organise, customise, colour, centre, optimise, recognise, cancelled, travelled, etc.). Never use American English spellings.

CRITICAL FORMATTING: NEVER use asterisks (**) in markdown headings. If you create headings, use: ## Heading (not ## **Heading**). Only use asterisks for inline bold text within paragraphs, not in headings.

CRITICAL HEADING RULES:
1. NEVER create headings with only images. If you need to show an image, use a descriptive heading followed by the image on the next line (e.g., "## Section Title" then "![Image](path.png)" on next line).
2. NEVER use asterisks (* or **) in heading text. Headings should be: ## Heading (not ## *Heading* or ## **Heading**).
3. NEVER create empty headings. Every heading must have descriptive text.
4. NEVER create standalone lines with just asterisks.

CRITICAL NAVIGATION RULES FOR "WHAT'S NEXT?" SECTIONS:
1. NEVER point back to the same section's collection (e.g., if in Onboarding, don't point to "Onboarding collection").
2. ALWAYS point forward to the next logical step:
   - Next section (e.g., from Onboarding → Essentials)
   - Next article in same section (if logical progression)
   - Related articles in other sections
3. Provide clear progression path with multiple options.
4. Use format: "Now that you understand [topic], you can: [list of next steps]".
5. Include links to: next section, related articles, and same section as optional.

CRITICAL: NEVER mention "Practera 2", "Practera2", or any version numbers. Always refer to the platform simply as "Practera" without version numbers.

REQUIREMENTS:
1. Process EVERY JIRA issue mentioned in the input - do not filter or skip any
2. Create detailed, technical summaries that thoroughly describe what was changed/fixed/added
3. Include as much relevant technical detail as possible while maintaining readability
4. Preserve the JIRA ID for each issue (e.g., CORE-7920) for reference
5. Focus on comprehensive technical documentation, not marketing language
6. Be specific about all components, systems, and processes affected
7. Include detailed context about the problem and solution
8. Identify the issue severity and user impact level

FORMAT for each issue:
- **[JIRA-ID] Component/System: Detailed Technical Title**
  Comprehensive technical description including: what specific functionality was affected, the nature of the issue/enhancement, technical details about the implementation, which user roles are impacted (Admin, Learner, Expert, Student, Coordinator, Educator), which systems/components are involved (App, API, Database, UI, Chat, File Upload, Assessment, etc.), root cause analysis where applicable, technical solution implemented, and any relevant technical context about the change. Include severity indicators (Critical/High/Medium/Low impact).

GUIDELINES:
- Be thorough and detailed - include all relevant technical information
- Specify user roles affected: Admin, Learner, Expert, Student, Coordinator, Educator, Reviewer
- Mention all system components: App, Admin Interface, API, GraphQL, Database, UI, Chat, File Upload, Assessment, Navigation, Authentication, etc.
- Include technical details about what was broken and how it was fixed
- Describe the impact on workflows and user interactions
- Mention any dependencies or related system changes
- For bugs: include root cause where identifiable
- For enhancements: explain the technical implementation approach
- Keep technical accuracy as the top priority
- Each summary should be 3-5 sentences with comprehensive detail
- Use consistent technical terminology throughout
- Identify patterns in related issues for better grouping later

CATEGORIZATION HINTS (for better second-stage processing):
- Mark clear NEW FUNCTIONALITY as [NEW FEATURE]
- Mark IMPROVEMENTS to existing features as [ENHANCEMENT] 
- Mark FIXES as [BUG FIX]
- Mark SECURITY-related items as [SECURITY]
- Mark PERFORMANCE improvements as [PERFORMANCE]
- Mark API/BACKEND changes as [API/BACKEND]

INPUT TO PROCESS:
{chunk}

OUTPUT: List all JIRA issues with their comprehensive technical summaries in the specified format, ensuring no issue is omitted and maximum technical detail is provided with appropriate categorization hints."""

def process_jira_issues(text: str, model: str) -> str:
    """Process all JIRA issues with a single comprehensive prompt."""
    cleaned_text = clean_input_text(text)
    chunks = chunk_text(cleaned_text)
    
    logger.info(f"Processing {len(chunks)} chunk(s) for technical summarization using {model}")
    
    all_summaries = []
    
    for i, chunk in enumerate(chunks, 1):
        logger.info(f"Processing chunk {i}/{len(chunks)}")
        prompt = create_technical_summary_prompt(chunk)
        
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system", 
                        "content": "You are a technical documentation specialist. Convert JIRA issues into precise, technical summaries for release notes."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                temperature=0.1  # Low temperature for consistency and accuracy
            )
            
            summary = response.choices[0].message.content.strip()
            all_summaries.append(summary)
            
        except Exception as e:
            logger.error(f"Failed to process chunk {i}: {e}")
            continue
    
    # Combine all summaries
    combined_summary = "\n\n".join(all_summaries)
    
    # Clean up any duplicate sections or headers
    cleaned_summary = clean_output(combined_summary)
    
    return cleaned_summary

def clean_output(text: str) -> str:
    """Clean the final output to ensure quality and consistency."""
    lines = text.splitlines()
    cleaned_lines = []
    seen_jira_ids = set()
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for duplicate JIRA IDs
        jira_match = re.search(r'CORE-\d+', line)
        if jira_match:
            jira_id = jira_match.group()
            if jira_id in seen_jira_ids:
                logger.warning(f"Duplicate JIRA ID found: {jira_id}")
                continue
            seen_jira_ids.add(jira_id)
        
        cleaned_lines.append(line)
    
    return "\n".join(cleaned_lines)

def save_technical_summary(content: str, version: str) -> str:
    """Save the technical summary to output file."""
    # Create header
    header = f"""# Technical Summary for Release v{version}

📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## JIRA Issues Technical Summary

"""
    
    full_content = header + content
    
    # Save to output file
    output_path = f"docs/releases/v{version}_technical_summary.md"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_content)
    
    logger.info(f"✅ Technical summary saved to {output_path}")
    return output_path

def create_release_notes_prompt(technical_summary: str, version: str) -> str:
    """Create a prompt to organise technical summary into proper release notes sections following the standard template."""
    # Use custom release date from environment or fallback to current date
    release_date = os.getenv('RELEASE_DATE') or datetime.now().strftime('%Y-%m-%d')
    
    return f"""You are a professional release notes editor. Your job is to take the technical summary and organise it into a well-structured, production-ready release note document following the EXACT template format.

CRITICAL: All content MUST use British English spelling (organise, customise, colour, centre, optimise, recognise, cancelled, travelled, etc.). Never use American English spellings.

CRITICAL FORMATTING: NEVER use asterisks (**) in markdown headings. Headings should be: # Heading (not # **Heading**). Only use asterisks for inline bold text within paragraphs, not in headings.

CRITICAL HEADING RULES:
1. NEVER create headings with only images. If you need to show an image, use a descriptive heading followed by the image on the next line (e.g., "## Section Title" then "![Image](path.png)" on next line).
2. NEVER use asterisks (* or **) in heading text. Headings should be: ## Heading (not ## *Heading* or ## **Heading**).
3. NEVER create empty headings. Every heading must have descriptive text.
4. NEVER create standalone lines with just asterisks.

CRITICAL NAVIGATION RULES FOR "WHAT'S NEXT?" SECTIONS:
1. NEVER point back to the same section's collection (e.g., if in Onboarding, don't point to "Onboarding collection").
2. ALWAYS point forward to the next logical step:
   - Next section (e.g., from Onboarding → Essentials)
   - Next article in same section (if logical progression)
   - Related articles in other sections
3. Provide clear progression path with multiple options.
4. Use format: "Now that you understand [topic], you can: [list of next steps]".
5. Include links to: next section, related articles, and same section as optional.

CRITICAL: NEVER mention "Practera 2", "Practera2", or any version numbers. Always refer to the platform simply as "Practera" without version numbers.

STRICT TEMPLATE FORMAT TO FOLLOW:
# Release v{version}
📅 Release Date: {release_date}

## Highlights
- **[Key Improvement 1]**: [One-sentence summary focused on user benefit.]
- **[Key Improvement 2]**: [Another important change in business/user terms.]
- **[Key Improvement 3]**: [Optional, up to 4 highlights maximum.]
- **[Key Improvement 4]**: [Optional.]

## ✨ New Features

- **[Feature Title]**: [Short, clear description focused on what users can do or benefit from.]

## 🔧 Enhancements

- **[Enhancement Title]**: [Short, clear description focused on improved experience or value.]

## 🐞 Bug Fixes

- **[Bug Title]**: [Short, clear description focused on user impact.]

## 🔐 Security

- **[Security Improvement Title]**: [Short, clear description.]

## 📌 Other Improvements

- **[Other Improvement Title]**: [Short, clear description focused on business value or user experience.]

Have questions? Reach out to us at help@practera.com.

ENHANCED PROCESSING REQUIREMENTS:

1. **Follow template structure EXACTLY**:
   - Use the exact section headings with emojis as shown
   - Include release date line with 📅 emoji
   - Keep sections in the specified order
   - Omit sections that have no items (don't show empty sections)

2. **Highlights section (max 4 items)**:
   - Select the 4 most impactful changes from the technical summary
   - Prioritize: New features > Major bug fixes > Performance improvements > User experience enhancements
   - Focus on user/business value, not technical details
   - One sentence each, clear and compelling

3. **Smart Consolidation Strategy**:
   - **Chat/Communication**: Group all chat-related fixes (file upload, messaging, channels, scheduling)
   - **File Upload/Management**: Consolidate all file upload, preview, delete, uploader improvements
   - **Assessment/Review System**: Group assessment submissions, reviews, file handling in assessments
   - **Traffic Light/Pulse Check**: Consolidate all pulse check and traffic light indicator improvements
   - **Admin Interface**: Group admin-specific UI, navigation, and functionality fixes
   - **User Experience**: Group UI improvements, accessibility, visual fixes
   - **API/Backend**: Group GraphQL, API, and backend infrastructure improvements

4. **Include user roles and components with specificity**:
   - Use specific user roles: Admin, Learner, Expert, Student, Coordinator, Educator, Reviewer
   - Mention system components: App, Admin Interface, API, Chat, File Upload, Assessment, Navigation, etc.
   - Example: "**Chat Functionality for Admins and Learners**: Enhanced file uploads, message scheduling, and team channel creation across the Admin Interface and App, ensuring seamless communication for all user roles."

5. **Format requirements**:
   - Use **bold text** for component/feature names in titles
   - Remove ALL JIRA IDs (CORE-XXXX) from output
   - Remove environment references (P2, P2-AUS, P2-USA, P2-EUK, P2-prerelease, P2-stage, etc.)
   - Each bullet: `- **Title**: Description` (no extra emojis, no links)
   - Extra blank lines between sections for readability

6. **Content guidelines with enhanced focus**:
   - Focus on user benefits and improved experience
   - Use clear, professional language that includes technical context when relevant
   - Include user roles and system components for clarity
   - Avoid overly technical jargon but maintain precision
   - Prioritize user-facing changes while explaining technical improvements
   - Group by functional area when consolidating
   - Emphasize reliability, performance, and user experience improvements

7. **Enhanced Section mapping**:
   - **New Features**: Brand new functionality that didn't exist before (look for [NEW FEATURE] hints)
   - **Enhancements**: Improvements to existing features (look for [ENHANCEMENT] hints)
   - **Bug Fixes**: Issues that were resolved (look for [BUG FIX] hints)
   - **Security**: Security-related fixes or improvements (look for [SECURITY] hints)
   - **Other Improvements**: Infrastructure, API changes, performance improvements (look for [API/BACKEND], [PERFORMANCE] hints)

8. **Quality checks**:
   - Ensure every section has meaningful, user-focused content
   - Verify consolidation makes logical sense to end users
   - Check that technical improvements are explained in business value terms
   - Ensure highlights truly represent the most impactful changes

9. **End with support line**:
   - Must end with exactly: "Have questions? Reach out to us at help@practera.com."

INPUT TECHNICAL SUMMARY:
{technical_summary}

OUTPUT: A release note document following the EXACT template format above with enhanced consolidation, clear user benefits, proper section organisation, and user-focused content that maintains technical accuracy while being accessible to end users."""

def organize_into_release_notes(technical_summary: str, version: str, model: str) -> str:
    """Take technical summary and organise it into proper release notes format."""
    logger.info(f"🔄 Organising technical summary into release notes format using {model}")
    
    prompt = create_release_notes_prompt(technical_summary, version)
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system", 
                    "content": "You are a professional release notes editor specializing in creating clear, well-structured documentation for external stakeholders."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            temperature=0.1  # Low temperature for consistency
        )
        
        organized_notes = response.choices[0].message.content.strip()
        logger.info("✅ Technical summary organised into release notes format")
        return organized_notes
        
    except Exception as e:
        logger.error(f"Failed to organise release notes: {e}")
        return technical_summary  # Return original if processing fails

def save_release_notes(content: str, version: str) -> str:
    """Save the organised release notes to output file."""
    # Add generation timestamp as HTML comment (won't be rendered in markdown)
    generation_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    release_date = os.getenv('RELEASE_DATE')
    
    # Add helpful comment about date source
    date_note = ""
    if release_date:
        date_note = f" (using custom date: {release_date})"
    
    header_note = f"""<!-- Generated: {generation_time}{date_note} -->

"""
    
    full_content = header_note + content
    
    # Save to output file
    output_path = f"docs/releases/v{version}.md"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_content)
    
    logger.info(f"✅ Release notes saved to {output_path}")
    return output_path

def main():
    # Help text explaining the model trade-offs for the user
    model_help_text = (
        "Choose the model for the task. The options provide a trade-off between cost, speed, and quality:\n"
        "- gpt-4o:         Highest quality, highest cost. Best for complex first-pass summary.\n"
        "- o4-mini:        High quality, high cost.\n"
        "- gpt-4.1-mini:   Good quality, medium cost.\n"
        "- gpt-4o-mini:    Balanced quality and cost. Good for formatting and general tasks.\n"
        "- gpt-4.1-nano:   Lowest cost, fastest. Best for simple, structured text formatting."
    )

    parser = argparse.ArgumentParser(
        description="Generate technical summaries and release notes from JIRA issues.",
        formatter_class=argparse.RawTextHelpFormatter # Allows for better formatting of help text
    )
    parser.add_argument("--version", required=True, help="Release version (e.g., 2.4.5)")
    parser.add_argument("--release-tag", help="Release tag (for compatibility with pipeline, not used)")
    parser.add_argument("--input-md", help="Input .md file (default: scripts/processing/to_llm_vX.md)")
    parser.add_argument("--technical-only", action="store_true", help="Generate only technical summary, skip release notes formatting")
    parser.add_argument(
        "--processor-model",
        default="gpt-4o-mini",
        choices=ALLOWED_MODELS,
        help="Model for the initial technical summary processing step.\n\n" + model_help_text
    )
    parser.add_argument(
        "--organizer-model",
        default="gpt-4o-mini",
        choices=ALLOWED_MODELS,
        help="Model for the final release note organisation step.\n\n" + model_help_text
    )
    args = parser.parse_args()

    # Determine input file path
    input_md_path = args.input_md or f"scripts/processing/to_llm_v{args.version}.md"
    
    if not os.path.exists(input_md_path):
        logger.error(f"❌ Input file not found: {input_md_path}")
        return

    logger.info(f"📖 Reading input file: {input_md_path}")
    
    with open(input_md_path, "r", encoding="utf-8") as f:
        raw_content = f.read()

    logger.info(f"🔄 Processing JIRA issues for version {args.version}")
    
    # Stage 1: Process all JIRA issues into technical summary
    technical_summary = process_jira_issues(raw_content, args.processor_model)
    
    # Save the technical summary
    technical_output_path = save_technical_summary(technical_summary, args.version)
    
    if args.technical_only:
        logger.info(f"✅ Technical summary generation completed!")
        logger.info(f"📄 Technical summary file: {technical_output_path}")
        return
    
    # Stage 2: Organise technical summary into proper release notes
    release_notes = organize_into_release_notes(technical_summary, args.version, args.organizer_model)
    
    # Save the final release notes
    release_notes_path = save_release_notes(release_notes, args.version)
    
    logger.info(f"✅ Release notes generation completed!")
    logger.info(f"📄 Technical summary: {technical_output_path}")
    logger.info(f"📄 Release notes: {release_notes_path}")

if __name__ == "__main__":
    main()
