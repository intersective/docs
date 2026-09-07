#!/usr/bin/env python3
"""
Fix image filenames with spaces by renaming them to use hyphens
and updating all markdown references to the new filenames.
This handles both regular spaces and URL-encoded spaces.
"""

import os
import re
import shutil
from pathlib import Path
from urllib.parse import unquote

# Specific files we know have issues (from broken link report)
FILES_TO_FIX = [
    {
        'old_name': 'Screenshot-2024-01-23-at-4.52.07 pm-1024x412.png',
        'new_name': 'Screenshot-2024-01-23-at-4.52.07-pm-1024x412.png',
        'dir': 'docs/help-articles/designing-feedback-loops/assets/images/designing-feedback-loops/allowing-resubmission',
    },
    {
        'old_name': 'Screenshot-2024-01-18-at-6.56.18 pm-1024x266.png',
        'new_name': 'Screenshot-2024-01-18-at-6.56.18-pm-1024x266.png',
        'dir': 'docs/help-articles/designing-feedback-loops/assets/images/designing-feedback-loops/preparing-feedback-loops',
    },
    {
        'old_name': 'Screenshot-2024-01-18-at-6.59.27 pm.png',
        'new_name': 'Screenshot-2024-01-18-at-6.59.27-pm.png',
        'dir': 'docs/help-articles/designing-feedback-loops/assets/images/designing-feedback-loops/preparing-feedback-loops',
    },
    {
        'old_name': 'Screenshot-2024-01-18-at-7.06.44 pm.png',
        'new_name': 'Screenshot-2024-01-18-at-7.06.44-pm.png',
        'dir': 'docs/help-articles/designing-feedback-loops/assets/images/designing-feedback-loops/preparing-feedback-loops',
    },
    {
        'old_name': 'Screenshot-2024-01-18-at-7.06.48 pm-1024x122.png',
        'new_name': 'Screenshot-2024-01-18-at-7.06.48-pm-1024x122.png',
        'dir': 'docs/help-articles/designing-feedback-loops/assets/images/designing-feedback-loops/preparing-feedback-loops',
    },
    {
        'old_name': 'Screenshot-2024-01-18-at-7.08.04 pm.png',
        'new_name': 'Screenshot-2024-01-18-at-7.08.04-pm.png',
        'dir': 'docs/help-articles/designing-feedback-loops/assets/images/designing-feedback-loops/preparing-feedback-loops',
    },
    {
        'old_name': 'Screenshot-2024-09-03-at-3.50.03 PM-289x300.png',
        'new_name': 'Screenshot-2024-09-03-at-3.50.03-PM-289x300.png',
        'dir': 'docs/help-articles/integrations/assets/images/integrations/embedding-practera-with-brightspace-lti-1-3',
    },
]

def find_file_with_variations(directory, base_name):
    """Find file with various space encodings."""
    dir_path = Path(directory)
    if not dir_path.exists():
        return None
    
    # Try different variations
    variations = [
        base_name,  # Regular space
        base_name.replace(' ', '%E2%80%AF'),  # URL-encoded
        base_name.replace(' ', '\u200f'),  # Non-breaking space
        base_name.replace(' ', '\u00a0'),  # Non-breaking space (alt)
    ]
    
    for var in variations:
        file_path = dir_path / var
        if file_path.exists():
            return file_path
    
    # Try listing directory and matching
    for file_path in dir_path.iterdir():
        if file_path.is_file():
            # Normalize both names for comparison
            normalized_old = base_name.replace(' ', '-').lower()
            normalized_file = file_path.name.replace(' ', '-').lower()
            if normalized_old in normalized_file or normalized_file in normalized_old:
                return file_path
    
    return None

def update_markdown_references(docs_dir, old_name, new_name):
    """Update all markdown references to the renamed file."""
    updated_files = []
    
    # Create patterns for various encodings
    old_name_variations = [
        old_name,  # Regular space
        old_name.replace(' ', '%E2%80%AF'),  # URL-encoded
        old_name.replace(' ', '-'),  # Already hyphenated (if someone fixed it)
    ]
    
    for md_file in Path(docs_dir).rglob('*.md'):
        try:
            content = md_file.read_text(encoding='utf-8')
            original_content = content
            
            for old_ref in old_name_variations:
                # Match image references in markdown
                # Pattern: ![alt](path/to/image.png) or [Image](path/to/image.png)
                # Escape special regex characters
                escaped_old = re.escape(old_ref)
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
    
    print("🔍 Fixing image files with spaces...")
    print("=" * 70)
    print()
    
    renamed = []
    updated_refs = []
    
    for file_info in FILES_TO_FIX:
        old_name = file_info['old_name']
        new_name = file_info['new_name']
        directory = file_info['dir']
        
        print(f"📄 Processing: {old_name}")
        
        # Find the actual file
        old_path = find_file_with_variations(directory, old_name)
        
        if not old_path:
            print(f"   ⚠️  File not found, skipping...")
            print()
            continue
        
        new_path = Path(directory) / new_name
        
        # Check if new name already exists
        if new_path.exists() and new_path != old_path:
            print(f"   ⚠️  {new_name} already exists, skipping rename")
            # Still update references
            print(f"   Updating markdown references...")
            updated = update_markdown_references(docs_dir, old_name, new_name)
            if updated:
                updated_refs.extend(updated)
                print(f"   ✅ Updated {len(updated)} markdown file(s)")
            print()
            continue
        
        # Rename the file
        try:
            old_path.rename(new_path)
            print(f"   ✅ Renamed: {old_path.name}")
            print(f"      → {new_path.name}")
            renamed.append((old_path, new_path))
        except Exception as e:
            print(f"   ❌ Error renaming: {e}")
            print()
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
    else:
        print("ℹ️  No changes needed.")

if __name__ == '__main__':
    main()
