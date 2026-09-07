#!/usr/bin/env python3
"""
Rename Image Directories to Remove -practera-2 Suffix

This script renames image directories to match the updated markdown references
after we removed "Practera 2" from file names but forgot to rename directories.
"""

import os
import shutil
from pathlib import Path
from typing import List, Dict

# Directory renaming map: old_name -> new_name
DIRECTORY_RENAME_MAP = {
    'managing-your-feedback-loops-practera-2': 'managing-your-feedback-loops',
    'reportcard-practera-2': 'reportcard',
    'preparing-feedback-loops-practera-2': 'preparing-feedback-loops',
    'release-notes-practera-2': 'release-notes',
    'adding-new-administrators-authors-and-coordinators-and-institution-wide-user-overview-practera-2': 'adding-new-administrators-authors-and-coordinators-and-institution-wide-user-overview',
    'understanding-user-roles-practera-2': 'understanding-user-roles',
    'whats-the-difference-between-locking-and-hiding-practera-2': 'whats-the-difference-between-locking-and-hiding',
    'sending-assessment-reminders-practera-2': 'sending-assessment-reminders',
    'the-experience-dashboard-explained-practera-2': 'the-experience-dashboard-explained',
    'bulk-enrolment-via-csv-upload-practera-2': 'bulk-enrolment-via-csv-upload',
    'communicating-with-learners-and-experts-practera-2': 'communicating-with-learners-and-experts',
    'the-experience-portal-explained-practera-2': 'the-experience-portal-explained',
    'logging-in-practera-2': 'logging-in',
}

def find_image_directories(docs_dir: Path) -> List[Dict]:
    """
    Find all image directories that need to be renamed.
    Returns list of directories to rename: {old_path, new_path, parent_dir}
    """
    directories_to_rename = []
    
    for root, dirs, files in os.walk(docs_dir):
        # Skip certain directories
        if 'node_modules' in root or '.git' in root or 'site' in root:
            continue
        
        # Look for assets/images directories
        if 'assets' in root and 'images' in root:
            for dir_name in dirs:
                if dir_name in DIRECTORY_RENAME_MAP:
                    old_path = Path(root) / dir_name
                    new_name = DIRECTORY_RENAME_MAP[dir_name]
                    new_path = Path(root) / new_name
                    
                    directories_to_rename.append({
                        'old_path': old_path,
                        'new_path': new_path,
                        'old_name': dir_name,
                        'new_name': new_name,
                        'parent': Path(root)
                    })
    
    return directories_to_rename

def rename_directory(old_path: Path, new_path: Path) -> bool:
    """Rename a directory."""
    try:
        if old_path.exists() and old_path.is_dir():
            # Check if new path already exists
            if new_path.exists():
                print(f"  ⚠️  Warning: {new_path.name} already exists. Skipping.")
                return False
            
            shutil.move(str(old_path), str(new_path))
            return True
        else:
            print(f"  ⚠️  Warning: {old_path} does not exist. Skipping.")
            return False
    except Exception as e:
        print(f"  ❌ Error renaming {old_path}: {e}")
        return False

def main():
    """Main function."""
    project_root = Path(__file__).parent.parent
    docs_dir = project_root / 'docs'
    
    if not docs_dir.exists():
        print(f"Error: docs directory not found at {docs_dir}")
        return 1
    
    print("🔧 Renaming Image Directories to Remove -practera-2 Suffix")
    print("=" * 70)
    print()
    
    # Find directories to rename
    directories_to_rename = find_image_directories(docs_dir)
    
    if not directories_to_rename:
        print("ℹ️  No directories found that need renaming.")
        return 0
    
    print(f"📁 Found {len(directories_to_rename)} directories to rename:")
    print()
    
    # Group by parent directory for better organization
    by_parent = {}
    for dir_info in directories_to_rename:
        parent_key = str(dir_info['parent'].relative_to(project_root))
        if parent_key not in by_parent:
            by_parent[parent_key] = []
        by_parent[parent_key].append(dir_info)
    
    total_renamed = 0
    total_failed = 0
    
    for parent_path, dirs in sorted(by_parent.items()):
        print(f"📂 {parent_path}")
        for dir_info in dirs:
            old_path = dir_info['old_path']
            new_path = dir_info['new_path']
            rel_old = old_path.relative_to(project_root)
            rel_new = new_path.relative_to(project_root)
            
            print(f"   {dir_info['old_name']} → {dir_info['new_name']}")
            
            if rename_directory(old_path, new_path):
                total_renamed += 1
                print(f"   ✅ Renamed successfully")
            else:
                total_failed += 1
                print(f"   ❌ Failed to rename")
        print()
    
    print("=" * 70)
    print(f"📊 Summary:")
    print(f"  Directories renamed: {total_renamed}")
    print(f"  Directories failed: {total_failed}")
    print()
    
    if total_renamed > 0:
        print("✅ Image directory renaming completed!")
        print()
        print("💡 Next: Verify images load correctly by:")
        print("   1. Running: python3 scripts/find_broken_links.py")
        print("   2. Building site: mkdocs build")
        print("   3. Testing locally: ./local.sh")
        return 0
    else:
        print("⚠️  No directories were renamed.")
        return 1

if __name__ == "__main__":
    exit(main())
