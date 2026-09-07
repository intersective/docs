#!/bin/bash
set -e
shopt -s nullglob

# Usage: ./release_pipeline.sh <release string>
# Example: ./release_pipeline.sh "Release 2.4.5" or "Hotfix 2.4.5.1"
# In GitHub Actions, set RELEASE_STRING env var instead of CLI arg

# Determine release string
if [ -n "$GITHUB_ACTIONS" ]; then
  # Running in GitHub Actions
  if [ -z "$RELEASE_STRING" ]; then
    echo "Error: RELEASE_STRING env var not set in GitHub Actions."
    exit 1
  fi
  RELEASE_STR="$RELEASE_STRING"
else
  # Running locally
  if [ -z "$1" ]; then
    echo "Usage: $0 <release string>"
    echo "Example: $0 'Release 2.4.5' or $0 'Hotfix 2.4.5.1'"
    exit 1
  fi
  RELEASE_STR="$1"
fi

# After setting RELEASE_STR, trim whitespace
RELEASE_STR="$(echo "$RELEASE_STR" | xargs)"

# Extract version for file naming using regex (supports 2.4.5, 2.4.5.1, 2.4, etc.)
VERSION=$(echo "$RELEASE_STR" | grep -oE '[0-9]+(\.[0-9]+)+' | head -1)
if [ -z "$VERSION" ]; then
  echo -e "${RED}Warning: Could not extract version number from release string '$RELEASE_STR'. File naming and downstream steps may fail."
fi
RELEASE_TAG="$RELEASE_STR"

# Handle custom release date with strict validation
if [ -n "$RELEASE_DATE" ]; then
  # Trim whitespace from custom date
  RELEASE_DATE="$(echo "$RELEASE_DATE" | xargs)"
  
  # Validate date format (YYYY-MM-DD)
  if [[ ! "$RELEASE_DATE" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
    echo -e "${RED}Error: Invalid date format '$RELEASE_DATE'. Must be YYYY-MM-DD (e.g., 2025-09-10)${NC}"
    echo -e "${RED}Examples: 2025-09-10, 2025-12-01, 2024-08-15${NC}"
    exit 1
  fi
  
  # Validate that date is not in the future
  CURRENT_DATE=$(date +%Y-%m-%d)
  if [[ "$RELEASE_DATE" > "$CURRENT_DATE" ]]; then
    echo -e "${RED}Error: Release date '$RELEASE_DATE' cannot be in the future. Current date is '$CURRENT_DATE'${NC}"
    exit 1
  fi
  
  # Validate that date is a real date (not like 2025-02-30)
  if ! date -d "$RELEASE_DATE" >/dev/null 2>&1; then
    echo -e "${RED}Error: Invalid date '$RELEASE_DATE'. Please check the date is valid (e.g., not Feb 30th)${NC}"
    exit 1
  fi
  
  echo -e "${GREEN}✓ Using custom release date: $RELEASE_DATE${NC}"
else
  # Use current date as fallback
  RELEASE_DATE=$(date +%Y-%m-%d)
  echo -e "${YELLOW}ℹ Using current date as release date: $RELEASE_DATE${NC}"
fi

echo "Using release string: $RELEASE_TAG"
echo "Extracted version: $VERSION"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to check if a command exists
check_command() {
    if ! command -v "$1" &> /dev/null; then
        echo -e "${RED}Error: $1 is not installed${NC}"
        exit 1
    fi
}

# Function to check if a file exists
check_file() {
    if [ ! -f "$1" ]; then
        echo -e "${RED}Error: $1 not found${NC}"
        exit 1
    fi
}

# Function to check environment variables
check_env() {
    local required_vars=("JIRA_API_TOKEN" "OPENAI_API_KEY")
    local missing_vars=()
    for var in "${required_vars[@]}"; do
        if [ -z "${!var}" ]; then
            missing_vars+=("$var")
        fi
    done
    if [ ${#missing_vars[@]} -ne 0 ]; then
        echo -e "${RED}Error: Missing required environment variables:${NC}"
        printf '%s\n' "${missing_vars[@]}"
        exit 1
    fi
}

# Function to run a step with error handling
run_step() {
    local step_name="$1"
    local command="$2"
    echo -e "\n${YELLOW}Running: $step_name...${NC}"
    if eval "$command"; then
        echo -e "${GREEN}✓ $step_name completed successfully${NC}"
    else
        echo -e "${RED}✗ $step_name failed${NC}"
        exit 1
    fi
}

# Check prerequisites
echo -e "${YELLOW}Checking prerequisites...${NC}"
check_command python3
check_command pip
check_command mkdocs

# Check required files
check_file "scripts/fetch_jira.py"
check_file "scripts/summarize_llm.py"
check_file "scripts/update_nav.py"
check_file "templates/release-note-template.md"

# Check environment variables
check_env

# Create necessary directories
mkdir -p docs/releases

# Set environment variables for the scripts
export RELEASE_TAG="$RELEASE_TAG"
export RELEASE_VERSION="$VERSION"
export RELEASE_DATE="$RELEASE_DATE"
export RELEASE_NOTES_FILE="docs/releases/v$VERSION.md"

# Run the pipeline
echo -e "\n${YELLOW}Starting release notes pipeline for: $RELEASE_TAG...${NC}"

# Step 1: Fetch Jira issues
run_step "Fetching Jira issues" "python3 scripts/fetch_jira.py '$RELEASE_TAG'"

# Step 2: Generate release notes
# Use models from environment variables if set, otherwise use defaults.
# This allows GitHub Actions to control the models via its UI.
PROCESSOR_MODEL_ARG="--processor-model ${PROCESSOR_MODEL:-gpt-4o-mini}"
ORGANIZER_MODEL_ARG="--organizer-model ${ORGANIZER_MODEL:-gpt-4o-mini}"

run_step "Generating release notes" "python3 scripts/summarize_llm.py --version $VERSION --release-tag '$RELEASE_TAG' $PROCESSOR_MODEL_ARG $ORGANIZER_MODEL_ARG"

# Step 3: Update navigation
run_step "Updating navigation" "python3 scripts/update_nav.py --version $VERSION"

# Step 4: Serve the site (only if running locally)
if [ -z "$GITHUB_ACTIONS" ]; then
  echo -e "\n${YELLOW}Starting MkDocs server...${NC}"
  echo -e "${GREEN}✓ Release notes pipeline completed successfully${NC}"
  echo -e "${YELLOW}Press Ctrl+C to stop the server${NC}"
  # mkdocs serve &
fi

# Step 5: Cleanup temp/intermediate files
echo "\nCurrent directory: $(pwd)"
echo "Cleaning up all temp/intermediate release files..."
PATTERNS=(
  "docs/releases/v*_raw.yaml"
  "docs/releases/v*_technical_summary.md"
  "scripts/processing/to_llm_v*.md"
)
for pattern in "${PATTERNS[@]}"; do
  echo "Checking pattern: $pattern"
  for file in $pattern; do
    if [ -f "$file" ]; then
      echo "Deleting $file"
      rm -f "$file"
    fi
  done
done
echo "Cleanup complete."

wait
exit 0 