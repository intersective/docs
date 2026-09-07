<!-- status: living -->

# API Reference

The Practera GraphQL API is the primary backend for all frontend applications. Authoritative specs live in the practera-graphql-api repository.

[View specs on GitHub](https://github.com/intersective/practera-graphql-api/tree/main/specs/)

## Infrastructure

| Spec | Description |
|------|-------------|
| [handler.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/handler.md) | Lambda entry point, JWT auth (RS256, JWKS), query complexity (≤1000) and depth (≤12) limits, per-request DataLoaders, security headers |
| [builder.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/builder.md) | Pothos schema builder, Context type, root extension points |
| [jwks.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/jwks.md) | JWKS endpoint, key identifier for JWT signing |

## Query Groups (23 query specs)

| Group | File | Key Operations |
|-------|------|---------------|
| Experiences | queries/experience.md | Experience listing and detail |
| Assessments | queries/assessment.md | Submission and review queries |
| Enrolments | queries/enrolment.md | Enrolment status |
| Feedback | queries/feedback.md | Feedback and analytics |
| Metrics | queries/metric.md | Metric configuration and values |
| Reports | queries/reports.md | Cohort reports, report cards |
| Teams | queries/team.md | Team listing and members |
| Chat | queries/chat.md | Channel and chat log queries |
| Events | queries/event.md | Bookable event queries |
| AI | queries/ai.md | AI expert and config queries |
| Automation | queries/automation.md | Automation rule queries |
| Institution | queries/institution.md | adminInstitutions, systemStats, report export |
| Auth | queries/auth.md | Experience-scoped re-authentication |

## Mutation Groups (19 mutation specs)

| Group | File | Key Operations |
|-------|------|---------------|
| Assessment | mutations/assessment.md | saveSubmissionAnswer, submitAssessment, assignReviewer, handleReview, AI scoring |
| Experience | mutations/experience.md | Experience CRUD, go-live, import/export |
| Content | mutations/content.md | Milestone/activity/task/topic CRUD |
| Enrolment | mutations/enrolment.md | Enrol/unenrol, status updates |
| Chat | mutations/chat.md | Channel CRUD, chat logs, read receipts |
| Teams | mutations/team.md | Team CRUD, member management |
| Metrics | mutations/metric.md | Metric configuration and calculation |
| Achievement | mutations/achievement.md | Achievement management |
| Auth | mutations/auth.md | Token exchange, magic link creation |
| Institution | mutations/institution.md | Institution CRUD, branding, roles |

## Object Types (27 object specs)

Core domain types: experience, activity, task, topic, assessment, pulse-check, user, enrolment, team, channel, meeting, event, metric, report, ai-expert, achievement, badge-definition, automation-rule, feedback, todo-item, institution, taxonomy, template, timeline, auth, shared, response.

[Browse object specs](https://github.com/intersective/practera-graphql-api/tree/main/specs/objects/)

## Integration Tests

14 database-backed integration test suites cover: achievements, admin users, branding, content CRUD, import, media files, progress, pulse checks, settings, assessment submission, and team todos.

[Browse integration specs](https://github.com/intersective/practera-graphql-api/tree/main/specs/integration/)
