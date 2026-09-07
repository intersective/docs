# Progress & Metrics

The Progress screen gives coordinators a data-driven view of how the cohort is developing over the life of the experience. It combines a **Skills Growth chart** for longitudinal skill tracking and configurable **Metric tiles** for monitoring key performance indicators.

Navigate to **Progress** in the left sidebar (route `/progress`), or click the Progress icon in the Deliver section.

![Screenshot](../../assets/placeholder.png)

---

## Skills Growth chart

The Skills Growth chart is a line chart showing how skill confidence or proficiency develops across the cohort over time.

### Reading the chart

- **X-axis**: time (weeks or milestones, depending on experience length)
- **Y-axis**: skill confidence score (0–100%)
- **Lines**: each line represents a skill tracked in the experience

### Filtering the chart

- **Skill selector**: use the dropdown to focus on a specific skill, or show all skills.
- **Date range**: narrow the view to a specific period.
- **Cohort vs individual**: toggle between cohort average and individual learner trends.

!!! tip
    Declining skill scores after a milestone usually indicate the assessment was challenging — a good opportunity to schedule a coaching session or send targeted resources.

---

## Metric tiles

Metric tiles are configurable KPI cards. Each tile displays a single number with a label and optional trend indicator.

### Default metrics

When you first open the Progress screen, a set of default metrics is shown:

| Metric | Description |
|--------|-------------|
| **Learners enrolled** | Total enrolled in the experience |
| **Completion rate** | % of learners who have completed all required tasks |
| **Engagement score** | Composite score based on login frequency, task completion, and submission activity |
| **Avg feedback quality** | Average reviewer quality rating across the experience |
| **Submissions rate** | % of assessments submitted by their due date |

### Creating a custom metric

1. Click **+ Add Metric**.
2. Select a **metric type** from the library (completion, engagement, assessment scores, team health, etc.).
3. Give the tile a **label**.
4. Choose the **display format** (number, percentage, or trend arrow).
5. Click **Save**.

The new tile appears in the metric grid. Drag to reorder tiles.

### Editing or deleting a tile

Click the **edit icon** (pencil) on any tile to modify its settings. Click the **delete icon** to remove it.

---

## Exporting data

Click the **Export** button (top right) to download the underlying metric data:

- **CSV** — raw data table, compatible with Excel and Google Sheets.
- **XLSX** — formatted spreadsheet with column headers.

The export includes all metrics visible on the screen at the time of export, plus the learner breakdown if the individual view is active.

---

## Related

- [Dashboard](../dashboard/index.md) — real-time experience statistics
- [Reports](reports.md) — build charts from this data into learner-facing reports
- [Skills Growth Report](../../help-articles/practera-metrics/skills-growth-report.md) (Help Center)
- [Creating New Metrics](../../help-articles/practera-metrics/creating-new-metrics.md) (Help Center)
