#!/usr/bin/env python3
"""
Analyze all "What's Next?" sections in markdown files to identify navigation issues.
"""

import re
from pathlib import Path
from collections import defaultdict

def get_navigation_structure():
    """Get the navigation structure from mkdocs.yml."""
    import yaml
    
    with open('mkdocs.yml', 'r') as f:
        config = yaml.safe_load(f)
    
    nav = config.get('nav', [])
    
    # Build a map of file paths to their position in navigation
    nav_map = {}
    section_map = {}
    
    def process_nav(items, path='', section=''):
        for item in items:
            if isinstance(item, dict):
                for key, value in item.items():
                    if isinstance(value, str):
                        file_path = Path('docs') / value
                        nav_map[str(file_path)] = {
                            'path': path + ' > ' + key if path else key,
                            'section': section or key,
                            'full_path': path + ' > ' + key if path else key
                        }
                    elif isinstance(value, list):
                        new_section = section or key
                        process_nav(value, path + ' > ' + key if path else key, new_section)
    
    process_nav(nav)
    return nav_map

def find_whats_next_sections():
    """Find all "What's Next?" sections in markdown files."""
    docs_dir = Path('docs')
    md_files = list(docs_dir.rglob('*.md'))
    
    whats_next_sections = []
    
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            lines = content.split('\n')
            
            for i, line in enumerate(lines):
                # Check for "What's Next?" heading (case insensitive)
                if re.match(r'^#+\s+What[\'']?s\s+Next\??\s*$', line, flags=re.IGNORECASE):
                    # Get the next few lines for context
                    context_lines = []
                    for j in range(i+1, min(i+10, len(lines))):
                        context_lines.append(lines[j])
                        if j < len(lines) - 1 and lines[j+1].strip() and lines[j+1].startswith('#'):
                            break
                    
                    whats_next_sections.append({
                        'file': md_file,
                        'line': i + 1,
                        'heading': line,
                        'content': '\n'.join(context_lines[:5]).strip()
                    })
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
    
    return whats_next_sections

def analyze_whats_next_content(whats_next_sections, nav_map):
    """Analyze the content of "What's Next?" sections for issues."""
    issues = []
    
    for section in whats_next_sections:
        file_path = section['file']
        content = section['content']
        
        # Get current file's navigation info
        current_nav = nav_map.get(str(file_path), {})
        current_section = current_nav.get('section', 'Unknown')
        current_path = current_nav.get('full_path', 'Unknown')
        
        # Check for links in the content
        links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
        
        # Analyze each link
        link_issues = []
        for link_text, link_path in links:
            # Resolve relative paths
            if link_path.startswith('../'):
                # Count ../ to determine how many levels up
                levels_up = len(re.findall(r'\.\./', link_path))
                resolved_path = file_path.parent
                for _ in range(levels_up):
                    resolved_path = resolved_path.parent
                resolved_path = resolved_path / link_path.replace('../', '')
            elif link_path.startswith('./'):
                resolved_path = file_path.parent / link_path.replace('./', '')
            elif not link_path.startswith('http'):
                resolved_path = file_path.parent / link_path
            
            # Check if link points to index.md (collection overview)
            if 'index.md' in str(resolved_path):
                target_section = resolved_path.parent.name
                # Check if pointing to same section (circular reference)
                if target_section == current_section or target_section in current_path:
                    link_issues.append({
                        'type': 'circular_reference',
                        'link_text': link_text,
                        'link_path': link_path,
                        'issue': f'Points to {target_section} collection, but article is already in {current_section}'
                    })
                elif target_section in ['onboarding', 'essentials'] and current_section == 'onboarding':
                    # Check if pointing backward in navigation
                    if target_section == 'onboarding' and 'essentials' in current_path.lower():
                        link_issues.append({
                            'type': 'backward_reference',
                            'link_text': link_text,
                            'link_path': link_path,
                            'issue': f'Points backward to {target_section} from {current_section}'
                        })
        
        # Check for generic "Onboarding collection" references when already in Onboarding
        if current_section.lower() == 'onboarding':
            if re.search(r'onboarding\s+collection', content, re.IGNORECASE):
                link_issues.append({
                    'type': 'circular_reference',
                    'link_text': 'Onboarding collection',
                    'link_path': 'text reference',
                    'issue': 'References Onboarding collection but article is already in Onboarding'
                })
        
        if link_issues:
            issues.append({
                'file': file_path,
                'line': section['line'],
                'section': current_section,
                'path': current_path,
                'content': section['content'][:200],
                'issues': link_issues
            })
    
    return issues

def main():
    print("🔍 Analyzing All 'What's Next?' Sections")
    print("=" * 70)
    print()
    
    # Get navigation structure
    print("📋 Loading navigation structure...")
    nav_map = get_navigation_structure()
    
    # Find all "What's Next?" sections
    print("🔍 Finding all 'What's Next?' sections...")
    whats_next_sections = find_whats_next_sections()
    
    print(f"✅ Found {len(whats_next_sections)} 'What's Next?' sections")
    print()
    
    # Analyze for issues
    print("🔍 Analyzing for navigation issues...")
    issues = analyze_whats_next_content(whats_next_sections, nav_map)
    
    # Report findings
    print("=" * 70)
    print("📊 ANALYSIS RESULTS")
    print("=" * 70)
    print()
    
    if issues:
        print(f"❌ Found {len(issues)} 'What's Next?' sections with issues:")
        print()
        
        for issue in issues:
            print(f"📄 {issue['file']}")
            print(f"   Line: {issue['line']}")
            print(f"   Section: {issue['section']}")
            print(f"   Path: {issue['path']}")
            print(f"   Content preview: {issue['content'][:100]}...")
            print(f"   Issues:")
            for link_issue in issue['issues']:
                print(f"     - {link_issue['type']}: {link_issue['issue']}")
                print(f"       Link: [{link_issue['link_text']}]({link_issue['link_path']})")
            print()
    else:
        print("✅ No navigation issues found in 'What's Next?' sections!")
    
    # Show all "What's Next?" sections for reference
    print("=" * 70)
    print("📋 ALL 'WHAT'S NEXT?' SECTIONS:")
    print("=" * 70)
    print()
    
    for section in whats_next_sections:
        nav_info = nav_map.get(str(section['file']), {})
        section_name = nav_info.get('section', 'Unknown')
        print(f"📄 {section['file']}")
        print(f"   Section: {section_name}")
        print(f"   Line: {section['line']}")
        print(f"   Content: {section['content'][:150]}...")
        print()

if __name__ == '__main__':
    main()
