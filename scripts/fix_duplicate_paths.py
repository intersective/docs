#!/usr/bin/env python3
"""
Fix Duplicate Path Segments in Markdown Links

This script fixes links that create duplicate path segments by replacing
../directory-name/ with ./ when the file is already inside that directory.
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple

def is_code_block(line: str, in_code_block: bool) -> bool:
    """Check if line is inside a code block."""
    stripped = line.strip()
    if stripped.startswith('```') or stripped.startswith('~~~'):
        return not in_code_block
    return in_code_block

def find_duplicate_path_links(file_path: Path, docs_root: Path) -> List[Dict]:
    """
    Find links in a file that would create duplicate path segments.
    Returns list of fixes needed: (line_num, old_link, new_link, reason)
    """
    fixes = []
    
    # Get the directory name the file is in
    file_dir = file_path.parent
    dir_name = file_dir.name
    
    # Get relative path from docs root
    try:
        rel_path = file_dir.relative_to(docs_root)
        path_parts = list(rel_path.parts)
    except ValueError:
        return fixes
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"  ⚠️  Error reading {file_path}: {e}")
        return fixes
    
    in_code_block = False
    link_pattern = r'(\[([^\]]+)\]\(([^)]+)\))'
    
    for line_num, line in enumerate(lines, 1):
        in_code_block = is_code_block(line, in_code_block)
        if in_code_block:
            continue
        
        matches = re.finditer(link_pattern, line)
        for match in matches:
            full_match = match.group(1)
            link_text = match.group(2)
            link_url = match.group(3)
            
            # Skip external URLs
            if link_url.startswith('http://') or link_url.startswith('https://') or link_url.startswith('mailto:'):
                continue
            
            # Skip anchor-only links
            if link_url.startswith('#'):
                continue
            
            # Check if link contains ../directory-name/ where directory-name matches current directory
            pattern = rf'\.\./{re.escape(dir_name)}/'
            if re.search(pattern, link_url):
                # This creates a duplicate path segment
                # Replace ../directory-name/ with ./
                new_url = re.sub(pattern, './', link_url)
                
                # Also handle cases like ../../directory-name/ when we're already in a subdirectory
                # But only if the directory name matches
                pattern2 = rf'\.\./\.\./{re.escape(dir_name)}/'
                if re.search(pattern2, new_url):
                    # We're in a subdirectory, need to go up one less level
                    new_url = re.sub(pattern2, '../', new_url)
                
                fixes.append({
                    'line': line_num,
                    'old': full_match,
                    'new': f'[{link_text}]({new_url})',
                    'old_url': link_url,
                    'new_url': new_url,
                    'reason': f'Duplicate path segment: ../{dir_name}/ when already in {dir_name}/'
                })
    
    return fixes

def fix_file(file_path: Path, fixes: List[Dict]) -> bool:
    """Apply fixes to a file."""
    if not fixes:
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ⚠️  Error reading {file_path}: {e}")
        return False
    
    # Apply fixes in reverse order to preserve line numbers
    for fix in sorted(fixes, key=lambda x: x['line'], reverse=True):
        # Replace the old link with new link
        # Need to escape special regex characters in old link
        old_pattern = re.escape(fix['old'])
        content = re.sub(old_pattern, fix['new'], content, count=1)
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"  ⚠️  Error writing {file_path}: {e}")
        return False

def main():
    """Main function."""
    project_root = Path(__file__).parent.parent
    docs_dir = project_root / 'docs'
    
    if not docs_dir.exists():
        print(f"Error: docs directory not found at {docs_dir}")
        return 1
    
    print("🔧 Fixing Duplicate Path Segments in Links")
    print("=" * 70)
    print()
    
    total_fixes = 0
    files_fixed = 0
    
    # Process all markdown files
    for root, dirs, files in os.walk(docs_dir):
        # Skip certain directories
        if 'node_modules' in root or '.git' in root or 'site' in root:
            continue
        
        for file in files:
            if not file.endswith('.md'):
                continue
            
            file_path = Path(root) / file
            fixes = find_duplicate_path_links(file_path, docs_dir)
            
            if fixes:
                rel_path = file_path.relative_to(project_root)
                print(f"📄 {rel_path}")
                for fix in fixes:
                    print(f"   Line {fix['line']}: {fix['old_url']} → {fix['new_url']}")
                    print(f"   Reason: {fix['reason']}")
                
                if fix_file(file_path, fixes):
                    files_fixed += 1
                    total_fixes += len(fixes)
                    print(f"   ✅ Fixed {len(fixes)} link(s)")
                else:
                    print(f"   ❌ Failed to apply fixes")
                print()
    
    print("=" * 70)
    print(f"📊 Summary:")
    print(f"  Files fixed: {files_fixed}")
    print(f"  Total links fixed: {total_fixes}")
    
    if total_fixes > 0:
        print()
        print("✅ Duplicate path fixes applied!")
        return 0
    else:
        print()
        print("ℹ️  No duplicate path issues found.")
        return 0

if __name__ == "__main__":
    exit(main())
