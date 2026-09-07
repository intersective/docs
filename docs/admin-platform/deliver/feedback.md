# Feedback Pipeline

The Feedback screen is the central hub for managing assessments during a live experience. It consolidates submission tracking, reviewer assignment, completion status, and Team 360 peer reviews into a single tabbed interface.

Navigate to **Feedback** in the left sidebar (route `/feedback`).

![Screenshot](../../assets/placeholder.png)

---

## Overview: three tabs

| Tab | What it shows |
|-----|--------------|
| **Pipeline** | All submissions — who submitted, which assessments, status, reviewers assigned |
| **Feedback Status** | A matrix showing reviewer × learner completion for each assessment |
| **Team 360** | Tools to publish peer review reports to learners |

---

## Pipeline tab

### Reading the submission table

The Pipeline tab shows every assessment submission across the experience. Key columns:

| Column | Description |
|--------|-------------|
| **Learner** | Who submitted |
| **Assessment** | Which assessment they submitted |
| **Milestone** | Which milestone it belongs to |
| **Submitted** | Submission date and time |
| **Reviewers** | Who is assigned to review it |
| **Status** | Pending / In Review / Reviewed / Acknowledged / Overdue |

### Pipeline summary

The summary row at the top of the table shows quick counts:

- **Pending** — submitted but not yet assigned a reviewer
- **Overdue** — review deadline has passed
- **Complete** — review given and acknowledged by learner

### Filtering

Use the filter bar to narrow by:

- **Status**: All / Pending / In Review / Reviewed / Overdue / Acknowledged
- **Milestone**: filter to a specific milestone
- **Assessment**: filter to a specific assessment task
- **Learner**: search by name

### Opening a submission

Click any row to open the **Submission Drawer** on the right. The drawer shows:

- Full submission content (text, file attachments)
- Assigned reviewer(s) with their review status
- Review content once submitted
- Submission metadata (date, attempt number)

### Assigning a reviewer

From the Submission Drawer:

1. Scroll to the **Reviewer Assignment** section.
2. Click **+ Assign Reviewer**.
3. Search for a reviewer by name — only enrolled users with the Reviewer or Coordinator role appear.
4. Select the reviewer and click **Assign**.

You can assign multiple reviewers to a single submission. To reassign, click the current reviewer's name and select a different user.

!!! tip "Bulk assignment"
    To assign all pending submissions in a milestone to a single reviewer, filter by milestone + status "Pending", then use the bulk-select checkbox and the **Assign** action in the toolbar.

---

## Feedback Status tab

The Feedback Status tab shows a completion matrix for each assessment in the experience.

- **Rows**: reviewers
- **Columns**: learners
- **Cell colour**: Green (reviewed + acknowledged), Amber (review given, awaiting acknowledgement), Red (overdue), Grey (not yet submitted)

Use this view to:

- Quickly spot which reviewers are behind
- Identify learners whose submissions have not been reviewed
- Send targeted reminders to specific reviewers

---

## Team 360 tab

Team 360 is a peer review mechanism where team members review each other's work. The Team 360 tab lets you **publish** the compiled peer review reports to learners.

### Publishing a Team 360 report

1. Select the **milestone** from the dropdown.
2. Select the **review cycle** (if there are multiple peer review assessments in the milestone).
3. Click **Preview** to see what learners will receive.
4. Click **Publish** to release the reports.

Once published, each learner can see an anonymised summary of how their teammates rated their work, and the comments given.

!!! warning "Publishing is final"
    Once a Team 360 report is published to learners, it cannot be unpublished. Make sure all reviews are complete before publishing.

---

## Related

- [Enrolments](../users/enrolments.md) — enrol reviewers into the experience
- [Teams](../users/teams.md) — set up teams for Team 360
- [Managing Your Feedback Loops](../../help-articles/designing-feedback-loops/managing-your-feedback-loops.md) (Help Center)
