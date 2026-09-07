#!/usr/bin/env python3
"""
Remove Asterisks from Markdown Headings

Safely removes redundant asterisks from markdown headings while preserving:
- Inline bold text in paragraphs
- Code blocks
- Links and other formatting
"""

import re
import os
from pathlib import Path

# Files/directories to skip
SKIP_PATTERNS = [
    'venv/',
    'site/',
    '.git/',
    '__pycache__/',
    '.pyc',
    'node_modules/',
]

# File extensions to process
PROCESS_EXTENSIONS = ['.md']

def should_skip_file(file_path: Path) -> bool:
    """Check if file should be skipped."""
    path_str = str(file_path)
    for pattern in SKIP_PATTERNS:
        if pattern in path_str:
            return True
    return False

def is_code_block(line: str, in_code_block: bool) -> bool:
    """Check if line is inside a code block."""
    stripped = line.strip()
    if stripped.startswith('```') or stripped.startswith('~~~'):
        return not in_code_block  # Toggle state
    return in_code_block

def remove_asterisks_from_heading(line: str) -> tuple[str, bool]:
    """
    Remove asterisks from markdown headings.
    Returns (converted_line, was_changed)
    """
    # Pattern 1: Markdown headings with asterisks: # **Heading** or ## **Heading**
    # Matches: # **Title**, ## **Title**, ### **Title**, etc.
    # Also handles: ## ****Title**** (double asterisks)
    pattern1 = r'^(\s*#+\s+)\*\*+([^*]+?)\*+\*+(\s*)$'
    match1 = re.match(pattern1, line)
    if match1:
        prefix = match1.group(1)
        title = match1.group(2).strip()
        suffix = match1.group(3)
        return f"{prefix}{title}{suffix}\n", True
    
    # Pattern 2: Standalone bold line: **Heading**
    # Convert to ### heading (level 3)
    pattern2 = r'^(\s*)\*\*+([^*]+?)\*+\*+(\s*)$'
    match2 = re.match(pattern2, line)
    if match2:
        indent = match2.group(1)
        title = match2.group(2).strip()
        suffix = match2.group(3)
        # Only convert if it's on its own line and looks like a heading
        if len(indent) < 4:  # Not heavily indented (likely a heading)
            return f"{indent}### {title}{suffix}\n", True
    
    return line, False

def convert_file(file_path: Path) -> tuple[int, list[str]]:
    """
    Convert a single file.
    Returns (total_changes, list_of_changed_lines_info)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"  ⚠️  Error reading {file_path}: {e}")
        return 0, []
    
    converted_lines = []
    total_changes = 0
    changed_lines_info = []
    in_code_block = False
    
    for line_num, line in enumerate(lines, 1):
        original_line = line
        
        # Check if entering/exiting code block
        in_code_block = is_code_block(line, in_code_block)
        
        # Skip code blocks
        if in_code_block:
            converted_lines.append(line)
            continue
        
        # Skip if line contains inline bold (not a heading)
        # Check if it's a heading pattern first
        if not re.match(r'^\s*#+\s+', line) and not re.match(r'^\s*\*\*+[^*]+\*+\*+\s*$', line):
            # Not a heading pattern, keep as-is
            converted_lines.append(line)
            continue
        
        # Convert heading
        converted_line, was_changed = remove_asterisks_from_heading(line)
        converted_lines.append(converted_line)
        
        if was_changed:
            total_changes += 1
            changed_lines_info.append(f"  Line {line_num}: {original_line.strip()[:60]}...")
    
    # Write back if changes were made
    if total_changes > 0:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(converted_lines)
        except Exception as e:
            print(f"  ⚠️  Error writing {file_path}: {e}")
            return 0, []
    
    return total_changes, changed_lines_info

def convert_directory(directory: Path) -> dict:
    """Convert all files in directory recursively."""
    stats = {
        'files_processed': 0,
        'files_changed': 0,
        'total_changes': 0,
        'file_details': {}
    }
    
    for root, dirs, files in os.walk(directory):
        root_path = Path(root)
        if should_skip_file(root_path):
            continue
        
        for file in files:
            file_path = root_path / file
            
            if should_skip_file(file_path):
                continue
            
            if file_path.suffix not in PROCESS_EXTENSIONS:
                continue
            
            stats['files_processed'] += 1
            changes, line_info = convert_file(file_path)
            
            if changes > 0:
                stats['files_changed'] += 1
                stats['total_changes'] += changes
                stats['file_details'][str(file_path)] = {
                    'changes': changes,
                    'lines': line_info
                }
                print(f"  ✅ {file_path.relative_to(directory)}: {changes} changes")
    
    return stats

def main():
    """Main conversion function."""
    project_root = Path(__file__).parent.parent
    docs_dir = project_root / 'docs'
    
    print("🧹 Removing Asterisks from Headings")
    print("=" * 60)
    print()
    
    # Convert docs directory
    print("📚 Converting documentation files...")
    stats = convert_directory(docs_dir)
    print()
    
    # Summary
    print("=" * 60)
    print("📊 Conversion Summary:")
    print(f"  Files processed: {stats['files_processed']}")
    print(f"  Files changed: {stats['files_changed']}")
    print(f"  Total conversions: {stats['total_changes']}")
    print()
    
    if stats['files_changed'] > 0:
        print("✅ Conversion completed successfully!")
    else:
        print("ℹ️  No changes needed - headings already clean!")

if __name__ == "__main__":
    main()
