<!-- status: living -->

# Experience Delivery

Experience Delivery covers the runtime of a programme — the learner journey and all the tools coordinators use to manage, support, and track participants. It spans two front-end systems: practera-app (learner-facing) and practera-admin-app (coordinator-facing).

> **Known gap:** practera-app has zero SpecGuard Living Specs. All learner-facing capabilities listed below are implemented but undocumented at the spec level. Bootstrapping is in progress — see [Alignment Status](../alignment/index.md).

#### Learner App (practera-app — Angular 19 + Ionic)

| Page | Description |
|------|-------------|
| **Home** | Dashboard with experience list and notifications |
| **Milestones / Activities** | Programme tree navigation; milestone progress, activity list |
| **Topic** | Rich content viewer (HTML, embedded media) |
| **Assessment** | Submission form (multiple question types including file upload, slider rating); submit guard; pagination; answer persistence |
| **Review** | Peer/expert review form; read-only preview for submitted reviews |
| **Chat** | Channel list, chat room (paginated messages, rich compose, edit), channel info, DMs and announcements |
| **Events** | Event list and detail; booking with capacity enforcement |
| **Pulse Check** | Wellbeing survey submission |
| **Badges/Certificates** | Earned achievements and certificate download |
| **Due Dates** | Timeline of upcoming and overdue tasks |
| **Settings** | Account settings |
| **Notifications** | In-app notification centre |
| **Meeting Poll** | Meeting time poll participation |
| **Contribution Rating** | Peer contribution rating for Team 360 |
| **Check-in** | QR-based event attendance check-in |

Source: `practera-app/projects/v3/src/app/pages/`

Specs: **None yet** — [see Alignment Status](../alignment/index.md)

#### Coordinator Tools (practera-admin-app — React/Vite)

| Capability | Description |
|------------|-------------|
| **Feedback Pipeline** | Submission table (server-side filter/sort/paginate), submission drawer (4-step pipeline: Submitted → Assigned → Reviewed → Acknowledged), reviewer assignment, AI quality scoring, feedback status matrix, Team 360 management |
| **Enrolment Management** | Enrolment table (role/progress filters), bulk CSV import wizard, invitation/reminder emails, per-learner report cards (milestone tree, assessment status) |
| **Team Management** | Team board (split-panel list + member detail), auto-assign by size, team heat maps, workload balance |
| **Communications** | Chat admin (channel management, scheduled messages), email, notification management |
| **Progress / Dashboard** | Experience picker, ELSA todos, feedback funnel, skills growth metrics |

Specs: [Admin App — Deliver specs](https://github.com/intersective/practera-admin-app/tree/main/specs/deliver/)
