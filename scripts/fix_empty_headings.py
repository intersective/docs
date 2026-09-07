#!/usr/bin/env python3
"""
Fix empty headings and headings with asterisks in markdown files.
- Removes heading markers from image-only headings
- Removes asterisks from headings
- Removes empty headings
- Removes standalone asterisk lines
"""

import re
from pathlib import Path
from collections import defaultdict

def is_code_block(line: str, in_code_block: bool) -> bool:
    """Check if line is a code block delimiter."""
    if '```' in line:
        return not in_code_block
    return in_code_block

def fix_file(file_path: Path) -> dict:
    """Fix heading issues in a markdown file."""
    try:
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')
    except Exception as e:
        print(f"  ⚠️  Error reading {file_path}: {e}")
        return {'fixed': 0, 'changes': []}
    
    fixed_lines = []
    changes = []
    in_code_block = False
    fixed_count = 0
    
    for line_num, line in enumerate(lines, 1):
        original_line = line
        
        # Track code blocks
        in_code_block = is_code_block(line, in_code_block)
        if in_code_block:
            fixed_lines.append(line)
            continue
        
        stripped = line.strip()
        
        # Fix 1: Image-only headings - remove heading marker
        # Pattern: ### ![Image](...) or ## ![Image](...)
        image_heading_match = re.match(r'^(#+)\s+(!\[.*\]\(.*\))\s*$', stripped)
        if image_heading_match:
            # Remove heading marker, keep image
            fixed_line = image_heading_match.group(2)
            fixed_lines.append(fixed_line)
            changes.append({
                'line': line_num,
                'type': 'image_only_heading',
                'before': line,
                'after': fixed_line
            })
            fixed_count += 1
            continue
        
        # Fix 2: Headings with single asterisks - remove asterisks
        # Pattern: ## *Heading* or ### *Heading*
        single_asterisk_match = re.match(r'^(#+)\s+\*([^*]+)\*\s*$', stripped)
        if single_asterisk_match:
            level = single_asterisk_match.group(1)
            text = single_asterisk_match.group(2).strip()
            fixed_line = f"{level} {text}"
            fixed_lines.append(fixed_line)
            changes.append({
                'line': line_num,
                'type': 'asterisk_heading',
                'before': line,
                'after': fixed_line
            })
            fixed_count += 1
            continue
        
        # Fix 3: Headings with double asterisks - remove asterisks
        # Pattern: ## **Heading** or ### **Heading**
        double_asterisk_match = re.match(r'^(#+)\s+\*\*([^*]+)\*\*\s*$', stripped)
        if double_asterisk_match:
            level = double_asterisk_match.group(1)
            text = double_asterisk_match.group(2).strip()
            fixed_line = f"{level} {text}"
            fixed_lines.append(fixed_line)
            changes.append({
                'line': line_num,
                'type': 'double_asterisk_heading',
                'before': line,
                'after': fixed_line
            })
            fixed_count += 1
            continue
        
        # Fix 4: Empty headings (just asterisks or whitespace) - remove entirely
        # Pattern: ## ** or ### * or ## (empty)
        empty_heading_match = re.match(r'^#+\s*\*\*?\s*$', stripped)
        if empty_heading_match:
            # Remove the line entirely
            changes.append({
                'line': line_num,
                'type': 'empty_heading',
                'before': line,
                'after': '(removed)'
            })
            fixed_count += 1
            continue
        
        # Fix 5: Standalone asterisk lines (not in headings) - remove
        # Pattern: ** or * or *** (standalone)
        if stripped in ['**', '*', '***', '****']:
            # Check if it's not part of a list or other structure
            # If previous line is empty or next line is empty, it's likely standalone
            prev_empty = line_num > 1 and not lines[line_num - 2].strip()
            next_empty = line_num < len(lines) and not lines[line_num].strip() if line_num < len(lines) else True
            
            if prev_empty or next_empty:
                changes.append({
                    'line': line_num,
                    'type': 'standalone_asterisks',
                    'before': line,
                    'after': '(removed)'
                })
                fixed_count += 1
                continue
        
        # No fix needed, keep original line
        fixed_lines.append(line)
    
    # Write back if changes were made
    if fixed_count > 0:
        try:
            file_path.write_text('\n'.join(fixed_lines), encoding='utf-8')
        except Exception as e:
            print(f"  ⚠️  Error writing {file_path}: {e}")
            return {'fixed': 0, 'changes': []}
    
    return {'fixed': fixed_count, 'changes': changes}

def main():
    docs_dir = Path('docs')
    md_files = list(docs_dir.rglob('*.md'))
    
    print("🔧 Fixing Empty Headings and Asterisk Issues")
    print("=" * 70)
    print()
    
    total_fixed = 0
    files_modified = []
    
    for md_file in md_files:
        result = fix_file(md_file)
        if result['fixed'] > 0:
            total_fixed += result['fixed']
            files_modified.append((md_file, result))
            print(f"📄 {md_file}")
            print(f"   Fixed: {result['fixed']} issue(s)")
            for change in result['changes']:
                print(f"   Line {change['line']} ({change['type']}):")
                print(f"     Before: {change['before'].strip()[:60]}")
                if change['after'] != '(removed)':
                    print(f"     After:  {change['after'].strip()[:60]}")
                else:
                    print(f"     After:  (removed)")
            print()
    
    print("=" * 70)
    print("📊 Summary:")
    print(f"   Files modified: {len(files_modified)}")
    print(f"   Total fixes: {total_fixed}")
    print()
    
    if total_fixed > 0:
        print("✅ All fixes applied successfully!")
    else:
        print("ℹ️  No issues found to fix.")

if __name__ == '__main__':
    main()
