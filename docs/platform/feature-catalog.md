# Practera Platform Feature Catalog

**Audience:** Product, Engineering, Sales  
**Purpose:** Authoritative inventory of what the platform does today, organized by the experiential learning lifecycle.  
**Last updated:** August 2026

> **Note:** This document reflects verified capabilities across the Practera codebase. Features are attributed to their implementing repository. Aspirational or roadmap features are documented separately in the [Strategic Roadmap](strategic-roadmap.md).

---

## Lifecycle Map

```
┌─────────────┐   ┌─────────────────────┐   ┌──────────────┐   ┌───────────┐
│   DESIGN    │──▶│ INDUSTRY ENGAGEMENT │──▶│   DELIVERY   │──▶│ REPORTING │
│             │   │                     │   │              │   │           │
│ Author the  │   │ Source real-world   │   │ Run the      │   │ Measure   │
│ experience  │   │ industry projects   │   │ program      │   │ outcomes  │
└─────────────┘   └─────────────────────┘   └──────────────┘   └───────────┘
```

---

## 1. Design

Everything an author or coordinator needs to build and configure an experiential learning program.

### 1.1 Experience Structure

Practera programs are organized as a nested hierarchy:

```
Experience
└── Project
    └── Milestone (phase of learning)
        └── Activity (a unit of work)
            └── Task (a content item within the activity)
```

Each level is independently configurable for visibility, sequencing, and assessment.

**Supported operations** (`practera-graphql-api`, `practera-admin`):

| Operation | Description |
|-----------|-------------|
| `createExperience` | Create a new experience with type, name, description |
| `createMilestone` / `updateMilestone` / `deleteMilestone` | Full milestone lifecycle |
| `createActivity` / `updateActivity` / `deleteActivity` | Activity management with `skill`/`learnflow` types |
| `addTaskToActivity` / `createAndAddTask` / `removeTaskFromActivity` | Task management within activities |
| Reorder milestones, activities, tasks | Drag-and-drop ordering |
| Move tasks between activities | Cross-activity task repositioning |
| Move activities between milestones | Cross-milestone activity repositioning |

### 1.2 Task Types

| Task Type | Key Capabilities | Implementation |
|-----------|----------------|----------------|
| **Topic** (story/content) | Rich HTML, video links, file attachments, H5P interactive simulations, read-progress tracking | `practera-graphql-api` (`createTopic`, `updateTopic`) |
| **Assessment** | Scored submissions with reviewer assignment, resubmission loops, AI feedback | `practera-graphql-api` |
| **Event** | Session scheduling with capacity limits, Zoom/video conference links, check-in assessments, booking management | `practera-graphql-api` |
| **Todo Group** | Team task lists with claim, takeover, complete, and praise actions; analytics dashboard | `practera-graphql-api` |

### 1.3 Assessment Types

Three assessment archetypes serve different feedback models:

| Type | Model | Auto-scored |
|------|-------|-------------|
| **Moderated** | Expert, peer, mentor, admin, self, or AI reviewer provides scored feedback per question | No |
| **Team 360** | Aggregated peer review across the full team; generates a PDF report | No |
| **Quiz** | Auto-graded with correct/incorrect scoring | Yes |

**Assessment configuration options:**
- Due dates with reminder notifications
- Team vs individual scope (`isTeam`)
- Resubmission allowed flag
- Auto-assign reviewer on submission
- Reviewer pool: specific users, role type, or AI Expert
- `reviewer_roles` JSONB — assign multiple role types as the reviewer pool
- `target_roles` JSONB — restrict visibility to specific role types
- Text-to-speech on assessment prompts (`textToSpeech` setting)
- Pulse-check widget attached to assessment

### 1.4 Question Types

Seven question types are available within any assessment:

| Type | Description |
|------|-------------|
| `text` | Open-ended written response |
| `oneof` | Single-choice from a list of options |
| `multiple` | Multi-select from a list of options |
| `slider` | Numeric scale response (configurable min/max/step) |
| `file` | File upload answer (TUS resumable, S3-backed) |
| `team_member_selector` | Select one team member |
| `multi_team_member_selector` | Select multiple team members |

