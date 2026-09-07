# Teams

Teams organise learners into groups for collaborative activities, peer review (Team 360), and group chat. The Teams screen gives you a drag-and-drop board to create, populate, and manage teams.

Navigate to **Teams** in the left sidebar (route `/teams`) while an experience is selected.

![Screenshot](../../assets/placeholder.png)

---

## The Teams board

The board has two types of columns:

- **Unassigned** (leftmost) — all enrolled learners who are not yet in a team.
- **Team columns** — one column per team, showing its members.

Each learner card shows the learner's name, email, and role badge.

---

## Creating teams

### Create a single team

1. Click **+ Create Team**.
2. Enter a **team name**.
3. Optionally set a **max size** (leave blank for unlimited).
4. Click **Create**.

A new column appears on the board.

### Auto-assign learners

For large cohorts, manual drag-and-drop is slow. Use auto-assign to populate teams automatically:

1. Click **Auto Assign**.
2. Choose an algorithm:
   - **Balanced** — distributes learners as evenly as possible across existing teams.
   - **Random** — randomly assigns learners to teams.
3. A preview shows the proposed allocation — review it before confirming.
4. Click **Confirm** to apply, or **Cancel** to discard.

!!! note
    Auto-assign only moves learners from **Unassigned**. It does not change learners who are already in a team.

---

## Assigning learners manually

Drag a learner card from the **Unassigned** column into any team column. The assignment saves immediately.

To move a learner between teams, drag their card from one team column to another.

To unassign a learner, drag their card back to the **Unassigned** column.

---

## Editing teams

### Rename a team

Click the team name at the top of the column. It becomes an editable text field. Type the new name and press **Enter** (or click outside the field).

### Delete a team

Click the **trash icon** at the top right of the team column. A confirmation dialog appears. All team members are moved back to **Unassigned** — no data is lost.

!!! warning
    Deleting a team removes the grouping but does not remove learners from the experience. They will appear in **Unassigned** and can be re-added to a new team.

---

## How teams are used

| Feature | How teams apply |
|---------|----------------|
| **Team 360** | Peer review cycles run within teams — learners review their teammates' work |
| **Group chat** | Team members share a default group chat channel |
| **Team Todo tasks** | Collaborative tasks are shared within the team |
| **Progress view** | The Progress screen can break down metrics by team |
| **Reports** | Reports can be filtered or grouped by team |

---

## Related

- [Enrolments](enrolments.md) — enrol users before assigning to teams
- [Team 360](../deliver/feedback.md) — publish peer review reports
- [Creating Teams](../../help-articles/essentials/creating-teams.md) (Help Center)
