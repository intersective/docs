# Enrolments

Enrolments manage which users have access to an experience and what role they play. Every user who participates in an experience — whether as a learner, reviewer, or coordinator — must be enrolled.

Navigate to **Users** in the left sidebar (or go to `/enrolments`) while an experience is selected.

![Screenshot](../../assets/placeholder.png)

---

## Enrolment table

The enrolment table shows all users currently enrolled in the experience.

| Column | Description |
|--------|-------------|
| **Name / Email** | User's display name and email |
| **Role** | Learner, Reviewer, Coordinator, or Admin |
| **Status** | Active, Pending (invitation sent, not yet accepted), or Removed |
| **Team** | The team the user is assigned to (if teams are enabled) |
| **Joined** | Date they accepted the enrolment |

### Filtering and search

- **Search**: type a name or email in the search box to filter the list in real time.
- **Role filter**: click the role dropdown to show only Learners, only Reviewers, etc.
- **Status filter**: show All, Active, Pending, or Removed users.

---

## Adding users

### Add a single user

1. Click **+ Add User**.
2. Enter the user's email address.
3. Select their role (Learner, Reviewer, Coordinator).
4. Click **Add**.

If the user already has a Practera account, they are enrolled immediately. If they are new, they receive an invitation email with a magic link.

### Bulk invite

1. Click **Invite**.
2. Paste email addresses — one per line, or comma-separated.
3. Select the role for all invitees.
4. Click **Send Invitations**.

Each invitee receives an email with a personalised magic link. Invitations expire after 7 days. You can resend from the Pending filter view.

### CSV import

For large cohorts, use the CSV import:

1. Click **Import**.
2. Download the **CSV template**.
3. Fill in the columns: `first_name`, `last_name`, `email`, `role`.
4. Upload the completed file.
5. Review the import preview — Practera shows a count of new users, existing users to update, and any rows with errors.
6. Click **Confirm Import**.

!!! tip "CSV tips"
    - Role values must be exactly: `learner`, `reviewer`, or `coordinator` (lowercase).
    - Duplicate emails are skipped with a warning — no duplicates are created.
    - A progress toast shows import status for large files.

---

## Managing enrolled users

### Change a user's role

Click the **role badge** on any row. A dropdown appears — select the new role. The change takes effect immediately.

### Remove a user

Click the **trash icon** on a user's row. A confirmation dialog appears. Confirm to remove them.

!!! note "Data retention after removal"
    Removing a user removes their access but does **not** delete their data. Their submissions and reviews are retained. If you re-add the same user, they regain access to their previous work.

### Resend invitation

In the **Pending** filter view, click the **resend icon** on any pending user to send a new invitation email.

---

## Report cards

Each enrolled learner has a **Report Card** — a structured view of their progress through the experience.

1. Find the learner in the enrolments table.
2. Click the **report card icon** on their row (or navigate to `/enrolments/:uuid/report-card`).
3. The report card shows: overall progress, milestone completion tree, assessment status per task, and reviewer feedback summaries.

---

## Related

- [Teams](teams.md) — organise learners into teams
- [Feedback pipeline](../deliver/feedback.md) — review submitted assessments
- [Bulk Enrolment via CSV Upload](../../help-articles/essentials/bulk-enrolment-via-csv-upload.md) (Help Center)
