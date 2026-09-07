#!/usr/bin/env python3
"""
Fix Remaining Image Paths - Remove -practera-2 from Image References

Some markdown files still reference -practera-2 in image paths, but we've
renamed the directories. This script updates those references.
"""

import os
import re
from pathlib import Path
from typing import List, Dict

def is_code_block(line: str, in_code_block: bool) -> bool:
    """Check if line is inside a code block."""
    stripped = line.strip()
    if stripped.startswith('```') or stripped.startswith('~~~'):
        return not in_code_block
    return in_code_block

def find_practera2_image_references(file_path: Path) -> List[Dict]:
    """Find image references that still contain -practera-2."""
    fixes = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"  ⚠️  Error reading {file_path}: {e}")
        return fixes
    
    in_code_block = False
    # Pattern for markdown images: ![alt](path) or <img src="path">
    image_pattern = r'(!\[[^\]]*\]\(([^)]+)\)|<img[^>]+src=["\']([^"\']+)["\'][^>]*>)'
    
    for line_num, line in enumerate(lines, 1):
        in_code_block = is_code_block(line, in_code_block)
        if in_code_block:
            continue
        
        # Check for -practera-2 in image paths
        if '-practera-2' in line and ('assets/images' in line or 'Image' in line):
            # Find all image references in this line
            matches = re.finditer(image_pattern, line)
            for match in matches:
                full_match = match.group(0)
                # Get the path (could be in group 2 or 3)
                path = match.group(2) if match.group(2) else match.group(3)
                
                if path and '-practera-2' in path:
                    # Replace -practera-2 with nothing
                    new_path = path.replace('-practera-2', '')
                    new_line = line.replace(path, new_path)
                    
                    fixes.append({
                        'line': line_num,
                        'old': line,
                        'new': new_line,
                        'old_path': path,
                        'new_path': new_path
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
    
    # Apply fixes
    for fix in sorted(fixes, key=lambda x: x['line'], reverse=True):
        # Replace the old line with new line
        content = content.replace(fix['old'], fix['new'], 1)
    
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
    
    print("🔧 Fixing Remaining Image Paths with -practera-2")
    print("=" * 70)
    print()
    
    # Find all markdown files with -practera-2 in image paths
    files_to_fix = []
    for root, dirs, files in os.walk(docs_dir):
        if 'node_modules' in root or '.git' in root or 'site' in root:
            continue
        
        for file in files:
            if not file.endswith('.md'):
                continue
            
            file_path = Path(root) / file
            fixes = find_practera2_image_references(file_path)
            
            if fixes:
                files_to_fix.append((file_path, fixes))
    
    if not files_to_fix:
        print("ℹ️  No files found with -practera-2 in image paths.")
        return 0
    
    total_fixes = 0
    files_updated = 0
    
    for file_path, fixes in files_to_fix:
        rel_path = file_path.relative_to(project_root)
        print(f"📄 {rel_path}")
        for fix in fixes:
            print(f"   Line {fix['line']}: {fix['old_path']} → {fix['new_path']}")
        
        if fix_file(file_path, fixes):
            files_updated += 1
            total_fixes += len(fixes)
            print(f"   ✅ Fixed {len(fixes)} image reference(s)")
        else:
            print(f"   ❌ Failed to apply fixes")
        print()
    
    print("=" * 70)
    print(f"📊 Summary:")
    print(f"  Files updated: {files_updated}")
    print(f"  Total image references fixed: {total_fixes}")
    
    if total_fixes > 0:
        print()
        print("✅ Image path fixes applied!")
        return 0
    else:
        print()
        print("ℹ️  No fixes needed.")
        return 0

if __name__ == "__main__":
    exit(main())