Questions are organized into named groups within an assessment. Groups, questions, and choices can all be reordered.

### 1.5 Adaptive Learning Pathways

Practera supports programmatic control of the learner's progression path through trigger-based gates:

- **Lock/hide triggers** — applied to milestones, activities, or individual tasks
- **Trigger conditions** — can be tied to achievement award, milestone completion, or manual coordinator override
- **Lock vs hide** — locked content is visible but inaccessible; hidden content is not shown until the trigger fires
- **Achievement gates** — earning a badge or superbadge can unlock the next phase

**GraphQL operations:** `setTrigger`, `clearTrigger`, `achievementSearch`

### 1.6 AI Expert System

A configurable AI agent framework that embeds AI into the learning experience. Each AI Expert is version-controlled and institution-scoped.

**Expert modes:**

| Mode | Role in the Experience |
|------|----------------------|
| `mentor` | Provides guidance and coaching to learners |
| `observer` | Passively monitors activity without intervening |
| `reviewer` | Acts as an automated reviewer for assessment submissions |
| `facilitator` | Facilitates group discussions and activities |

**Key capabilities:**

- Create, update, clone, and delete AI Experts (`createAiExpert`, `updateAiExpert`, `cloneAiExpert`, `deleteAiExpert`)
- Version snapshots — create a named version at any point; restore to any prior version (`createAiExpertVersion`, `restoreAiExpertVersion`)
- Knowledge files — upload reference documents attached to the expert; backed by an OpenAI vector store (`vectorstoreId`) for semantic retrieval (`uploadAiExpertFile`, `deleteAiExpertFile`)
- Web search — configurable `webSearch` flag enables the expert to search the web during conversations
- Model selection — specific model alias configurable per expert (e.g. `gpt-5`, `claude-4`); temperature, verbosity, and reasoning mode configurable
- Provider-agnostic — supports OpenAI, Anthropic, and AWS Bedrock via the AI service
- Moderation settings — JSON-configurable content moderation per expert
- Shareable expert library (`aiExpertLibrary`) — reuse experts across experiences; publish to global library
- Institution AI configuration — manage provider API keys through the platform (`institutionAiConfig`, `updateInstitutionAiConfig`)

**Implementation:** `practera-graphql-api` (GraphQL), `practera-services/ai` (async workers), `practera-admin` (Cutie UI)

### 1.7 Template Library

Authors can save, share, and reuse complete experience designs:

- **Export** a live experience as a reusable template (`exportExperience`)
- **Import** from a template UUID to create a new experience (`importExperience`, `importExperienceData`)
- **Import JSON** — raw Practera JSON format import (`importExperienceJson`)
- **Duplicate** an existing experience with role selection (`duplicateExperienceUrl`)
- **Public vs private** templates — institution-scoped or shared across the platform
- **Template metadata** — searchable by category, type, duration, and tags
- **DynamoDB-backed catalog** — served via `practera-services/templates` HTTP Lambda
- **Cutie template browser** — search, preview, resource downloads, custom template chips

**Implementation:** `practera-graphql-api`, `practera-services/templates`, `practera-admin` (Cutie)

### 1.8 Experience Settings

A comprehensive settings surface for each experience:

| Setting Category | Options |
|----------------|---------|
| Identity | Name, description, type (internship, workSimulation, mentoring, accelerator) |
| Branding | Colors, logo, background image, email signature, custom email template |
| Scheduling | Timezone, engagement period, due date matrix |
| Language | Locale configuration |
| Access | Open registration (self-enrol), data retention exemption |
| Integrations | Notification matrix JSON (per event, per channel), Project Hub link, guide URLs |
| Features | Pulse-check indicator widget, chat enable/disable, review rating, TTS |
| Support | Support contact list per experience |

**Implementation:** `practera-graphql-api` (`updateExperienceSettings`), `practera-admin`

### 1.9 Custom Roles (RBAC)

