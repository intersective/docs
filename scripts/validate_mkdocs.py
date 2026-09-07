#!/usr/bin/env python3
"""
MkDocs Configuration Validator
Validates mkdocs.yml syntax and checks all navigation files exist
"""

import yaml
import os
import sys

def validate_mkdocs_config():
    """Validate MkDocs configuration and navigation files"""
    
    print("🔍 Validating MkDocs configuration...")
    
    # Check if mkdocs.yml exists
    if not os.path.exists('mkdocs.yml'):
        print("❌ mkdocs.yml not found")
        return False
    
    # Validate mkdocs.yml syntax
    try:
        with open('mkdocs.yml', 'r') as f:
            config = yaml.safe_load(f)
        print("✅ mkdocs.yml syntax is valid")
    except Exception as e:
        print(f"❌ mkdocs.yml syntax error: {e}")
        return False
    
    # Check if docs directory exists
    if not os.path.exists('docs'):
        print("❌ docs directory not found")
        return False
    
    print("🔍 Checking for broken links in navigation...")
    
    def check_nav_files(nav_item, path=''):
        """Recursively check navigation files exist"""
        missing_files = []
        
        if isinstance(nav_item, dict):
            for key, value in nav_item.items():
                missing_files.extend(check_nav_files(value, f'{path}/{key}'))
        elif isinstance(nav_item, list):
            for item in nav_item:
                missing_files.extend(check_nav_files(item, path))
        elif isinstance(nav_item, str) and nav_item.endswith('.md'):
            file_path = f'docs/{nav_item}' if not nav_item.startswith('/') else nav_item[1:]
            if not os.path.exists(file_path):
                missing_files.append(file_path)
                print(f"❌ Missing file: {file_path}")
            else:
                print(f"✅ Found: {file_path}")
        
        return missing_files
    
    nav = config.get('nav', [])
    missing_files = check_nav_files(nav)
    
    if missing_files:
        print(f"❌ Found {len(missing_files)} missing files")
        return False
    else:
        print("✅ All navigation files exist")
        return True

if __name__ == "__main__":
    if validate_mkdocs_config():
        print("🎉 MkDocs configuration validation passed!")
        sys.exit(0)
    else:
        print("💥 MkDocs configuration validation failed!")
        sys.exit(1) 