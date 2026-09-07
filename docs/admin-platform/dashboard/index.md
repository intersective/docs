# Dashboard

The **Dashboard** is the first screen you see after logging in and selecting an experience. It gives you a real-time snapshot of how your program is performing — enrolment health, learner engagement, and the full feedback pipeline — so you can spot issues early and take action without digging through multiple reports.

![Screenshot](../../assets/placeholder.png)

---

## Selecting an experience

All dashboard metrics apply to the **currently selected experience**. Use the **experience picker** in the top bar — a dropdown next to the experience name — to switch between programs at your institution.

!!! note "No experience selected?"
    If you land on the Dashboard without an experience selected, open the **Institution menu** (click your institution badge in the top bar) and choose **Experiences**. Click the card for the program you want to manage, then return to **Dashboard** in the sidebar.

When you switch experiences, every metric on the page refreshes automatically to reflect the new program.

---

## Overview metrics

The top row of the Dashboard shows four headline numbers for your experience:

| Metric | What it tells you |
|--------|-------------------|
| **Learners enrolled** | Total active participants currently enrolled in the experience |
| **Pending enrolments** | People who have been invited or registered but are not yet fully enrolled |
| **On-track learners** | Learners who have completed scheduled activities on time (see below) |
| **Engaged learners** | Learners who have logged in and interacted with the experience recently |

These figures update in near real time as learners progress, submit work, and receive feedback.

### Understanding "on-track"

**On-track** measures whether learners are keeping pace with the program schedule. A learner is counted as on-track when they have completed the activities that were due by today according to your experience calendar and milestone structure.

!!! tip "On-track is a schedule metric, not a quality metric"
    A learner can be on-track while submitting low-quality work, and a high-performing learner may appear off-track if they are working ahead of due dates in an unusual way. Use on-track alongside the feedback funnel to get the full picture.

If on-track numbers drop suddenly, check **Setup → Schedule** to confirm due dates are configured correctly, and review **Deliver → Progress** to see which learners are falling behind.

---

## Feedback funnel

Below the overview metrics, the **feedback funnel** visualises the assessment and review pipeline from submission through to acknowledgement. Use it to identify bottlenecks at a glance.

| Stage | Description |
|-------|-------------|
| **Submitted vs Unsubmitted** | How many required assessments have been submitted compared to those still outstanding |
| **Awaiting Review** | Submissions that have been received but not yet reviewed by a mentor, expert, or coordinator |
| **Overdue reviews** | Reviews that have passed their due date without being completed |
| **Feedback given** | Submissions where a reviewer has published feedback |
| **Awaiting Acknowledgement** | Learners who have received feedback but have not yet acknowledged it |
| **Quality %** | The proportion of submissions meeting your configured quality threshold |
| **Mean time** | Average time from submission to published feedback |

A healthy funnel shows steady movement from left to right. Stages that grow without clearing indicate where you need to focus coordinator effort.

---

## Feedback Cycles table

The **Feedback Cycles** table breaks submission and review activity down **by milestone**. Each row shows:

- Milestone name
- Number of submissions received
- Number of reviews completed
- Outstanding items at each stage

This per-milestone view helps you see whether a specific phase of the program — for example, the mid-program reflection or the final capstone — is causing delays, rather than treating the experience as a single block.

!!! note "Milestone names come from your experience design"
    If a milestone is missing from the table, it may not contain any assessments, or learners may not have reached that phase yet.

---

## ELSA tab

Switch to the **ELSA** tab at the top of the Dashboard to access AI-powered insights for your experience. ELSA (Experiential Learning Support Assistant) analyses patterns in learner activity, submission quality, and engagement, then surfaces **action recommendations** tailored to your program.

Typical ELSA insights include:

- Learners or teams at risk of disengaging
- Milestones where submission rates are unusually low
- Suggested coordinator actions (for example, sending a reminder or checking team assignments)

ELSA complements the numeric metrics — use it when you want context and suggested next steps rather than raw counts.

---

## Taking action from the Dashboard

The Dashboard is most useful when you treat it as a **decision screen**, not just a report. Here are practical responses to common signals:

| If you see… | Consider… |
|-------------|-----------|
| High **pending enrolments** | Go to **Setup → Users** or **Deliver → Enrolments** to approve or troubleshoot registrations |
| Low **on-track** percentage | Open **Deliver → Progress** to identify behind-schedule learners; send comms or adjust due dates |
| High **overdue reviews** | Go to **Deliver → Feedback → Assignments** to reassign reviews or nudge reviewers |
| Large **awaiting acknowledgement** count | Send a reminder via **Deliver → Comms**, or check whether feedback was published correctly |
| Low **quality %** on a milestone | Review assessment instructions in **Setup → Designer**; consider a coordinator check-in |

!!! tip "Make the Dashboard part of your weekly routine"
    Many coordinators open the Dashboard at the start of each week, note the two or three metrics that need attention, and work through the linked Deliver tools. Five minutes here can prevent hours of catch-up later.

---

## Related guides

- [Switching experiences](../getting-started/switching-experiences.md) — change the active program from the top bar
- [The Experience Dashboard Explained](../../help-articles/elsa-ai-based-experiential-learning-support-assistant/the-experience-dashboard-explained.md) — deeper dive into ELSA insights
- [Managing Your Feedback Loops](../../help-articles/designing-feedback-loops/managing-your-feedback-loops.md) — configure and monitor assessment workflows

---

*Last updated: August 2026*