Beyond the system roles (participant, mentor, coordinator, admin, inst_admin), institutions can define custom roles:

- Scoped to the institution (not per-experience)
- `base_type` — anchors to a system role for fallback permissions
- `permissions` JSONB array — granular capability list
- Roles with `base_type = 'admin'` pass all experience-scoped permission checks (but not `roles.manage`)
- Used at runtime via `requirePermission(context, 'permission.name')` — no inline role string checks

**GraphQL:** `institutionRoles`, `createInstitutionRole`, `updateInstitutionRole`, `deleteInstitutionRole`

### 1.10 Custom Taxonomy

Each institution or experience can override the terminology displayed in the UI:

- Rename "Milestone" to "Phase", "Mentor" to "Advisor", etc.
- Applied per-experience, inherited from institution default
- **GraphQL:** `taxonomy`, `updateTaxonomy`
- **App:** `TaxonomyService` applies labels throughout the learner UI

### 1.11 Experience Lifecycle Management

Experiences move through a defined status lifecycle managed by coordinators and admins:

```
Draft → Live → Completed → Archived
```

- Status transitions gate learner access
- Preview magic link lets authors see the learner view before going live (`previewMagicLink`)
- Student emulator — coordinator can view any learner's exact progress state
- Autosave on the designer prevents data loss

**Implementation:** `practera-admin` (PHP designer), `practera-graphql-api`

---

## 2. Industry Engagement

Tools for sourcing real-world projects from industry partners and connecting them to learner experiences.

### 2.1 Project Hub Overview

The Project Hub (`practera-project-hub`) is a standalone Next.js application for managing industry-sourced projects. It runs independently and links to Practera experiences via API.

**Stakeholders served:**

| Role | Capabilities |
|------|-------------|
| Admin/Coordinator | Manage campaigns, create/edit briefs, link to experiences, assign teams |
| Client (Industry Partner) | Review and approve briefs via unauthenticated token link |
| Learner | Browse available projects, submit priority-ranked applications |

### 2.2 Campaign Management

Campaigns are time-boxed intake cycles:

- Create campaigns with a share slug for public intake forms
- Campaign-specific intake workflows
- Open intake option (no campaign required)
- Brief sessions — AI-assisted conversational brief authoring intake
- Campaign dashboard showing brief status breakdown

### 2.3 Project Brief Lifecycle

Briefs follow a controlled approval workflow:

```
DRAFT → CLIENT_APPROVED → ADMIN_APPROVED → ARCHIVED
```

| Status | Who acts | What happens |
|--------|---------|--------------|
| `DRAFT` | Admin creates | Brief is being configured; not visible to learners |
| `CLIENT_APPROVED` | Client reviews and approves | Client has confirmed brief content |
| `ADMIN_APPROVED` | Admin promotes | Brief is ready for learner assignment |
| `ARCHIVED` | Admin archives | Brief retired from active use; restorable |

**Additional brief operations:**
- Star/favourite briefs for quick access
- Brief autosave (debounced)
- Restore archived briefs
- Duplicate briefs across campaigns

### 2.4 Client Collaboration

Industry partners can review and edit briefs without creating a Practera account:

- Time-limited, hashed edit tokens (SHA-256 stored; plaintext never persisted)
- Email invite with edit link (`project-brief-edit-link` template)
- Email approval request flow (`project-brief-approval-request` template)
- Clients can approve or request changes from within the brief editor
- Token revocation via `revokedAt` timestamp

### 2.5 AI Brief Generation

The campaign intake flow supports an AI-assisted multi-step brief authoring process:

- `BriefSession` model stores the workflow state for each intake session
- Multi-step workflow: Org Info → Company Research → Options Generated → Brief Complete
- Sessions are stored and resumable — industry partners can return to an incomplete session
- The structured workflow guides industry partners through defining their project brief

**Implementation:** `practera-project-hub` (`BriefSession` model, campaign session API routes)

### 2.6 Brief Content Model

Each project brief can contain:

