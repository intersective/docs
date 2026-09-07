#!/usr/bin/env python3
"""
Find Broken Links in MkDocs Documentation

This script identifies broken internal links by:
1. Finding all markdown links
2. Resolving relative paths
3. Checking if target files exist
4. Identifying duplicate path segments
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple
from urllib.parse import urlparse

def is_code_block(line: str, in_code_block: bool) -> bool:
    """Check if line is inside a code block."""
    stripped = line.strip()
    if stripped.startswith('```') or stripped.startswith('~~~'):
        return not in_code_block
    return in_code_block

def extract_links(content: str, file_path: Path) -> List[Dict]:
    """Extract all markdown links from content."""
    links = []
    in_code_block = False
    lines = content.split('\n')
    
    # Pattern for markdown links: [text](url) or [text](url "title")
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    for line_num, line in enumerate(lines, 1):
        in_code_block = is_code_block(line, in_code_block)
        if in_code_block:
            continue
            
        matches = re.finditer(link_pattern, line)
        for match in matches:
            link_text = match.group(1)
            link_url = match.group(2)
            
            # Skip external URLs
            if link_url.startswith('http://') or link_url.startswith('https://') or link_url.startswith('mailto:'):
                continue
            
            # Skip anchors only
            if link_url.startswith('#'):
                continue
            
            links.append({
                'line': line_num,
                'text': link_text,
                'url': link_url,
                'file': file_path
            })
    
    return links

def resolve_link_path(link_url: str, source_file: Path, docs_root: Path) -> Tuple[Path, bool, str]:
    """
    Resolve a relative link path to an absolute file path.
    Returns: (resolved_path, exists, error_message)
    """
    # Remove anchor if present
    if '#' in link_url:
        link_url = link_url.split('#')[0]
    
    # Remove query parameters
    if '?' in link_url:
        link_url = link_url.split('?')[0]
    
    # Handle absolute paths (from docs root)
    if link_url.startswith('/'):
        resolved = docs_root / link_url.lstrip('/')
    # Handle relative paths
    else:
        # Get source file's directory
        source_dir = source_file.parent
        # Resolve relative path
        resolved = (source_dir / link_url).resolve()
    
    # Normalize path
    resolved = resolved.resolve()
    
    # Check if it's within docs root
    try:
        resolved.relative_to(docs_root)
    except ValueError:
        return resolved, False, "Path outside docs directory"
    
    # Check if file exists
    if resolved.exists() and resolved.is_file():
        return resolved, True, ""
    
    # Check if it's a markdown file without extension
    if not resolved.suffix:
        md_file = resolved.with_suffix('.md')
        if md_file.exists():
            return md_file, True, ""
    
    # Check if directory with index.md
    if resolved.is_dir():
        index_file = resolved / 'index.md'
        if index_file.exists():
            return index_file, True, ""
    
    return resolved, False, "File not found"

def check_for_duplicate_path_segments(link_url: str, source_file: Path) -> bool:
    """Check if link URL contains duplicate path segments."""
    # Remove anchor
    if '#' in link_url:
        link_url = link_url.split('#')[0]
    
    # Get source file's directory path relative to docs
    source_dir = source_file.parent
    source_parts = source_dir.parts
    
    # Parse link URL
    if link_url.startswith('/'):
        # Absolute path
        link_parts = link_url.strip('/').split('/')
    else:
        # Relative path - resolve it
        try:
            resolved = (source_dir / link_url).resolve()
            # Get relative path from docs
            docs_root = Path('docs')
            try:
                rel_path = resolved.relative_to(docs_root)
                link_parts = list(rel_path.parent.parts) if resolved.is_file() else list(rel_path.parts)
            except ValueError:
                return False
        except:
            return False
    
    # Check for consecutive duplicate segments
    for i in range(len(link_parts) - 1):
        if link_parts[i] == link_parts[i + 1]:
            return True
    
    # Check if source directory name appears twice in resolved path
    if len(source_parts) > 0:
        source_dir_name = source_parts[-1]
        count = link_parts.count(source_dir_name)
        if count > 1:
            return True
    
    return False

def analyze_links(docs_dir: Path) -> Dict:
    """Analyze all links in documentation."""
    broken_links = []
    duplicate_path_links = []
    all_links = []
    
    for root, dirs, files in os.walk(docs_dir):
        # Skip certain directories
        if 'node_modules' in root or '.git' in root or 'site' in root:
            continue
        
        for file in files:
            if not file.endswith('.md'):
                continue
            
            file_path = Path(root) / file
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue
            
            links = extract_links(content, file_path)
            
            for link in links:
                all_links.append(link)
                
                # Check for duplicate path segments
                if check_for_duplicate_path_segments(link['url'], file_path):
                    duplicate_path_links.append({
                        **link,
                        'issue': 'duplicate_path_segment',
                        'message': f"Link contains duplicate path segments: {link['url']}"
                    })
                
                # Resolve and check if file exists
                resolved_path, exists, error = resolve_link_path(
                    link['url'],
                    file_path,
                    docs_dir
                )
                
                if not exists:
                    broken_links.append({
                        **link,
                        'resolved_path': str(resolved_path),
                        'issue': 'file_not_found',
                        'message': error or f"File not found: {resolved_path}"
                    })
    
    return {
        'total_links': len(all_links),
        'broken_links': broken_links,
        'duplicate_path_links': duplicate_path_links,
        'all_links': all_links
    }

def main():
    """Main function."""
    project_root = Path(__file__).parent.parent
    docs_dir = project_root / 'docs'
    
    if not docs_dir.exists():
        print(f"Error: docs directory not found at {docs_dir}")
        return
    
    print("🔍 Analyzing Links in MkDocs Documentation")
    print("=" * 70)
    print()
    
    results = analyze_links(docs_dir)
    
    print(f"📊 Summary:")
    print(f"  Total links found: {results['total_links']}")
    print(f"  Broken links: {len(results['broken_links'])}")
    print(f"  Duplicate path links: {len(results['duplicate_path_links'])}")
    print()
    
    # Report duplicate path links
    if results['duplicate_path_links']:
        print("=" * 70)
        print("⚠️  DUPLICATE PATH SEGMENT LINKS (Likely cause of 404 errors):")
        print("=" * 70)
        
        # Group by file
        by_file = {}
        for link in results['duplicate_path_links']:
            file_key = str(link['file'])
            if file_key not in by_file:
                by_file[file_key] = []
            by_file[file_key].append(link)
        
        for file_path, links in sorted(by_file.items()):
            rel_path = Path(file_path).relative_to(project_root)
            print(f"\n📄 {rel_path}")
            for link in links:
                print(f"   Line {link['line']}: [{link['text']}]({link['url']})")
                print(f"   ⚠️  Issue: {link['message']}")
    
    # Report broken links
    if results['broken_links']:
        print()
        print("=" * 70)
        print("❌ BROKEN LINKS (File not found):")
        print("=" * 70)
        
        # Group by file
        by_file = {}
        for link in results['broken_links']:
            file_key = str(link['file'])
            if file_key not in by_file:
                by_file[file_key] = []
            by_file[file_key].append(link)
        
        for file_path, links in sorted(by_file.items()):
            rel_path = Path(file_path).relative_to(project_root)
            print(f"\n📄 {rel_path}")
            for link in links:
                print(f"   Line {link['line']}: [{link['text']}]({link['url']})")
                print(f"   ❌ Resolved to: {link['resolved_path']}")
                print(f"   ❌ Error: {link['message']}")
    
    print()
    print("=" * 70)
    
    if results['duplicate_path_links'] or results['broken_links']:
        print("❌ Issues found! Review the links above.")
        return 1
    else:
        print("✅ No broken links found!")
        return 0

if __name__ == "__main__":
    exit(main())
