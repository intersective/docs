<!-- status: living -->
# Developer Docs Site Setup (Cloudflare)

This page documents the one-time setup required to publish `developers.practera.com` via Cloudflare Pages with GitHub OAuth access control.

## Prerequisites

- Access to the Cloudflare account used for `practera.com`
- GitHub org admin access to `intersective`
- `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` added as GitHub repository secrets in `intersective/practera-docs`

---

## Step 1: Create Cloudflare Pages Project

1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com)
2. Go to **Workers & Pages** → **Pages** → **Create a project**
3. Choose **Direct Upload** (we deploy via GitHub Actions, not Git integration)
4. Name the project: `practera-developer-docs`
5. Click **Create project** (skip the initial upload — the workflow will handle it)

---

## Step 2: Configure Custom Domain

1. In the Pages project, go to **Custom domains**
2. Add `developers.practera.com`
3. Cloudflare will automatically create the DNS record (since the domain is already on Cloudflare)
4. Wait for the SSL certificate to provision (usually a few minutes)

---

## Step 3: Configure Cloudflare Access (GitHub OAuth)

This restricts the developer docs site to members of the `intersective` GitHub organisation.

1. In the Cloudflare dashboard, go to **Zero Trust** → **Access** → **Applications**
2. Click **Add an application** → **Self-hosted**
3. Configure:
   - **Application name**: `Practera Developer Docs`
   - **Session duration**: `24 hours`
   - **Application domain**: `developers.practera.com`
4. Under **Identity providers**, add/select **GitHub**
   - If GitHub is not yet configured as an IdP, go to **Settings** → **Authentication** → **Login methods** → **Add new** → **GitHub**
   - You will need to create a GitHub OAuth App at [github.com/organizations/intersective/settings/applications](https://github.com/organizations/intersective/settings/applications)
   - Set the callback URL to: `https://<your-team>.cloudflareaccess.com/cdn-cgi/access/callback`
5. Create an **Access Policy**:
   - **Policy name**: `Intersective GitHub Org Members`
   - **Action**: Allow
   - **Include rule**: `GitHub organization` = `intersective`
6. Save the application

---

## Step 4: Add GitHub Repository Secrets

In [github.com/intersective/practera-docs/settings/secrets/actions](https://github.com/intersective/practera-docs/settings/secrets/actions):

| Secret | Value |
|--------|-------|
| `CLOUDFLARE_API_TOKEN` | API token with `Cloudflare Pages:Edit` permission |
| `CLOUDFLARE_ACCOUNT_ID` | Found in Cloudflare dashboard sidebar (Account ID) |

To create the API token:
1. Go to [Cloudflare API Tokens](https://dash.cloudflare.com/profile/api-tokens)
2. **Create Token** → **Custom token**
3. Permissions: `Cloudflare Pages` → `Edit`
4. Account Resources: `Include` → `[your account]`
5. Create and copy the token

---

## Step 5: Deploy

Trigger the workflow manually:

```bash
gh workflow run deploy-developer-docs.yml --repo intersective/practera-docs
```

Or push to `main` with changes in `docs/developer/**`.

After the first successful deployment, the site will be available at `https://developers.practera.com` (protected by Cloudflare Access).

---

## Maintenance Notes

- The developer docs are built from `mkdocs-dev.yml` using MkDocs Material
- Content lives in `docs/developer/` in the `main` branch
- The workflow builds into `site-dev/` and uploads to Cloudflare Pages
- `site-dev/` is gitignored — only built files are uploaded, never committed
- Access policy can be updated in Cloudflare Zero Trust without redeploying the site