| Field | Description |
|-------|-------------|
| Title, description | Core project information |
| Sector (industry) | Industry/sector classification (e.g., Technology, Healthcare) |
| Project Theme (project_type) | Type of work (e.g., Research, Development, Consulting) |
| Focus area | Specific focus domain |
| Organisation type | Type of organisation offering the project |
| Duration | Expected engagement duration |
| Deliverables | Expected outputs from the learner team |
| Skills required | Skill tags for matching and search |
| Logo image | Organisation logo (1:1 aspect ratio, TUS upload) |
| Background image | Hero image (16:9 or 21:9, TUS upload) |

### 2.7 Brief Catalog and Search

- A catalog of 660+ curated project briefs (`practera-mcp-server/src/data/project_briefs.json`)
- Searchable by skill, industry, deliverable, and duration
- Used as inspiration during brief creation and by AI matching tools
- `mcp_practera_search_project_briefs` MCP tool provides agent-accessible search

### 2.8 Learner Applications

- Learners submit priority-ranked preferences for available project briefs
- Unique constraints: one application per learner-brief pair, one application per priority level
- Applications linked to both a `LearnerProfile` and an `Experience`
- Admin can auto-group applicants into teams based on application priorities

### 2.9 Experience Linking

Once a brief is approved, it is assigned to one or more Practera experiences:

- `ProjectBriefExperience` — bridge record linking brief to experience
- `application_closed` flag — controls whether new learner applications are accepted
- Team-level project text (`team.projectBrief`) — brief content surfaced to the learner team

### 2.10 File Uploads for Briefs

Supported via TUS resumable upload protocol (`practera-tusd`):

- Client-side image cropping before upload enforces aspect ratios
- Logo validation: square (1:1) with ±10px tolerance
- Background validation: landscape 16:9 (±10% ratio) or 21:9 (±10% ratio)
- Old files cleaned up via authenticated TUS DELETE on replacement
- File metadata (dimensions, S3 bucket, path, CDN URL) stored as JSONB

---

## 3. Delivery

Everything that happens when a program is live — learner experience, team management, communication, assessment, and feedback.

### 3.1 Learner Application (App V2)

The learner-facing application is built with Angular 21 + Ionic 8, designed for mobile-first use.

**Key screens:**

| Screen | Capabilities |
|--------|-------------|
| Experience picker | Select from multiple enrolled programs; cross-stack switching |
| Home dashboard | Milestone/activity progress overview, achievement display, pulse-check widget, project brief modal, bookmarking |
| Activity view | Task list within an activity, completion status, due date |
| Topic reader | Rich HTML content, video, file attachments, H5P simulations, read-progress tracking |
| Assessment UI | Question-by-question submission, file upload answers, save draft, submit, resubmit |
| Review queue | Assigned reviews, accept/reject, per-question feedback entry, publish |
| Messages (chat) | Real-time team/DM/cohort channels, file attachments |
| Events | Browse sessions, book/cancel, detail view |
| Due dates | Chronological overview of upcoming deadlines |
| Notifications | In-app notification centre |
| Achievements | Badges, superbadges, certifications, certificate download |
| Settings | Profile, avatar upload, stack/region switch, LTI return URL |

**Implementation:** `practera-app` (Angular/Ionic), `practera-graphql-api` (API)

### 3.2 Activity and Topic Progression

- `startActivity` / `stopActivity` — tracks when a learner engages with an activity
- `startActivities` — bulk-start by experience scope
- `updateProgress` — marks topic content as viewed or completed
- H5P simulation support — interactive educational simulations embedded in topics
- Bookmarking — learner can bookmark activities for quick return
- Activity search and filter on the home screen
- Lock/unlock visual indicators driven by trigger state

### 3.3 Assessment Submission Workflow

```
Author drafts → Auto-assign / Manual assign → Learner submits
→ Reviewer assigned → Reviewer publishes → Learner rates → Resubmit (optional)
```

**Learner actions:**
- `saveSubmissionAnswer` — save individual question answers without submitting
- `submitAssessment` — finalize and submit for review
- `resubmitAssessment` — reopen a reviewed submission for revision (if enabled)
- File upload answers via TUS metadata (S3-backed)

