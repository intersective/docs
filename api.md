# Release Notes System Documentation

## Overview
This document provides detailed information about the Automated Release Notes System, including script interfaces, configuration, and usage patterns.

## 🔧 System Architecture

The system consists of several Python scripts that work together to automate the release notes generation process:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Jira Issues   │───▶│  AI Summarizer  │───▶│  Release Notes  │
│                 │    │   (OpenAI)      │    │   (Markdown)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  fetch_jira.py  │    │summarize_llm.py │    │  update_nav.py  │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🔐 Authentication & Configuration

### Environment Variables

All scripts require the following environment variables:

```bash
# Jira Configuration
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_USER_EMAIL=your-email@company.com
JIRA_API_TOKEN=your-jira-api-token

# OpenAI Configuration
OPENAI_API_KEY=your-openai-api-key
```

### Security Best Practices

- **Never commit credentials**: All sensitive data is stored in `.env` files (gitignored)
- **Use environment variables**: Scripts load credentials via `os.getenv()`
- **GitHub Secrets**: For CI/CD, use GitHub repository secrets
- **Token rotation**: Regularly rotate API tokens for security

## 📜 Script Interfaces

### 1. Jira Issue Fetcher (`scripts/fetch_jira.py`)

Fetches issues from Jira based on release tags and prepares them for processing.

#### Usage
```bash
# Fetch issues for a specific release
python scripts/fetch_jira.py "Release 2.4.5"

# List available releases
python scripts/fetch_jira.py --list
```

#### Output
- Creates `docs/releases/v{VERSION}_raw.yaml` with structured issue data
- Generates initial markdown content in `scripts/processing/to_llm_v{VERSION}.md`

#### JQL Query Format
```sql
fixVersion = "Release 2.4.5" ORDER BY type DESC, priority DESC
```

### 2. AI Summarizer (`scripts/summarize_llm.py`)

Uses OpenAI GPT-4 to generate professional, business-focused release notes.

#### Usage
```bash
# Generate complete release notes (both stages)
python scripts/summarize_llm.py --version 2.4.5 --release-tag "Release 2.4.5"

# Generate only technical summary (first stage)
python scripts/summarize_llm.py --version 2.4.5 --technical-only
```

#### Output Files
- `docs/releases/v{VERSION}_technical_summary.md`: Detailed technical analysis (Stage 1)
- `docs/releases/v{VERSION}.md`: Final formatted release notes (Stage 2)

#### Features
- **Two-Stage Processing**: First creates detailed technical summaries, then organizes into release notes
- **Intelligent Categorization**: Groups issues by type (Features, Bug Fixes, etc.)
- **Business-Focused Language**: Converts technical details to user benefits
- **Template Compliance**: Ensures consistent formatting following templates/release-note-template.md
- **Multi-Chunk Processing**: Handles large issue sets efficiently
- **Comprehensive Coverage**: Processes every JIRA issue without filtering

#### Two-Stage Prompt Engineering
The system uses a sophisticated two-prompt approach:

**Stage 1 - Technical Summary Prompt:**
- Comprehensive technical analysis of every JIRA issue
- Detailed documentation suitable for technical teams
- Preservation of technical context and implementation details
- Categorization hints for better organization

**Stage 2 - Release Notes Organization Prompt:**
- Transforms technical summaries into user-focused language
- Groups related issues intelligently
- Follows exact template structure from templates/release-note-template.md
- Removes technical jargon while maintaining accuracy
- Focuses on user benefits and business value

### 3. Navigation Updater (`scripts/update_nav.py`)

Automatically updates MkDocs navigation to include new releases.

#### Usage
```bash
python scripts/update_nav.py --version 2.4.5
```

#### Features
- **Automatic Sorting**: Releases sorted by version number (newest first)
- **Pattern Matching**: Supports various release naming conventions
- **Safe Updates**: Only modifies navigation when changes are detected

### 4. Release Pipeline (`release_pipeline.sh`)

Main orchestration script that coordinates the entire process.

#### Usage
```bash
# Manual execution
./release_pipeline.sh "Release 2.4.5"

# GitHub Actions (uses RELEASE_STRING env var)
./release_pipeline.sh
```

#### Pipeline Steps
1. **Prerequisites Check**: Validates environment and dependencies
2. **Jira Fetch**: Retrieves issues for the specified release
3. **Two-Stage AI Summarization**: 
   - Stage 1: Creates detailed technical summaries
   - Stage 2: Organizes into user-focused release notes
4. **Navigation Update**: Updates MkDocs navigation
5. **Cleanup**: Removes temporary files (raw YAML, technical summaries, processing files)

## 📊 Data Flow

### 1. Jira Data Extraction
```yaml
# Example raw.yaml structure
issues:
  - key: "PROJ-123"
    summary: "Add user authentication feature"
    description: "Implement OAuth2 authentication for users"
    type: "Story"
    priority: "High"
    status: "Done"
    category: "feature"
```

