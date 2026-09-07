# Navigation

The Practera Admin Platform is organised around a persistent **shell** — a top bar and left sidebar that stay visible as you move between pages. Once you learn this layout, you can reach any tool in one or two clicks.

![Screenshot](../../assets/placeholder.png)

---

## Layout overview

```
┌─────────────────────────────────────────────────────────────┐
│  TOP BAR — institution, experience, team, user menu         │
├──────────┬──────────────────────────────────────────────────┤
│          │                                                  │
│ SIDEBAR  │  MAIN CONTENT                                    │
│          │  (Dashboard, Feedback, Designer, etc.)             │
│ Deliver  │                                                  │
│ Setup    │                                                  │
│ Expert   │                                                  │
│          │                                                  │
└──────────┴──────────────────────────────────────────────────┘
```

The **top bar** shows where you are (institution and experience). The **sidebar** lists the tools available for your current context. The **main content area** displays the page you have selected.

---

## Top bar

The top bar runs across the full width of the screen.

| Element | Location | Purpose |
|---------|----------|---------|
| **Practera logo** | Far left | Click to jump to the **Dashboard** |
| **Institution badge** | Left of centre | Shows your institution name; click to open the **Institution Menu** |
| **Experience name + status** | Centre | Shows the active experience (when one is selected) and its status badge |
| **Team button** | Right of centre | Quick access to team management for the current experience |
| **User menu** | Far right | Your name, role, Refresh, and Log Out |

!!! tip "Logo shortcut"
    Clicking the **Practera logo** always takes you to the Dashboard for your current experience. It is the fastest way to return to your program overview.

---

## Left sidebar

The sidebar lists admin tools grouped into three sections. It can be **collapsed** to an icon-only strip — click the collapse control at the bottom of the sidebar to toggle.

### Deliver

Day-to-day program management for the selected experience.

| Item | Description |
|------|-------------|
| **Dashboard** | Program overview — enrolment, activity health, quick stats |
| **Feedback** | Submission queues, review pipeline, and feedback tools |
| **Reports** | Built-in and custom reports, skills growth, export options |

### Setup

Configuration and authoring for the selected experience.

| Item | Description |
|------|-------------|
| **Design** | Experience designer — milestones, activities, assessments |
| **Calendar** | Events, due dates, and scheduling |
| **Users** | Enrolments, roles, and participant management |
| **Settings** | Experience-level settings and notifications |

### Expert

Advanced and adaptive learning tools.

| Item | Description |
|------|-------------|
| **Triggers** | Adaptive unlock rules and manual trigger awards |
| **AI Experts** | Configure AI agents embedded in your experience |

!!! note "Sidebar items depend on context"
    Most sidebar items require an **experience to be selected**. If no experience is active, the sidebar may show fewer options until you switch into one from the Experiences page.

---

## Institution menu

Click the **institution badge** in the top bar to open the Institution Menu. These pages operate at institution scope — not tied to a single experience.

| Item | Available to | Description |
|------|--------------|-------------|
| **Overview** | All admins | Institution dashboard and summary |
| **Experiences** | All admins | Browse and switch between experiences |
| **Audit Logs** | Institution admins | Record of admin actions across the institution |
| **Settings** | Institution admins | Branding, defaults, institution configuration |
| **AI Experts** | Institution admins | Institution-wide AI expert configuration |
| **CS Manager** | CS admins only | Cross-institution customer success tools |
| **Super Badges** | CS admins only | Platform-level badge management |
| **Billing** | CS admins only | Subscription and billing information |

!!! warning "CS admin items"
    CS Manager, Super Badges, and Billing are visible only to Practera customer success staff. Coordinators and institution administrators will not see these entries.

---

## User menu

Click your **name** in the top-right corner to open the User Menu.

| Item | Description |
|------|-------------|
| **Your name and role** | Confirms which account and permission level is active |
| **Refresh** | Reloads your session and permissions without logging out |
| **Log Out** | Ends your session and returns you to the Login App |

Use **Refresh** after an administrator changes your role — you will see new menu items without needing to sign in again.

---

## Experience context

Most Deliver and Setup tools apply to **one experience at a time**. The top bar always shows which experience is active:

- **Experience name** — the program you are managing
- **Status badge** — Draft, Live, or Archived

### Switching experience context

| Action | How |
|--------|-----|
| **Switch to another experience** | Institution Menu → **Experiences** → click a card |
| **Clear experience context** | Click the **institution name** in the top bar to return to institution-wide view |

See [Switching experiences](switching-experiences.md) for a full walkthrough.

---

## Legacy screens

Some pages still load inside the new shell as **legacy screens** — the familiar Practera interface you may have used before v2.6. Navigation works the same way: the sidebar and top bar remain visible, and the legacy page appears in the main content area.

!!! tip "Same features, new wrapper"
    Legacy screens behave exactly as they did before. If a button or workflow looks different, it is usually only the surrounding navigation that has changed — not the underlying tool.

---

## Quick reference

| I want to… | Go to… |
|------------|--------|
| See program stats | Deliver → **Dashboard** (or click the logo) |
| Review submissions | Deliver → **Feedback** |
| Edit milestones or assessments | Setup → **Design** |
| Enrol learners | Setup → **Users** |
| Switch programs | Institution Menu → **Experiences** |
| Change institution branding | Institution Menu → **Settings** |
| Sign out | User Menu → **Log Out** |

---

## What's next?

- [Switching experiences](switching-experiences.md) — select and manage experience context
- [Getting Started overview](index.md) — return to the section index