**Reviewer actions:**
- `assignReviewer` — manual or automatic assignment
- `handleReview` — accept or decline the review assignment
- `saveReviewAnswer` — save per-question feedback and score (without publishing)
- `submitReview` — publish feedback to the learner

**Learner feedback on review:**
- `submitReviewRating` — 1–5 helpfulness score plus tag selection

### 3.4 Review Assignment Options

| Assignment Type | How it works |
|----------------|-------------|
| Expert / mentor | Specific user assigned as reviewer |
| Peer | Auto-assigned from same cohort |
| Admin | Coordinator reviews directly |
| Self | Learner reviews own submission |
| AI Expert | Configured AI Expert agent performs the review |
| Auto-assign on submit | Reviewer immediately assigned on submission |
| `reviewer_roles` pool | Assessment-level configuration specifying which roles can review |

### 3.5 Team 360 Reports

- Peer feedback across the full team on designated Team 360 assessments
- Aggregated via Lambda function — generates a PDF report per learner showing peer ratings
- Reports published by coordinator (`how-to-publish-team-360-reports`)
- Email notification: `team360-report`

**GraphQL:** `team360Report`

### 3.6 AI Feedback in Assessments

- AI Expert in `reviewer` mode acts as an automated reviewer
- Async processing via `practera-services/ai` (`assessment-feedback` action)
- Provider-agnostic: OpenAI, Anthropic, or Bedrock (selected per institution AI config)
- Translation action: `translate` (additional planned actions: `evaluate`, `tts`, `moderate`)
- Legacy PHP `ApiAiFeedbackComponent` also available for existing experiences

### 3.7 Events and Sessions

Events are structured learning sessions within an activity:

| Feature | Detail |
|---------|--------|
| Event types | `activity_session`, `other` |
| Capacity | Maximum bookings configurable |
| Video conference | Zoom/video conference link field |
| Check-in assessment | Attach an assessment to verify attendance |
| Single-booking | Prevent learners from booking multiple sessions for the same activity |
| Booking | `bookEvent` / `cancelEvent` mutations |
| Reminders | Email and SMS reminders before the session |
| Calendar | Due dates view shows event schedule |

**Email templates:** `event-invite`, `event-update`, `event-delete`, `event-reminder`, `book-session`, `session-reminder`, `event-withdraw`

### 3.8 Team Formation and Management

Teams are first-class objects in Practera:

| Operation | Detail |
|-----------|--------|
| Create / edit / delete teams | `createTeam`, `editTeam`, `deleteTeam` |
| Move teams | `moveTeam` — move team between timelines |
| Member management | `addTeamMember`, `removeTeamMember` |
| Team-scoped assessments | `isTeam` flag — assessment submitted by the whole team |
| Team member selector questions | Select team members as part of a response |
| Team progress | `teamProgress` — paginated progress table per team |
| My team peers | `peers` — list same-timeline participants for peer selection |

**Email templates:** `team-joined`, `team-joined-v3`, `team-left`, `team-changed`, `team-issue-flagged`, `collab-view`

### 3.9 Todo Groups (Team Task Lists)

A structured team task management system within experiences:

- Coordinators create todo groups with named task items (`createTodoGroup`, `createTodoTaskItem`)
- Learners can claim tasks (`actOnTodoItem` — `claim`), takeover, complete, and praise team members
- Coordinator can nudge learners on incomplete tasks
- Todo group analytics dashboard for coordinators
- `isTeam` flag on todo metadata for team-scoped tasks
- Scheduled message templates for todo reminders

### 3.10 Real-Time Chat

Chat channels are available to all learners, coordinators, and experts:

| Channel Type | Scope |
|-------------|-------|
| `Team` | Team members only |
| `Enrolment` (DM) | Direct message between two users |
| `Timeline` | Cohort-wide broadcast channel |

**Features:**
- `createChatLog`, `editChatLog`, `deleteChatLog`, `readChatLogs`
- File attachments within messages (`fileObj`)
- Announcement channels (read-only for participants)
- Role-restricted channels
- Unread counts via ChatAPI proxy
- Scheduled messages (Cutie admin interface)
- Real-time delivery via Pusher/Soketi (private channel per user/experience)