### 2. AI Processing
```markdown
# Generated release notes structure
# Release v2.4.5
📅 Release Date: 2024-01-15

## Highlights
- **Enhanced Security**: New authentication system for improved user protection
- **Better User Experience**: Streamlined login process

## ✨ New Features
- **User Authentication**: Secure OAuth2-based login system for enhanced security
```

### 3. Navigation Update
```yaml
# Updated mkdocs.yml navigation
nav:
  - Releases:
    - releases/index.md
    - v2.4.5: releases/v2.4.5.md
    - v2.4.4: releases/v2.4.4.md
```

## 🔄 GitHub Actions Integration

### Workflow Configuration

The system includes a GitHub Actions workflow (`.github/workflows/release-notes.yml`) that:

- **Manual Trigger**: Uses `workflow_dispatch` for controlled execution
- **Input Validation**: Requires release string as input
- **Environment Setup**: Configures Python and dependencies
- **Secure Execution**: Uses GitHub secrets for credentials
- **Error Handling**: Comprehensive error reporting and logging

### Workflow Usage
1. Navigate to Actions → Release Notes Automation
2. Click "Run workflow"
3. Enter release string (e.g., "Release 2.4.5")
4. Monitor execution in real-time

## 🎯 Quality Assurance

### Template Compliance
All generated release notes follow the structure defined in `templates/release-note-template.md`:

- Consistent section ordering
- Standardized bullet point formatting
- Business-focused language
- Professional tone and style

### Content Guidelines
- **User-Centric**: Focus on user benefits and business value
- **Non-Technical**: Avoid technical jargon and implementation details
- **Concise**: Clear, actionable descriptions
- **Professional**: Suitable for external stakeholders

## 🚀 Performance & Scalability

### Optimization Features
- **Chunked Processing**: Large issue sets are processed in manageable chunks
- **Caching**: Intermediate results are cached to avoid reprocessing
- **Parallel Processing**: Multiple operations can run concurrently
- **Memory Management**: Efficient handling of large datasets

### Rate Limiting
- **Jira API**: 100 requests per minute
- **OpenAI API**: 3 requests per minute (GPT-4)
- **GitHub API**: 5000 requests per hour

## 🐛 Error Handling

### Common Error Scenarios
1. **Authentication Failures**: Invalid credentials or expired tokens
2. **API Rate Limits**: Exceeded request limits
3. **Network Issues**: Connectivity problems
4. **Data Validation**: Invalid or missing data

### Error Recovery
- **Retry Logic**: Automatic retry for transient failures
- **Graceful Degradation**: Partial results when possible
- **Detailed Logging**: Comprehensive error reporting
- **User Feedback**: Clear error messages and suggestions

## 📈 Monitoring & Logging

### Logging Levels
- **INFO**: Normal operation events
- **WARNING**: Potential issues that don't stop execution
- **ERROR**: Issues that prevent successful completion
- **DEBUG**: Detailed information for troubleshooting

### Log Format
```
2024-01-15 10:30:45 - fetch_jira - INFO - Fetched 25 issues for Release 2.4.5
2024-01-15 10:31:12 - summarize_llm - INFO - Processing chunk 1/3
```

## 🔧 Customization

### Template Modification
To customize the release notes format, edit `templates/release-note-template.md`:

```markdown
# Custom template structure
# Release vX.Y.Z
📅 Release Date: YYYY-MM-DD

## Custom Section
- **[Item Title]**: [Description]
```

### Prompt Customization
Modify prompts in `scripts/summarize_llm.py` to adjust:
- Language style and tone
- Content categorization
- Formatting preferences
- Business focus areas

## 📚 Examples

### Complete Workflow Example
```bash
# 1. Set environment variables
export JIRA_API_TOKEN="your-token"
export OPENAI_API_KEY="your-key"

# 2. Run the pipeline
./release_pipeline.sh "Release 2.4.5"

# 3. Check results
ls docs/releases/v2.4.5.md
cat docs/releases/v2.4.5.md
```

### Batch Processing Example
```bash
# Create release list
echo "Release 2.4.5" > release.log
echo "Release 2.4.4" >> release.log

# Process all releases
./one-time.sh
```

## 🆘 Support & Troubleshooting

### Getting Help
- **Documentation**: Check this file and README.md
- **Issues**: Report problems via GitHub Issues
- **Email**: Contact help@practera.com for urgent support

### Debug Mode
```bash
# Enable verbose logging
export DEBUG=1
./release_pipeline.sh "Release 2.4.5"
```

### Common Solutions
1. **Authentication Issues**: Verify credentials and permissions
2. **API Limits**: Check rate limits and billing status
3. **File Permissions**: Ensure write access to output directories
4. **Network Problems**: Verify internet connectivity and firewall settings 