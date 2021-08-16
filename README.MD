# Practera Docs

[![Build and Deploy](https://github.com/intersective/docs/actions/workflows/build-deploy.yml/badge.svg)](https://github.com/intersective/docs/actions/workflows/build-deploy.yml)

See the [Documentation](https://intersective.github.io/docs/)

We use [VuePress](https://vuepress.vuejs.org/) to build this documentation.

## Install

* run `npm install` to install the packages
* run `npm run dev` to start a server on local

## Create new doc

### Create a new doc under an existing section

* under the section's folder (e.g. `/src/development/`), create a new MarkDown file with the name starting by a number and `.` (e.g. `10.new-doc.md`). The files will be ordered by the starting number in the sidebar.

### Create a new section with documentations

1. create a new folder under `/src/` (e.g. `/src/new-section/`)
1. go to `/src/.vuepress/config.js`, add the newly added section to `themeConfig.sidebar`
1. inside `/src/.vuepress/config.js`, add a link to the `themeConfig.nav` so that this section appears on the top menu
