#!/usr/bin/env python3
"""
Jira Issue Fetcher

This script fetches issues from Jira and prepares them for release notes generation.
"""

import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import sys
import argparse
import re

import jira
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class JiraIssueFetcher:
    def __init__(self):
        self.jira_url = os.getenv("JIRA_BASE_URL")
        self.jira_email = os.getenv("JIRA_USER_EMAIL")
        self.jira_token = os.getenv("JIRA_API_TOKEN")

        if not all([self.jira_url, self.jira_email, self.jira_token]):
            logger.error("Missing one or more required Jira credentials.")
            logger.error(f"JIRA_BASE_URL: {'SET' if self.jira_url else 'NOT SET'}")
            logger.error(f"JIRA_USER_EMAIL: {'SET' if self.jira_email else 'NOT SET'}")
            logger.error(f"JIRA_API_TOKEN: {'SET' if self.jira_token else 'NOT SET'}")
            raise EnvironmentError("Missing required Jira credentials in environment")

        self.client = jira.JIRA(
            server=self.jira_url,
            basic_auth=(self.jira_email, self.jira_token)
        )

        self.max_results = 1000
        self.issue_types = {
            "feature": ["New Feature", "Story"],
            "bug": ["Bug"],
            "improvement": ["Improvement", "Task"],
            "security": ["Security"],
            "technical": ["Technical Task"]
        }
        
        # Create processing directory if it doesn't exist
        self.processing_dir = Path(__file__).parent / "processing"
        self.processing_dir.mkdir(exist_ok=True)

    def _clean_text(self, text: str) -> str:
        if not text:
            return ""
        junk = ["{code}", "{/code}", "{panel}", "{/panel}"]
        for marker in junk:
            text = text.replace(marker, "")
        boilerplate = [
            "h1.", "h2.", "h3.", "h4.", "h5.", "h6.",
            "*", "_", "~", "+", "-", "^", "{{", "}}",
            "{colour}", "{/colour}", "{status}", "{/status}"
        ]
        for marker in boilerplate:
            text = text.replace(marker, "")
        return " ".join(text.split())

    def _categorize_issue(self, issue: Dict) -> str:
        issue_type = issue.get("type", "").lower()
        for category, types in self.issue_types.items():
            if issue_type in [t.lower() for t in types]:
                return category
        labels = [label.lower() for label in issue.get("labels", [])]
        if "security" in labels:
            return "security"
        if "technical" in labels:
            return "technical"
        return "improvement"

    def _format_issue(self, issue: Dict) -> Dict:
        return {
            "key": issue["key"],
            "summary": self._clean_text(issue["summary"]),
            "description": self._clean_text(issue.get("description", "")),
            "type": issue.get("type", ""),
            "priority": issue.get("priority", ""),
            "status": issue.get("status", ""),
            "labels": issue.get("labels", []),
            "components": issue.get("components", []),
            "category": self._categorize_issue(issue)
        }

    def _generate_markdown(self, issues: List[Dict], release_tag: str, fetch_date: str) -> str:
        """Generate markdown content from issues."""
        # Extract version from release_tag
        version = release_tag.split(" ", 1)[1] if release_tag.lower().startswith("release ") else release_tag
        
        # Start with header
        md_content = [
            f"# Release Notes v{version}",
            f"\n**Release Date:** {fetch_date.split('T')[0]}",
            "\n## Overview",
            "\nThis release includes the following changes:"
        ]

        # Group issues by category
        categorized_issues = {}
        for issue in issues:
            category = issue["category"]
            if category not in categorized_issues:
                categorized_issues[category] = []
            categorized_issues[category].append(issue)

        # Add sections for each category
        category_headers = {
            "feature": "### New Features",
            "bug": "### Bug Fixes",
            "security": "### Security Improvements",
            "improvement": "### Enhancements",
            "technical": "### Technical Changes"
        }

        for category, header in category_headers.items():
            if category in categorized_issues and categorized_issues[category]:
                md_content.append(f"\n{header}")
                for issue in categorized_issues[category]:
                    md_content.append(f"\n- [{issue['key']}]({self.jira_url}/browse/{issue['key']}) - {issue['summary']}")
                    if issue['description']:
                        md_content.append(f"  - {issue['description']}")

        return "\n".join(md_content)

    def fetch_issues(self, release_tag: str) -> List[Dict]:
        try:
            jql = f'fixVersion = "{release_tag}" ORDER BY type DESC, priority DESC'
            issues = self.client.search_issues(
                jql,
                maxResults=self.max_results,
                fields="summary,description,issuetype,priority,status,labels,components"
            )
            logger.info(f"Fetched {len(issues)} issues for release {release_tag}")
            formatted_issues = []
            for issue in issues:
                formatted = self._format_issue({
                    "key": issue.key,
                    "summary": issue.fields.summary,
                    "description": issue.fields.description,
                    "type": issue.fields.issuetype.name,
                    "priority": issue.fields.priority.name,
                    "status": issue.fields.status.name,
                    "labels": issue.fields.labels,
                    "components": [c.name for c in issue.fields.components]
                })
                formatted_issues.append(formatted)
            return formatted_issues
        except Exception as e:
            logger.error(f"Error fetching issues: {str(e)}")
            raise

def list_jira_releases():
    jira_url = os.getenv("JIRA_BASE_URL")
    jira_email = os.getenv("JIRA_USER_EMAIL")
    jira_token = os.getenv("JIRA_API_TOKEN")
    if not all([jira_url, jira_email, jira_token]):
        print("Missing Jira credentials in environment.")
        exit(1)
    client = jira.JIRA(server=jira_url, basic_auth=(jira_email, jira_token))
    # List all projects and their releases
    projects = client.projects()
    for project in projects:
        print(f"Project: {project.key} - {project.name}")
        try:
            versions = client.project(project.key).versions
            print(f"  Releases (fixVersions):")
            for v in versions:
                print(f"    - {v.name}")
        except Exception as e:
            print(f"  Could not fetch versions: {e}")

def main():
    parser = argparse.ArgumentParser(description="Fetch Jira issues for a release or list available releases.")
    parser.add_argument("release_tag", nargs="?", help="Release name as in Jira (e.g., 'Release 2.4.5')")
    parser.add_argument("--list", action="store_true", help="List all available releases (fixVersions) and exit.")
    args = parser.parse_args()

    if args.list:
        list_jira_releases()
        sys.exit(0)

    if not args.release_tag:
        print("Usage: python fetch_jira.py <RELEASE_TAG> or python fetch_jira.py --list")
        sys.exit(1)
    release_tag = args.release_tag
    fetcher = JiraIssueFetcher()
    issues = fetcher.fetch_issues(release_tag)
    if not issues:
        print(f"No issues found for release '{release_tag}'. Please check the release name and try again.")
        sys.exit(0)
    # Generate markdown content
    fetch_date = datetime.now().isoformat()
    md_content = fetcher._generate_markdown(issues, release_tag, fetch_date)
    # Extract version for filename using regex
    match = re.search(r'[0-9]+(\.[0-9]+)+', release_tag)
    version = match.group(0) if match else release_tag
    # Save as markdown file with to_llm_ prefix
    output_path = fetcher.processing_dir / f"to_llm_v{version}.md"
    with open(output_path, "w") as f:
        f.write(md_content)
    logger.info(f"Release notes saved to {output_path}")
    # No longer call summarize_llm.py here; pipeline should handle next steps

if __name__ == "__main__":
    main()