### 3.11 Notifications and Communications

Practera runs a comprehensive 54+ email template notification system, plus SMS and real-time push:

**Email service** (`practera-services/email`, SES in production):

| Category | Templates |
|----------|-----------|
| Auth | verification-code, registration, forgot-password, magic-login, account-verification, email-change-verification, compromised-password |
| Enrolment | new-enrolment, invite-registered, enrolment-reminder, bulk-enrolment-started, bulk-enrolment-completed |
| Assessments | assessment-submitted, assessment-reminder (3 variants), feedback-received |
| Reviews | review-assigned, review-unassigned, review-auto-assign-failed, review-received, review-completed-by-other, review-published, review-reminder, review-resubmitted, review-resubmitting, review-rating-report |
| Events | event-invite, event-update, event-delete, event-reminder, book-session, session-reminder, event-withdraw |
| Teams | team-joined, team-joined-v3, team-left, team-changed, team-issue-flagged, team360-report, collab-view |
| Achievements | achievement-awarded |
| Chat | unread-chat |
| Todo | todo-assigned |
| Coordinator | advisor-digest, report-published |
| Project briefs | project-brief-edit-link, project-brief-approval-request |
| Admin | admin-share, admin-support-request, admin-new-customer, admin-custom-branding, admin-contact |

**SMS service** (`practera-services/sms`, Twilio):

- verification-code, unread-chat, assessment-reminder, event-reminder, generic

**Real-time** (`practera-services/comms`, Pusher/Soketi):

- Private channel per user/experience
- Event bus for cross-service notifications
- Cron-driven: assessment reminders, review rating notifications, advisor digest, unread chat reminders

### 3.12 Pulse Checks

A lightweight engagement check-in mechanism:

| Type | Description |
|------|-------------|
| `skills` | Learner self-rates progress on a defined skill set |
| `on_track` | Learner indicates overall program on-track status |

- Configurable indicator widget displayed on the home dashboard
- Coordinator view shows traffic-light status per learner
- `pulseCheck`, `pulseCheckStatus`, `pulseCheckSkills`, `submitPulseCheck`

### 3.13 LTI 1.3 Integration

Full LTI 1.3 Advantage implementation (`practera-login-api`):

| Feature | Detail |
|---------|--------|
| Supported LMS | Canvas, Moodle, Blackboard, Brightspace, and any LTI 1.3 compliant LMS |
| OIDC launch | Standard LTI 1.3 OIDC login initiation |
| Deep linking | Select specific activities from within the LMS |
| Dynamic registration | Automated platform registration (LTI ADR) |
| AGS (grade passback) | Submit grades back to the LMS gradebook |
| NRPS (roster sync) | Sync course members from LMS to Practera |
| MFA gate | Admin users with passkeys must complete passkey verification during LTI launch |
| Institution management | `institutionLtiRegistrations`, `registerLtiPlatform`, `deleteLtiRegistration` via GraphQL |

### 3.14 Authentication Methods

| Method | Implementation |
|--------|--------------|
| Magic link (email code) | Time-limited code sent via email; verified at `/code/verify` → JWT |
| Passkey (WebAuthn) | Biometric or hardware key via browser WebAuthn API |
| Password | Traditional email/password with forgot/reset flow |
| JWT / API key | Header `apikey`; direct JWT login; global_login for stack switch |
| Direct auth token | `auth(authToken)` — one-time link for magic-link handoffs |
| LTI launch | Login-api → `exchangeToken` → Practera JWT |
| Open registration | Learner self-registers via experience share link |
| Stack switching | Login-api `/stacks` → `/stack/switch` → magic link for regional stack redirect |
| MFA | Passkey registration required for admin LTI access |
| Client edit token | Project Hub — hashed short-lived token for unauthenticated brief editing |

Email hashing uses Argon2id (`practera-login-api`).

### 3.15 File Uploads

