#!/usr/bin/env sh

# abort on errors
set -e


mkdir practera-docs
git clone --branch gh-pages https://$GITHUB_TOKEN@github.com/intersective/docs.git practera-docs/.

git config credential.helper 'cache --timeout=90'
git config --global user.name 'githubaction'
git config --global user.email 'githubaction@practera.com'


cp -R src/.vuepress/dist/* practera-docs/

cd practera-docs && git add --all
DIFF=$(git diff --staged --name-only)
echo $DIFF
test -z "$DIFF" && echo "nothing to commit, working tree clean" || (git commit -m "github action deployment" && git push -q https://$GITHUB_TOKEN@github.com/intersective/docs.git gh-pages)