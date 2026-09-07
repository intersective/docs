# Practera Docs

Central documentation repository for the Practera platform.

## Sites

| Site | URL | Audience | Build |
|------|-----|----------|-------|
| Support Centre | [support.practera.com](https://support.practera.com) | End users, admins | `mkdocs.yml` |
| Developer Docs | [developers.practera.com](https://developers.practera.com) | Engineering, product | `mkdocs-dev.yml` |

## Local Development

```bash
pip install -r requirements.txt

# Support Centre
mkdocs serve

# Developer Docs
mkdocs serve -f mkdocs-dev.yml
```

## Structure

```
docs/
  index.md                    # Support Centre home
  admin-platform/             # Admin app user documentation
  help-articles/              # End-user help articles
  platform/                   # Internal platform reference
  releases/                   # Release notes (auto-generated)
  faq/                        # FAQ
  operations/                 # Ops reference
  developer/                  # Developer docs (published to developers.practera.com)
    index.md                  # Platform functional spec (value chain)
    architecture.md           # System architecture overview
    design/                   # Experience Design stage
    sourcing/                 # Project Sourcing stage
    delivery/                 # Experience Delivery stage
    reporting/                # Reporting stage
    alignment/                # Cross-system alignment matrix
    api/                      # API reference
scripts/                      # Python automation (release notes, etc.)
templates/                    # Release note templates
```

## Release Notes

Release notes are auto-generated from Jira via the `release-notes` GitHub Actions workflow.

## Deployment

- **Support Centre**: Deploy via the `deploy-docs` GitHub Actions workflow (deploys from `release/live` branch to `gh-pages`)
- **Developer Docs**: Deploy via the `deploy-developer-docs` GitHub Actions workflow (Cloudflare Pages, GitHub OAuth protected)
