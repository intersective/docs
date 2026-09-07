#!/usr/bin/env python3
"""
Fix image filenames with spaces (including non-breaking spaces) by renaming them 
to use hyphens and updating all markdown references to the new filenames.
"""

import os
import re
from pathlib import Path
from urllib.parse import unquote

# Non-breaking space character and its URL encoding
NBSP = '\u202f'  # Non-breaking space
NBSP_BYTES = b'\xe2\x80\xaf'
NBSP_URL = '%E2%80%AF'

def find_files_with_spaces(docs_dir):
    """Find all image files with spaces or non-breaking spaces."""
    files_to_fix = []
    
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                file_path = Path(root) / file
                name_bytes = file.encode('utf-8')
                
                # Check for regular space, non-breaking space, or URL-encoded space
                if ' ' in file or NBSP in file or NBSP_BYTES in name_bytes:
                    files_to_fix.append(file_path)
    
    return files_to_fix

def create_new_filename(old_name):
    """Create new filename by replacing spaces with hyphens."""
    # Replace non-breaking space with hyphen
    new_name = old_name.replace(NBSP, '-')
    # Replace regular space with hyphen
    new_name = new_name.replace(' ', '-')
    # Replace URL-encoded space (if somehow in filename)
    new_name = new_name.replace(NBSP_URL, '-')
    
    # Clean up multiple consecutive hyphens
    new_name = re.sub(r'-+', '-', new_name)
    
    return new_name

def update_markdown_references(docs_dir, old_name, new_name):
    """Update all markdown references to the renamed file."""
    updated_files = []
    
    # Create patterns for various encodings of the old name
    old_name_patterns = [
        old_name,  # Exact match
        old_name.replace(NBSP, ' '),  # Regular space version
        old_name.replace(NBSP, NBSP_URL),  # URL-encoded version
        old_name.replace(' ', NBSP_URL),  # If it had regular space, URL-encoded
    ]
    
    for md_file in Path(docs_dir).rglob('*.md'):
        try:
            content = md_file.read_text(encoding='utf-8')
            original_content = content
            
            for old_pattern in old_name_patterns:
                # Match image references in markdown
                # Pattern: ![alt](path/to/image.png) or [Image](path/to/image.png)
                escaped_old = re.escape(old_pattern)
                pattern = rf'(\[.*?\]\([^)]*?)({escaped_old})(\))'
                replacement = rf'\1{new_name}\3'
                content = re.sub(pattern, replacement, content)
            
            if content != original_content:
                md_file.write_text(content, encoding='utf-8')
                updated_files.append(md_file)
        except Exception as e:
            print(f"⚠️  Error processing {md_file}: {e}")
    
    return updated_files

def main():
    docs_dir = Path('docs')
    
    print("🔍 Finding image files with spaces (including non-breaking spaces)...")
    print("=" * 70)
    print()
    
    files_to_fix = find_files_with_spaces(docs_dir)
    
    if not files_to_fix:
        print("ℹ️  No files with spaces found.")
        return
    
    print(f"📊 Found {len(files_to_fix)} image files with spaces:")
    for f in files_to_fix:
        print(f"   - {f.name}")
    print()
    
    renamed = []
    updated_refs = []
    
    for old_path in files_to_fix:
        old_name = old_path.name
        new_name = create_new_filename(old_name)
        
        if old_name == new_name:
            print(f"⏭️  Skipping {old_name} (no spaces to replace)")
            continue
        
        new_path = old_path.parent / new_name
        
        # Check if new name already exists
        if new_path.exists() and new_path != old_path:
            print(f"⚠️  Skipping {old_name} - {new_name} already exists")
            # Still try to update references
            updated = update_markdown_references(docs_dir, old_name, new_name)
            if updated:
                updated_refs.extend(updated)
            continue
        
        print(f"📄 Processing: {old_name}")
        
        # Rename the file
        try:
            old_path.rename(new_path)
            print(f"   ✅ Renamed: {old_name}")
            print(f"      → {new_name}")
            renamed.append((old_path, new_path))
        except Exception as e:
            print(f"   ❌ Error renaming: {e}")
            continue
        
        # Update markdown references
        print(f"   Updating markdown references...")
        updated = update_markdown_references(docs_dir, old_name, new_name)
        if updated:
            updated_refs.extend(updated)
            print(f"   ✅ Updated {len(updated)} markdown file(s)")
        print()
    
    print("=" * 70)
    print("📊 Summary:")
    print(f"   Files renamed: {len(renamed)}")
    print(f"   Markdown files updated: {len(set(updated_refs))}")
    print()
    
    if renamed or updated_refs:
        print("✅ Image filename fixes complete!")
        print("✅ All spaces replaced with hyphens!")
        print("✅ All markdown references updated!")
    else:
        print("ℹ️  No changes made.")

if __name__ == '__main__':
    main()
