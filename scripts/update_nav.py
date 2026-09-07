import os
import re
import yaml

MKDOCS_YML = "mkdocs.yml"
RELEASES_DIR = os.path.join("docs", "releases")

# Match v2.4.5.md, v2.4.5.1.md, v2.4.5-Metrics-MVP.md, v2.4.5.1-Hotfix.md, etc.
RELEASE_PATTERN = re.compile(r"^v([0-9]+(\.[0-9]+)+)(.*)\.md$")


def get_release_files():
    files = []
    for fname in os.listdir(RELEASES_DIR):
        if "_technical_summary" in fname:
            continue  # Ignore temporary technical summary files
        match = RELEASE_PATTERN.match(fname)
        if match:
            version = match.group(1)
            suffix = match.group(3).replace('-', ' ').strip()
            nav_key = f"v{version}{' ' + suffix if suffix else ''}"
            files.append((tuple(map(int, version.split('.'))), nav_key, fname))
    # Sort by version tuple descending
    files.sort(key=lambda v: v[0], reverse=True)
    return [(nav_key, fname) for _, nav_key, fname in files]


def update_mkdocs_nav():
    with open(MKDOCS_YML, "r") as f:
        # Use yaml.load instead of yaml.safe_load to handle Python-specific tags
        mkdocs = yaml.load(f, Loader=yaml.Loader)

    nav = mkdocs.get("nav", [])
    # Find the Releases section
    releases_idx = None
    for i, entry in enumerate(nav):
        if isinstance(entry, dict) and "Releases" in entry:
            releases_idx = i
            break
    if releases_idx is None:
        raise ValueError("No 'Releases' section found in mkdocs.yml nav")

    releases_nav = nav[releases_idx]["Releases"]
    # Always keep releases/index.md at the top
    new_releases_nav = ["releases/index.md"]
    for nav_key, fname in get_release_files():
        new_releases_nav.append({nav_key: f"releases/{fname}"})

    # Only update if changed
    if releases_nav != new_releases_nav:
        nav[releases_idx]["Releases"] = new_releases_nav
        mkdocs["nav"] = nav
        with open(MKDOCS_YML, "w") as f:
            yaml.dump(mkdocs, f, sort_keys=False, width=120, default_flow_style=False)
        print(f"Updated navigation in {MKDOCS_YML} with {len(new_releases_nav)-1} releases.")
    else:
        print("Navigation already up to date.")


def main():
    update_mkdocs_nav()

if __name__ == "__main__":
    main() 