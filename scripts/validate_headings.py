#!/usr/bin/env python3
"""
Validate Markdown Headings

Checks for asterisks in markdown headings and reports violations.
Can be used in CI/CD pipelines or manually.
"""

import re
import os
import sys
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

# File extensions to check
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
        return not in_code_block
    return in_code_block

def check_file(file_path: Path) -> list:
    """
    Check a single file for asterisks in headings.
    Returns list of violations: [(line_num, line_content), ...]
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"  ⚠️  Error reading {file_path}: {e}", file=sys.stderr)
        return []
    
    violations = []
    in_code_block = False
    
    for line_num, line in enumerate(lines, 1):
        # Check if entering/exiting code block
        in_code_block = is_code_block(line, in_code_block)
        
        # Skip code blocks
        if in_code_block:
            continue
        
        # Check for asterisks in markdown headings
        # Pattern: # **Heading** or ## **Heading** etc.
        if re.match(r'^\s*#+\s+\*\*', line):
            violations.append((line_num, line.strip()))
        
        # Check for image-only headings
        # Pattern: ### ![Image](...) or ## ![Image](...)
        if re.match(r'^\s*#+\s+!\[.*\]\(.*\)\s*$', line.strip()):
            violations.append((line_num, f"Image-only heading: {line.strip()}"))
        
        # Check for empty headings (just asterisks)
        if re.match(r'^\s*#+\s*\*\*?\s*$', line.strip()):
            violations.append((line_num, f"Empty heading: {line.strip()}"))
        
        # Check for headings with single asterisks
        if re.match(r'^\s*#+\s+\*[^*]+\*\s*$', line.strip()):
            violations.append((line_num, f"Heading with asterisks: {line.strip()}"))
    
    return violations

def validate_directory(directory: Path) -> dict:
    """Validate all files in directory recursively."""
    results = {
        'files_checked': 0,
        'files_with_violations': 0,
        'total_violations': 0,
        'violations': {}
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
            
            results['files_checked'] += 1
            violations = check_file(file_path)
            
            if violations:
                results['files_with_violations'] += 1
                results['total_violations'] += len(violations)
                results['violations'][str(file_path)] = violations
    
    return results

def main():
    """Main validation function."""
    project_root = Path(__file__).parent.parent
    docs_dir = project_root / 'docs'
    
    print("🔍 Validating Markdown Headings")
    print("=" * 60)
    print()
    
    results = validate_directory(docs_dir)
    
    # Summary
    print("=" * 60)
    print("📊 Validation Summary:")
    print(f"  Files checked: {results['files_checked']}")
    print(f"  Files with violations: {results['files_with_violations']}")
    print(f"  Total violations: {results['total_violations']}")
    print()
    
    if results['total_violations'] > 0:
        print("❌ Violations found:")
        print()
        for file_path, violations in sorted(results['violations'].items()):
            rel_path = Path(file_path).relative_to(project_root)
            print(f"  📄 {rel_path}:")
            for line_num, line_content in violations:
                print(f"    Line {line_num}: {line_content[:70]}")
            print()
        print("⚠️  Please remove asterisks from headings!")
        sys.exit(1)
    else:
        print("✅ All headings are clean - no asterisks found!")
        sys.exit(0)

if __name__ == "__main__":
    main()
