# Practera Platform — Internal Reference

This section provides internal strategic documentation about the Practera platform. It is intended for product, engineering, and commercial teams — not end-user help.

---

## Contents

| Document | Purpose | Audience |
|----------|---------|----------|
| [Feature Catalog](feature-catalog.md) | Complete inventory of every experiential learning capability, organized by lifecycle stage | Product, Engineering, Sales |
| [Strategic Roadmap](strategic-roadmap.md) | Competitive landscape analysis, gap identification, moat builders, and innovation opportunities | Leadership, Product, Commercial |

---

## Platform at a Glance

Practera is an end-to-end experiential learning platform that covers the full program lifecycle:

```
Design → Industry Engagement → Delivery → Reporting
```

Unlike point solutions that address a single stage, Practera provides a unified environment for every stakeholder: program authors, industry partners, coordinators, learners, and reviewers.

**Core platform architecture:**

| Layer | Purpose |
|-------|---------|
| GraphQL API (`practera-graphql-api`) | Primary API surface — authoring, learner flows, admin, AI, metrics |
| Learner App (`practera-app`) | Angular/Ionic mobile-first learner experience |
| Coordinator UI (Cutie, `practera-admin`) | Embedded Angular dashboard for program coordinators |
| Legacy Admin (`practera-admin` PHP) | CakePHP experience designer, reports, API endpoints |
| Industry Project Hub (`practera-project-hub`) | Campaign management, project briefs, learner applications |
| Backend Services (`practera-services`) | Email, SMS, AI feedback, notifications, certificates, statistics, template library |
| Authentication (`practera-login-api/app`) | Magic link, passkey, LTI 1.3, stack switching, branding |
| File Service (`practera-tusd`) | TUS-protocol resumable file uploads to S3 |
| MCP Server (`practera-mcp-server`) | AI agent tooling and project brief catalog |

---

## Lifecycle Overview

### Design
Authors build experiences using a structured hierarchy (Milestones → Activities → Tasks), configure rich assessment and feedback loops, set adaptive unlock rules, and deploy AI Expert agents into the experience.

### Industry Engagement
Program coordinators source real-world projects from industry through campaign-based intake forms, manage a brief approval workflow with client collaboration, and link approved projects to learner experiences.

### Delivery
Learners progress through activities, submit assessments, receive expert or AI-generated feedback, collaborate in teams, participate in events, and communicate via real-time chat — all tracked against due dates and progression rules.

### Reporting
Coordinators and institution admins access live statistics, configurable custom metrics, visual reports, and cross-experience rollups to measure program effectiveness and demonstrate outcomes.

---

*Last updated: August 2026*
