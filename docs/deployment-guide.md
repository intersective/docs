# Deployment Guide

This guide explains how to deploy your documentation changes to the live environment using GitHub Actions.

## 🚀 Manual Deployment Workflow

The **Deploy Documentation** workflow allows you to manually deploy your local changes to the live site.

### How to Use

1. **Go to GitHub Actions**:
   - Navigate to your repository on GitHub
   - Click on the **Actions** tab
   - Select **Deploy Documentation** from the workflow list

2. **Run the Workflow**:
   - Click **Run workflow**
   - Configure deployment options:

#### Deployment Options

| Option | Description | Options |
|--------|-------------|---------|
| **Branch** | Source branch to deploy from | Default: `release/live`, or specify any branch name |
| **Force Deploy** | Force deployment even without changes | `true` or `false` (default: false) |

> **Note:** All deployments go to **support.practera.com** - no environment selection needed!

### 📋 What the Workflow Does

1. **Validates** your documentation:
   - Checks MkDocs configuration
   - Verifies all navigation links exist
   - Ensures critical files are present

2. **Builds** the site:
   - Runs `mkdocs build`
   - Generates static HTML files
   - Optimises assets and stylesheets

3. **Tests** the built site:
   - Verifies critical pages exist (index, FAQ, releases)
   - Checks for assets and stylesheets
   - Validates site structure

4. **Deploys** to GitHub Pages:
   - Publishes to support.practera.com
   - Uses existing CNAME configuration
   - Provides deployment summary

### 🌐 Access Your Deployed Site

After successful deployment:
- **Main Site**: https://support.practera.com
- **FAQ Section**: https://support.practera.com/faq/
- **Release Notes**: https://support.practera.com/releases/

### ⏱️ Deployment Timeline

- **Build time**: 2-3 minutes
- **Deployment time**: 1-2 minutes
- **CDN propagation**: 2-5 minutes
- **Total time**: ~5-10 minutes

### 🔧 Troubleshooting

#### Common Issues

1. **Missing Files Error**:
   - Check that all files referenced in navigation exist
   - Verify file paths are correct in `mkdocs.yml`

2. **Build Failure**:
   - Ensure `requirements.txt` includes all dependencies
   - Check MkDocs configuration syntax

3. **Deployment Failure**:
   - Verify GitHub Pages is enabled in repository settings
   - Check that secrets are configured if needed

#### Getting Help

- **View workflow logs** in GitHub Actions for detailed error messages
- **Check the deployment summary** for quick status information
- **Contact the DevOps team** for infrastructure issues

### 🔄 Automatic Workflows

For release notes, use the **Release Notes Automation** workflow which:
- Fetches issues from Jira
- Generates release notes with AI
- Automatically deploys the updated documentation

## Best Practices

1. **Test locally first**: Run `mkdocs serve` to preview changes
2. **Deploy from release/live**: Use your main `release/live` branch for production
3. **Review changes**: Ensure all updates are tested before deploying
4. **Monitor deployment**: Check the deployment summary and verify the live site
5. **Regular deployments**: Deploy frequently to keep documentation current

---

*For technical questions about the deployment process, contact the DevOps team.* 