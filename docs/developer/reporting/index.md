<!-- status: living -->

# Reporting

The Reporting stage provides coordinators and institution admins with data-driven insights into programme performance, learner progress, and engagement. All reporting features are in practera-admin-app.

Specs: [Admin App — Report specs](https://github.com/intersective/practera-admin-app/tree/main/specs/report/)

### Metrics and KPIs

Configurable metric definitions: data source, aggregation type, filter (role, status), data type. Value history timeline. Answer distribution view. Metric status lifecycle (draft → active → archived).

[Spec: report/metrics/](https://github.com/intersective/practera-admin-app/tree/main/specs/report/metrics/)

### Skills Growth

Grouped bar chart visualising skill/pulse check scores across sequences. Per-role breakdown. Powered by pulse check submissions.

[Spec: report/metrics/components/skills-growth.md](https://github.com/intersective/practera-admin-app/tree/main/specs/report/metrics/components/skills-growth.md)

### Custom Report Builder

Section-based report editor. Five chart types: area chart, bar chart, pie chart, data table, KPI card. Shareable read-only preview. Feedback status report variant.

[Spec: report/reports/](https://github.com/intersective/practera-admin-app/tree/main/specs/report/reports/)

### Feedback Status Matrix

Reviewer × assessment completion accountability matrix. Shows which reviewers have completed/pending reviews per assessment.

[Spec: report/reports/feedback-status.md](https://github.com/intersective/practera-admin-app/tree/main/specs/report/reports/feedback-status.md)

### Team 360 Reports

Peer contribution rating aggregation. Legacy Team360 iframe embed for detailed breakdown.

### Cohort Reports and Exports

Aggregated learner progress at cohort level. CSV and XLSX export. Report card per learner (milestone tree, assessment status).

[GraphQL API: queries/reports.md](https://github.com/intersective/practera-graphql-api/tree/main/specs/queries/reports.md)

### Audit Log

Programme activity log viewer. Referenced in architecture index but spec file pending creation.
