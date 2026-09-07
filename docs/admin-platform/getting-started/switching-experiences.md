# Switching Experiences

An **experience** is a single experiential learning program — one cohort, one curriculum, one set of learners. Most admin work happens inside one experience at a time. This guide explains how to browse your institution's experiences, switch between them, and understand status badges in the top bar.

![Screenshot](../../assets/placeholder.png)

---

## Why experience context matters

The Admin Platform sidebar — Dashboard, Feedback, Design, Users, and so on — operates on the **currently selected experience**. If you review feedback while the wrong experience is active, you may see empty queues or data from a different program.

Always check the **experience name** in the top bar before taking action.

---

## Opening the Experiences list

There are two ways to reach the Experiences page:

1. Click the **institution badge** in the top bar → select **Experiences** from the Institution Menu
2. Navigate directly to `/experiences` in your browser (if you have the URL bookmarked)

The Experiences page shows every program your account can access at this institution, displayed as a grid of **experience cards**.

---

## Experience cards

Each card summarises one program:

| Element | Description |
|---------|-------------|
| **Experience name** | The program title — usually set by the author or coordinator |
| **Status badge** | Draft, Live, or Archived |
| **Learner count** | Number of enrolled learners in this experience |

Cards are sorted and filtered to help you find the right program quickly. Use search or filters if your institution runs many experiences simultaneously.

### Switching into an experience

**Click a card** to switch into that experience. The page navigates to the Dashboard (or your last visited page), and the top bar updates to show:

- The **experience name**
- Its **status badge** (Draft, Live, or Archived)

All sidebar items in Deliver and Setup now apply to this experience.

!!! tip "Confirm before you act"
    After switching, glance at the top bar to confirm the experience name matches what you intended. This small habit prevents accidental changes to the wrong program.

---

## Experience status badges

Every experience has a lifecycle status. The badge in the top bar and on each card tells you where the program stands.

### Draft

The experience is **not yet visible to learners**. Coordinators and authors can edit the designer, adjust settings, and test workflows.

When an experience is in Draft, you may see a **Go Live** control in the top bar — an amber button with a **Zap icon** labelled **Go Live**. Click it when you are ready to open the program to enrolled learners.

See [Going Live](../../help-articles/essentials/going-live.md) for the full checklist before publishing.

### Live

The experience is **active**. Enrolled learners can access activities, submit assessments, and participate in teams.

Live experiences show a **green "Live" pill** in the top bar. Editing is still possible, but changes may affect learners immediately — use preview and caution when modifying live content.

!!! warning "Changes to live experiences"
    Structural changes (deleting activities, changing due dates, modifying assessments) can impact learners who are mid-program. Communicate changes to your cohort when in doubt.

### Archived

The experience is **closed**. Learners can no longer submit new work. Archived programs remain accessible to administrators for reporting and record-keeping.

---

## Go Live button

When your selected experience is in **Draft** status, the top bar displays:

**⚡ Go Live** (amber button with Zap icon)

Clicking **Go Live** publishes the experience to enrolled learners. Before you click:

- Confirm enrolments are complete (or intentionally partial)
- Review due dates and calendar events
- Preview key activities from the learner's perspective
- Verify notification settings

After going live, the amber button is replaced by the green **Live** pill.

---

## Returning to institution view

Sometimes you need to step out of a single experience and work at institution level — for example, to browse all programs, check audit logs, or adjust institution settings.

**Click the institution name** in the top bar to clear experience context.

The top bar no longer shows an experience name. The sidebar may show fewer items until you select an experience again. Institution Menu pages (Overview, Experiences, Settings) remain fully available.

| Context | Top bar shows | Sidebar focus |
|---------|---------------|---------------|
| **Experience selected** | Institution + experience name + status | Deliver, Setup, Expert |
| **No experience selected** | Institution name only | Institution-level pages |

---

## Common workflows

### Starting your day as a coordinator

1. Log in to the Admin Platform
2. Open **Experiences** and click the program you are delivering today
3. Go to **Deliver → Dashboard** for a snapshot of overnight activity
4. Open **Feedback** to work through the review queue

### Managing multiple programs

Switch between experiences by returning to **Experiences** and clicking a different card. Your session remembers each experience independently — settings, enrolments, and content do not overlap between programs.

### Setting up a new program

1. Create or duplicate an experience (from the Experiences page or institution tools)
2. Switch into the new experience (status: **Draft**)
3. Use **Setup → Design** to build content
4. Use **Setup → Users** to enrol participants
5. Click **Go Live** when ready

---

## Troubleshooting

**I do not see an experience I expect**

- Your administrator may not have granted you access to that program
- The experience may belong to a different institution — check you are on the correct stack
- Archived experiences may be hidden by default filters

**The Go Live button is missing**

- The experience may already be Live or Archived
- You may not have coordinator or admin permissions for this experience

**Sidebar items are greyed out or missing**

- You may not have an experience selected — open Experiences and click a card
- Your role may not include permission for that tool — contact your administrator

---

## What's next?

- [Navigation](navigation.md) — full tour of the admin interface
- [Experience Status](../../help-articles/onboarding/experience-status.md) — deeper explanation of Draft, Live, and Archived
- [Going Live](../../help-articles/essentials/going-live.md) — checklist before publishing