All file uploads use the TUS resumable upload protocol (`practera-tusd`), backed by AWS S3:

- Assessment file-type answers
- Chat message attachments
- Topic content attachments
- AI Expert knowledge files
- Profile avatars
- Project Hub logo and background images
- Institution media library (`mediaFilesConnection`) — searchable, paginated

**File operations:** `createFileStore`, `deleteFileStore`, `renameFileStore`, `updateFile`, `fileUsage`

### 3.16 Achievements, Badges, and Certificates

| Type | Description |
|------|-------------|
| `badge` | Awarded for completing an activity or trigger condition |
| `superbadge` | Meta-badge awarded for earning a defined set of badges |
| `certification` | Formal credential with PDF certificate |

**Features:**
- Open Badges compatible — `rebadgeOpenBadge` re-issues with a different email
- Skills tagging — badge linked to specific skill areas
- Points system — learners accumulate points for achievements
- Certificate PDF generation via Lambda function — stored in S3, served via presigned URL
- Learner UI: `/v3/badges-certificates` page

**GraphQL:** `achievements`, `badges`, `achievementsConnection`, `userAchievement`, `certificateUrl`

### 3.17 Enrolment and Onboarding

| Feature | Detail |
|---------|--------|
| Invite enrolment | `enrolUser` — invite by email with role assignment |
| Bulk enrolment | CSV upload; `bulk-enrolment-started` / `bulk-enrolment-completed` email notifications |
| Open registration | `openRegistration` setting — learner self-registers |
| Status management | `updateEnrolmentStatus` — drop removes team memberships |
| Unenrolment | `unenrollUser` |
| Dev provisioning | `provisionDevAccount`, `devLogin` (local/stage only) |
| Ops worker | `handleEnrolment` SQS handler for async enrolment side effects |

---

## 4. Reporting

Tools for measuring program effectiveness, learner outcomes, and operational health.

### 4.1 Experience Statistics

Real-time statistics available at the experience level:

| Metric Set | Contents |
|-----------|---------|
| `expStatistics` | Overview metrics, funnel metrics, feedback cycle metrics |
| `dashboardStatistics` | Submission charts, feedback loops, helpfulness ratings (Cutie dashboard) |
| `cutieStatistics` | Coordinator-facing stats: submissions per activity, feedback loop completion rates, review helpfulness scores |
| `skillsGrowth` | Skills bar graph — before/after self-rating comparison |
| `expsStatistics` | Cross-experience overview (institution admin) |

### 4.2 Custom Metrics

A configurable metric builder for institutionsit to define their own KPIs:

**Data sources available:**

| Source | What it measures |
|--------|----------------|
| `question` | Response to a specific assessment question |
| `assessment` | Completion and score aggregates for an assessment |
| `user` | User-level attributes (enrolment, activity) |
| `pulse_check` | Pulse check response aggregates |

**Aggregation functions:** `average`, `sum`, `count`, `net_promoter`

**Operations:** `createMetric`, `updateMetric`, `configureMetric`, `useMetric`, `unlinkMetric`, `calculateMetrics`

**Library:** `metrics(publicOnly)` — public metrics reusable across experiences; `metric(uuid)` for specific metric detail

**Institution rollup:** `institutionMetricSummary`, `experienceMetrics` — aggregate metrics across all experiences in the institution

### 4.3 Custom Reports

A report builder for creating visual data presentations:

- Reports are JSON-section based — compose multiple visualization blocks
- Section types: bar chart, pie chart, data table, summary card, color configuration
- Institution-scoped or experience-scoped reports
- Report preview within Cutie

**GraphQL:** `reports`, `report(uuid)`, `createReport`, `editReport`, `deleteReport`

**Implementation:** `practera-admin` (Cutie reports module), `practera-graphql-api`

### 4.4 Coordinator Dashboard (Cutie)

The coordinator-facing dashboard (`practera-admin`, Cutie module) provides:

