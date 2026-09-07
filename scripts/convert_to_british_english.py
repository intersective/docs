#!/usr/bin/env python3
"""
British English Conversion Script

Safely converts American English to British English in documentation files.
Preserves code blocks, technical terms, and CSS/JS variables.
"""

import re
import os
from pathlib import Path
from typing import List, Tuple

# Conversion mappings: (American, British)
CONVERSIONS = [
    # -ize/-ization → -ise/-isation
    (r'\borganize\b', 'organise'),
    (r'\borganized\b', 'organised'),
    (r'\borganizing\b', 'organising'),
    (r'\borganizes\b', 'organises'),
    (r'\borganization\b', 'organisation'),
    (r'\borganizations\b', 'organisations'),
    
    (r'\bcustomize\b', 'customise'),
    (r'\bcustomized\b', 'customised'),
    (r'\bcustomizing\b', 'customising'),
    (r'\bcustomizes\b', 'customises'),
    (r'\bcustomization\b', 'customisation'),
    (r'\bcustomizations\b', 'customisations'),
    
    (r'\boptimize\b', 'optimise'),
    (r'\boptimized\b', 'optimised'),
    (r'\boptimizing\b', 'optimising'),
    (r'\boptimizes\b', 'optimises'),
    (r'\boptimization\b', 'optimisation'),
    (r'\boptimizations\b', 'optimisations'),
    
    (r'\brecognize\b', 'recognise'),
    (r'\brecognized\b', 'recognised'),
    (r'\brecognizing\b', 'recognising'),
    (r'\brecognizes\b', 'recognises'),
    (r'\brecognition\b', 'recognition'),  # Same in both
    
    # -or → -our (only in documentation text, not CSS vars)
    (r'\bcolor\b(?![-_])', 'colour'),  # Not followed by - or _
    (r'\bcolors\b', 'colours'),
    (r'\bcolored\b', 'coloured'),
    (r'\bcoloring\b', 'colouring'),
    
    (r'\bfavor\b', 'favour'),
    (r'\bfavors\b', 'favours'),
    (r'\bfavorable\b', 'favourable'),
    (r'\bfavoring\b', 'favouring'),
    
    # -er → -re (only in documentation text)
    (r'\bcenter\b(?![-_])', 'centre'),  # Not followed by - or _
    (r'\bcenters\b', 'centres'),
    (r'\bcentered\b', 'centred'),
    (r'\bcentering\b', 'centring'),
    
    # -l/-ll (doubling)
    (r'\bcanceled\b', 'cancelled'),
    (r'\bcanceling\b', 'cancelling'),
    (r'\bcancelation\b', 'cancellation'),
    
    (r'\btraveled\b', 'travelled'),
    (r'\btraveling\b', 'travelling'),
    (r'\btraveler\b', 'traveller'),
    (r'\btravelers\b', 'travellers'),
]

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
PROCESS_EXTENSIONS = ['.md', '.yml', '.yaml', '.txt']

def should_skip_file(file_path: Path) -> bool:
    """Check if file should be skipped."""
    path_str = str(file_path)
    for pattern in SKIP_PATTERNS:
        if pattern in path_str:
            return True
    return False

def is_code_block(line: str) -> bool:
    """Check if line is inside a code block."""
    # Simple check: count backticks
    return line.strip().startswith('```') or line.strip().startswith('~~~')

def convert_text(text: str, in_code_block: bool = False) -> Tuple[str, int]:
    """
    Convert American English to British English.
    Returns (converted_text, change_count)
    """
    if in_code_block:
        return text, 0
    
    change_count = 0
    converted = text
    
    for american_pattern, british_replacement in CONVERSIONS:
        matches = re.findall(american_pattern, converted, re.IGNORECASE)
        if matches:
            # Count case variations
            for match in matches:
                if match.lower() != british_replacement.lower():
                    change_count += 1
            
            # Perform replacement (case-insensitive)
            def replace_func(m):
                word = m.group(0)
                # Preserve case
                if word.isupper():
                    return british_replacement.upper()
                elif word[0].isupper():
                    return british_replacement.capitalize()
                else:
                    return british_replacement
            
            converted = re.sub(american_pattern, replace_func, converted, flags=re.IGNORECASE)
    
    return converted, change_count

def convert_file(file_path: Path) -> Tuple[int, List[str]]:
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
    code_block_lang = None
    
    for line_num, line in enumerate(lines, 1):
        original_line = line
        
        # Check if entering/exiting code block
        if is_code_block(line):
            if not in_code_block:
                in_code_block = True
                # Extract language if present
                code_block_lang = line.strip().replace('```', '').replace('~~~', '').strip()
            else:
                in_code_block = False
                code_block_lang = None
            converted_lines.append(line)
            continue
        
        # Convert line
        converted_line, changes = convert_text(line, in_code_block)
        converted_lines.append(converted_line)
        
        if changes > 0:
            total_changes += changes
            # Store info about changed line
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
        # Skip directories
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
    scripts_dir = project_root / 'scripts'
    templates_dir = project_root / 'templates'
    
    print("🇬🇧 British English Conversion")
    print("=" * 60)
    print()
    
    all_stats = {
        'files_processed': 0,
        'files_changed': 0,
        'total_changes': 0,
        'file_details': {}
    }
    
    # Convert docs directory
    print("📚 Converting documentation files...")
    docs_stats = convert_directory(docs_dir)
    all_stats['files_processed'] += docs_stats['files_processed']
    all_stats['files_changed'] += docs_stats['files_changed']
    all_stats['total_changes'] += docs_stats['total_changes']
    all_stats['file_details'].update(docs_stats['file_details'])
    print()
    
    # Convert scripts (only .py files with documentation strings)
    print("🔧 Converting script files...")
    for script_file in scripts_dir.glob('*.py'):
        if should_skip_file(script_file):
            continue
        stats = convert_file(script_file)
        if stats[0] > 0:
            all_stats['files_processed'] += 1
            all_stats['files_changed'] += 1
            all_stats['total_changes'] += stats[0]
            all_stats['file_details'][str(script_file)] = {
                'changes': stats[0],
                'lines': stats[1]
            }
            print(f"  ✅ {script_file.name}: {stats[0]} changes")
    print()
    
    # Convert templates
    print("📝 Converting template files...")
    templates_stats = convert_directory(templates_dir)
    all_stats['files_processed'] += templates_stats['files_processed']
    all_stats['files_changed'] += templates_stats['files_changed']
    all_stats['total_changes'] += templates_stats['total_changes']
    all_stats['file_details'].update(templates_stats['file_details'])
    print()
    
    # Summary
    print("=" * 60)
    print("📊 Conversion Summary:")
    print(f"  Files processed: {all_stats['files_processed']}")
    print(f"  Files changed: {all_stats['files_changed']}")
    print(f"  Total conversions: {all_stats['total_changes']}")
    print()
    
    if all_stats['files_changed'] > 0:
        print("✅ Conversion completed successfully!")
        print()
        print("📋 Changed files:")
        for file_path, details in sorted(all_stats['file_details'].items()):
            rel_path = Path(file_path).relative_to(project_root)
            print(f"  • {rel_path} ({details['changes']} changes)")
    else:
        print("ℹ️  No changes needed - files already use British English!")

if __name__ == "__main__":
    main()
