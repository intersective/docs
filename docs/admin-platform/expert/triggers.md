# Triggers & Badges

Triggers and Badges are the automation and gamification tools in the Expert section. Use them to build adaptive learning pathways, automate notifications, and celebrate learner achievement.

Navigate to **Expert → Automation** (route `/automation`). The page has two tabs: **Triggers** and **Badges**.

![Screenshot](../../assets/placeholder.png)

---

## Triggers

A trigger is a rule: **when [event] happens, do [action]**.

### Common trigger patterns

| Pattern | Event | Action |
|---------|-------|--------|
| **Sequential unlock** | Learner completes Activity A | Unlock Activity B |
| **Completion reward** | Learner completes all tasks in a milestone | Award a badge |
| **At-risk alert** | Assessment due date passes without submission | Send notification to coordinator |
| **Conditional branch** | Learner receives a score above X | Unlock advanced activity |
| **Timed reveal** | Specific date/time arrives | Unhide a milestone |

### Creating a trigger

1. Go to **Expert → Automation → Triggers tab**.
2. Click **+ New Trigger**.
3. Fill in the trigger details:
   - **Name** — a short descriptive name for the trigger (internal only).
   - **Event** — the condition that fires the trigger (see events below).
   - **Condition** — optional filter (e.g. "only if score > 70%").
   - **Action** — what happens when the trigger fires (see actions below).
4. Click **Save**.

### Trigger events

| Event | When it fires |
|-------|--------------|
| **Task completed** | Learner marks a task as complete |
| **Assessment submitted** | Learner submits an assessment |
| **Assessment reviewed** | A review is submitted for a learner's submission |
| **Badge awarded** | A specific badge is earned |
| **Enrolment created** | A user is enrolled in the experience |
| **Scheduled date** | A specific calendar date/time arrives |
| **Score threshold** | A review score crosses a threshold |

### Trigger actions

| Action | What it does |
|--------|-------------|
| **Unlock milestone/activity/task** | Makes a locked item accessible |
| **Hide milestone/activity/task** | Hides an item from the learner |
| **Award badge** | Gives a specific badge to the learner |
| **Send notification** | Sends an email or in-app notification to the learner, reviewer, or coordinator |
| **Enrol in experience** | Automatically enrols the user in a different experience |

### Manually awarding a trigger

To fire a trigger for a specific learner without waiting for the event:

1. Find the learner in **Users → Enrolments**.
2. Click their name to open their profile.
3. In the **Triggers** section, click **Award** next to the relevant trigger.

---

## Badges

Badges are digital achievement tokens awarded to learners for meeting milestones or demonstrating excellence. They appear on the learner's profile page.

### Creating a badge

1. Go to **Expert → Automation → Badges tab**.
2. Click **+ New Badge**.
3. Fill in the badge details:
   - **Name** — what learners will see.
   - **Description** — why this badge is earned.
   - **Image** — upload a badge image (square PNG recommended, 200×200px).
   - **Criteria** — the conditions for earning it (displayed to learners).
4. Click **Save**.

The badge is now available to use as a trigger action or as a manual award.

### Manually awarding a badge

1. Find the learner in **Users → Enrolments**.
2. Click their name to open their profile.
3. In the **Badges** section, click **Award Badge** → select the badge → confirm.

### Badge visibility

By default, badges are visible to the learner and to coordinators. If you want to hide a badge from learners until it is awarded, toggle the **Hidden until earned** option when creating the badge.

!!! note "Legacy interface"
    Triggers and Badges are currently served through the legacy CakePHP interface within the new admin shell. The UI appearance may differ slightly from other screens. A fully redesigned Triggers & Badges experience is planned for v2.7.

---

## Related

- [Designer](../setup/designer.md) — set up lock/hide controls that triggers can activate
- [Whats the Difference Between Locking and Hiding](../../help-articles/creating-adaptive-learning-pathways/whats-the-difference-between-locking-and-hiding.md) (Help Center)
- [Creating and Configuring Triggers](../../help-articles/creating-adaptive-learning-pathways/creating-and-configuring-triggers.md) (Help Center)
- [Creating Badges for Your Experience](../../help-articles/creating-adaptive-learning-pathways/creating-badges-for-your-experience.md) (Help Center)
