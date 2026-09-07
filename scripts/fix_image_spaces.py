#!/usr/bin/env python3
"""
Fix image filenames with spaces by renaming them to use hyphens
and updating all markdown references to the new filenames.
"""

import os
import re
from pathlib import Path
from urllib.parse import unquote

def find_images_with_spaces(docs_dir):
    """Find all image files with spaces in their names."""
    images_with_spaces = []
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                if ' ' in file or '%E2%80%AF' in file:
                    full_path = Path(root) / file
                    images_with_spaces.append(full_path)
    return images_with_spaces

def rename_file_remove_spaces(file_path):
    """Rename file to replace spaces with hyphens."""
    old_name = file_path.name
    new_name = old_name.replace(' ', '-').replace('%E2%80%AF', '-')
    
    # Clean up multiple consecutive hyphens
    new_name = re.sub(r'-+', '-', new_name)
    
    if old_name == new_name:
        return None, None
    
    new_path = file_path.parent / new_name
    return file_path, new_path

def update_markdown_references(docs_dir, old_path, new_path):
    """Update all markdown references to the renamed file."""
    old_name = old_path.name
    new_name = new_path.name
    
    # Also check for URL-encoded version
    old_name_encoded = old_name.replace(' ', '%E2%80%AF')
    
    updated_files = []
    
    for md_file in Path(docs_dir).rglob('*.md'):
        try:
            content = md_file.read_text(encoding='utf-8')
            original_content = content
            
            # Replace various forms of the reference
            patterns = [
                (old_name, new_name),
                (old_name_encoded, new_name),
                (unquote(old_name_encoded), new_name),
            ]
            
            for old_ref, new_ref in patterns:
                # Match image references in markdown
                # Pattern: ![alt](path/to/image.png) or [Image](path/to/image.png)
                pattern = rf'(\[.*?\]\([^)]*?)({re.escape(old_ref)})(\))'
                replacement = rf'\1{new_ref}\3'
                content = re.sub(pattern, replacement, content)
            
            if content != original_content:
                md_file.write_text(content, encoding='utf-8')
                updated_files.append(md_file)
        except Exception as e:
            print(f"⚠️  Error processing {md_file}: {e}")
    
    return updated_files

def main():
    docs_dir = Path('docs')
    
    print("🔍 Finding image files with spaces...")
    images_with_spaces = find_images_with_spaces(docs_dir)
    
    print(f"📊 Found {len(images_with_spaces)} image files with spaces")
    print()
    
    renamed = []
    updated_refs = []
    
    for img_path in images_with_spaces:
        old_path, new_path = rename_file_remove_spaces(img_path)
        
        if old_path and new_path:
            # Check if new name already exists
            if new_path.exists():
                print(f"⚠️  Skipping {old_path.name} - {new_path.name} already exists")
                continue
            
            # Rename the file
            old_path.rename(new_path)
            print(f"✅ Renamed: {old_path.name}")
            print(f"   → {new_path.name}")
            
            renamed.append((old_path, new_path))
            
            # Update markdown references
            print(f"   Updating markdown references...")
            updated = update_markdown_references(docs_dir, old_path, new_path)
            if updated:
                updated_refs.extend(updated)
                print(f"   ✅ Updated {len(updated)} markdown file(s)")
            print()
    
    print("=" * 70)
    print("📊 Summary:")
    print(f"   Files renamed: {len(renamed)}")
    print(f"   Markdown files updated: {len(set(updated_refs))}")
    print()
    
    if renamed:
        print("✅ All image files with spaces have been renamed!")
        print("✅ All markdown references have been updated!")
    else:
        print("ℹ️  No files needed renaming.")

if __name__ == '__main__':
    main()
