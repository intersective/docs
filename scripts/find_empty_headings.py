#!/usr/bin/env python3
"""
Find empty headings and headings with asterisks in markdown files.
"""

import re
from pathlib import Path
from collections import defaultdict

def is_code_block(line: str, in_code_block: bool) -> bool:
    """Check if line is a code block delimiter."""
    if '```' in line:
        return not in_code_block
    return in_code_block

def analyze_file(file_path: Path):
    """Analyze a markdown file for heading issues."""
    try:
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')
    except Exception as e:
        print(f"  ⚠️  Error reading {file_path}: {e}")
        return []
    
    issues = []
    in_code_block = False
    
    for line_num, line in enumerate(lines, 1):
        # Track code blocks
        in_code_block = is_code_block(line, in_code_block)
        if in_code_block:
            continue
        
        stripped = line.strip()
        
        # Check for heading patterns
        heading_match = re.match(r'^(#+)\s+(.+)$', stripped)
        if heading_match:
            level = len(heading_match.group(1))
            content_part = heading_match.group(2).strip()
            
            # Issue 1: Empty heading (just asterisks or whitespace)
            if re.match(r'^\*\*?\s*$', content_part) or content_part == '':
                issues.append({
                    'type': 'empty_heading',
                    'line': line_num,
                    'content': line,
                    'level': level
                })
            
            # Issue 2: Heading with only image
            elif re.match(r'^!\[.*\]\(.*\)\s*$', content_part):
                issues.append({
                    'type': 'image_only_heading',
                    'line': line_num,
                    'content': line,
                    'level': level
                })
            
            # Issue 3: Heading with asterisks around text (single asterisks)
            elif re.match(r'^\*[^*]+\*\s*$', content_part):
                issues.append({
                    'type': 'asterisk_heading',
                    'line': line_num,
                    'content': line,
                    'level': level,
                    'clean': content_part.strip('*').strip()
                })
            
            # Issue 4: Heading with double asterisks around text
            elif re.match(r'^\*\*[^*]+\*\*\s*$', content_part):
                issues.append({
                    'type': 'double_asterisk_heading',
                    'line': line_num,
                    'content': line,
                    'level': level,
                    'clean': content_part.strip('*').strip()
                })
        
        # Issue 5: Standalone asterisk lines (not headings)
        elif stripped in ['**', '*', '***', '****']:
            issues.append({
                'type': 'standalone_asterisks',
                'line': line_num,
                'content': line
            })
    
    return issues

def main():
    docs_dir = Path('docs')
    md_files = list(docs_dir.rglob('*.md'))
    
    print("🔍 Analyzing Markdown Files for Empty Headings and Asterisk Issues")
    print("=" * 70)
    print()
    
    all_issues = defaultdict(list)
    
    for md_file in md_files:
        issues = analyze_file(md_file)
        for issue in issues:
            all_issues[issue['type']].append((md_file, issue))
    
    # Report findings
    print("📊 SUMMARY:")
    print("=" * 70)
    for issue_type, items in sorted(all_issues.items()):
        print(f"  {issue_type}: {len(items)} occurrences")
    print()
    
    # Detailed report
    print("📋 DETAILED FINDINGS:")
    print("=" * 70)
    
    for issue_type in ['empty_heading', 'image_only_heading', 'asterisk_heading', 'double_asterisk_heading', 'standalone_asterisks']:
        if issue_type in all_issues:
            print(f"\n{issue_type.upper().replace('_', ' ')}:")
            print("-" * 70)
            for file, issue in all_issues[issue_type][:20]:  # Show first 20
                if issue_type in ['asterisk_heading', 'double_asterisk_heading']:
                    print(f"  {file}:{issue['line']}")
                    print(f"    Current: {issue['content'].strip()}")
                    print(f"    Should be: {'#' * issue['level']} {issue['clean']}")
                else:
                    print(f"  {file}:{issue['line']} - {issue['content'].strip()[:60]}")
            if len(all_issues[issue_type]) > 20:
                print(f"  ... and {len(all_issues[issue_type]) - 20} more")
    
    print()
    print("=" * 70)
    print(f"Total issues found: {sum(len(items) for items in all_issues.values())}")
    
    return all_issues

if __name__ == '__main__':
    main()