| Panel | Contents |
|-------|---------|
| Metrics pane | Key statistics for the experience |
| Submission chart | Visual breakdown of submission activity over time |
| ELSA todo list | AI-surfaced coordinator action items |
| Todo health | Status of team todo groups (completion rates, blockers) |
| Progress table | Per-user and per-team assessment completion matrix |
| Feedback status matrix | Which learner/assessment combinations have outstanding reviews |
| Cohort overview | Cross-experience stat cards (standalone `overview-only` route) |

### 4.5 Skills Growth Report

A before/after skill self-assessment visualization:

- Learners complete a pulse check at the start and end of a program
- `skillsGrowth` query returns bar chart data showing change in self-rated skill level
- Available in both the learner app and coordinator admin view

**Help article:** `docs/help-articles/practera-metrics/skills-growth-report.md`

### 4.6 Engagement Statistics

- Statistics Lambda (`practera-services/statistics`) computes: experience-level engagement, dashboard engagement, engagement status
- Invoked from GraphQL via Lambda data source
- Feeds engagement status indicators used by coordinators

### 4.7 Reviewer Feedback Status

- `reviewerFeedbackStatus` — matrix of which assessments have outstanding reviews per reviewer
- Coordinator can action individual review assignments from this view
- Included in the Cutie coordinator module

### 4.8 Todo Group Analytics

- `todoGroupAnalytics` — coordinator view of team task completion, claim rates, and blockers
- Surfaced in the Cutie dashboard

### 4.9 Institution Administration and Audit

**Institution management:**

| Feature | Detail |
|---------|--------|
| Institution listing | `adminInstitutions`, `adminInstitution` |
| Experience listing | `institutionExperiences` |
| Admin users | `institutionAdmins`, `addInstitutionAdmin`, `removeInstitutionAdmin` |
| User management | `adminUsers`, `adminUser` (cross-institution search for sysadmin) |
| Enrolment admin | `adminEnrolments` (DataTables-compatible), `enrolmentProgress` |

**Data deletion and privacy:**

- `triggerDataDeletion` — phased deletion by role (reset → timeline → user)
- `institutionDeletionAudits` — audit trail of deletion events
- `checkDeletionRecord` — verify a user was deleted via email SHA-256 hash lookup
- `deletionExempt` — per-experience opt-out from data retention lifecycle
- `data-retention` service (`practera-services`) — SQS-driven phased deletion

**Audit logging:**

- `auditLog` batch handler in `practera-services/ops`
- Cross-service audit trail stored in the database
- Audit log UI in Cutie (`Audit Log of Admin Activity`)

### 4.10 Enrolment Progress Reporting

- `enrolmentProgress` — per-enrolment progress data for admin reporting
- `teamProgress` — team-level progress table with pagination
- Legacy `EnrolmentProgress` PHP controller for DataTables-compatible reporting

---

## Repository Reference

| Repo | Feature areas implemented |
|------|--------------------------|
| `practera-graphql-api` | All GraphQL API operations: authoring, learner flows, review, AI, metrics, LTI, admin |
| `practera-app` | Learner UX: home, activities, topics, assessments, reviews, chat, events, achievements, settings |
| `practera-admin` (Cutie) | Coordinator dashboard, progress, metrics, reports, template library, chat, AI Experts |
| `practera-admin` (PHP) | Legacy experience designer, API endpoints, exports, webhooks, enrolment admin |
| `practera-project-hub` | Industry campaign management, project briefs, client collaboration, learner applications |
| `practera-services` | Email (54+ templates), SMS, real-time comms, AI feedback/chat, certificates, statistics, templates, ops workers |
| `practera-login-api` | Authentication: magic link, passkey, LTI 1.3 full suite, stack switching, branding |
| `practera-login-app` | Login UI: email login, passkey, stack switcher, LTI deep link, admin dashboard |
| `practera-tusd` | TUS-protocol resumable file uploads to S3 |
| `practera-mcp-server` | AI agent tooling for authoring/learner/reviewer flows; project brief catalog |

---

*This document reflects the verified codebase as of August 2026. For future capabilities and strategic direction, see the [Strategic Roadmap](strategic-roadmap.md).*
