# Reports

The Reports builder lets you create custom learner progress reports — rich documents combining charts, metrics, narrative text, and formatted data — that can be published to individual learners at the end of a milestone or experience.

Navigate to **Reports** in the left sidebar (route `/reports`).

![Screenshot](../../assets/placeholder.png)

---

## Reports list

The Reports screen shows all report templates for the current experience. Each report card shows the template name, last modified date, and a preview thumbnail.

- **Open a report for editing**: click its card.
- **Create a new report**: click **+ New Report**, enter a name, and the editor opens.
- **Duplicate**: click the options menu (⋮) on a card → Duplicate.
- **Delete**: click the options menu → Delete (with confirmation).

---

## Report Editor

The Report Editor uses a drag-and-drop canvas. The report is composed of **sections** arranged vertically. You can add, reorder, and delete sections.

### Section types

| Type | Use for |
|------|---------|
| **Heading** | Large titles and section breaks |
| **Text** | Narrative paragraphs, instructions, or context |
| **Chart** | Data visualisation (see chart types below) |
| **Table** | Tabular data (e.g. task completion per milestone) |
| **Metric Tile** | A single large KPI number with label |
| **Page Break** | Forces a new page when the report is printed or exported as PDF |

### Adding a section

1. Click **+ Add Section** between existing sections (or at the end of the report).
2. Select the section type from the panel.
3. The new section appears in place. Click it to open its configuration panel on the right.

### Configuring a section

Each section type has its own settings:

- **Heading / Text**: title and content fields with a rich text editor.
- **Chart**: select chart type, data source, and axis labels.
- **Table**: choose columns and data source.
- **Metric Tile**: select the metric, label, and colour.

### Reordering sections

Drag the handle (≡) on the left edge of any section to reorder it within the report.

### Deleting a section

Click the **trash icon** on the section to delete it (with a brief undo window).

---

## Chart types

Five chart types are available in the Chart section:

| Chart type | Best for |
|-----------|---------|
| **Bar** | Comparing values across categories (e.g. submission counts by milestone) |
| **Line** | Trends over time (e.g. engagement score over weeks) |
| **Area** | Cumulative trends (e.g. total submissions over time) |
| **Pie / Donut** | Proportions (e.g. on-track vs off-track learners) |
| **Grouped Bar** | Comparing multiple series across categories |

---

## Preview

Click **Preview** in the editor toolbar to see the report exactly as a learner will see it. The preview renders all sections with live data for the currently selected experience.

!!! tip
    Use Preview to catch layout issues before publishing. Long text blocks may benefit from a Page Break section to keep the report readable when printed.

---

## Publishing reports to learners

Reports are published **per learner** via the Report Card:

1. Go to **Users → Enrolments**.
2. Click the **report card icon** on a learner's row.
3. The Report Card page shows the learner's progress and any published reports.
4. Click **Publish Report** → select the report template → confirm.

The learner receives a notification and can view the report in the Practera App.

---

## Related

- [Enrolments](../users/enrolments.md) — find the learner's report card
- [Progress](progress.md) — metrics and skills growth data that feeds report charts
- [Skills & Progress Tab](../../help-articles/delivering-experiential-learning/skills-and-progress-tab.md) (Help Center)
