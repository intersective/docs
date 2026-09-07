<!-- status: living — updated 2026-09-07 -->

# Alignment Status

This page tracks spec coverage across Practera repos and flags known gaps between frontend and backend specifications.

> **Last updated:** 2026-09-07 — practera-app and practera-project-hub specs bootstrapped.

## Spec Coverage

| Repo | Specs | Format | Status |
|------|-------|--------|--------|
| practera-admin-app | 193 | SpecGuard Living Specs | ✅ Good coverage |
| practera-graphql-api | 270 | SpecGuard Living Specs | ✅ Good coverage |
| practera-login-app | 32 | SpecGuard Living Specs | ✅ Good coverage |
| practera-login-api | 59 | SpecGuard Living Specs | ✅ Good coverage |
| practera-project-hub | 10 + 9 | SpecGuard (new) + Speckit (legacy) | 🔄 SpecGuard bootstrapped; test alignment pending |
| practera-app | 17 | SpecGuard Living Specs (draft) | 🔄 Bootstrapped; needs `specguard align` and refinement |

## Capability Alignment Matrix

| Capability | Stage | Admin-App Spec | App Spec | Project-Hub Spec | API Spec | Status |
|------------|-------|---------------|----------|-----------------|----------|--------|
| Assessment submission | Delivery | [deliver/feedback/submissions-table.md](https://github.com/intersective/practera-admin-app/blob/main/specs/deliver/feedback/submissions-table.md) | [pages/assessment.md](https://github.com/intersective/practera-app/blob/main/specs/pages/assessment.md) | — | [mutations/assessment.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/mutations/assessment.md) | ⚠️ Needs spec-to-API cross-check |
| Assessment review | Delivery | [deliver/feedback/submission-drawer.md](https://github.com/intersective/practera-admin-app/blob/main/specs/deliver/feedback/submission-drawer.md) | [pages/review.md](https://github.com/intersective/practera-app/blob/main/specs/pages/review.md) | — | [resolvers/mutations/saveReviewAnswer.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/resolvers/mutations/saveReviewAnswer.md) | ⚠️ Needs spec-to-API cross-check |
| Chat / messaging | Delivery | [deliver/chat/](https://github.com/intersective/practera-admin-app/tree/main/specs/deliver/chat/) | [pages/chat.md](https://github.com/intersective/practera-app/blob/main/specs/pages/chat.md) | — | [mutations/chat.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/mutations/chat.md) | ⚠️ Needs spec-to-API cross-check |
| Milestone / activity tree | Delivery | — | [pages/activity.md](https://github.com/intersective/practera-app/blob/main/specs/pages/activity.md) | — | [objects/activity.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/objects/activity.md) | ⚠️ Needs spec-to-API cross-check |
| Topic content viewer | Delivery | — | [pages/topic.md](https://github.com/intersective/practera-app/blob/main/specs/pages/topic.md) | — | [objects/topic.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/objects/topic.md) | ⚠️ Needs spec-to-API cross-check |
| Pulse check | Delivery | — | [pages/pulse-check.md](https://github.com/intersective/practera-app/blob/main/specs/pages/pulse-check.md) | — | [objects/pulse-check.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/objects/pulse-check.md) | ⚠️ Needs spec-to-API cross-check |
| Badges / achievements | Delivery | — | [pages/badges-certificates.md](https://github.com/intersective/practera-app/blob/main/specs/pages/badges-certificates.md) | — | [objects/achievement.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/objects/achievement.md) | ⚠️ Needs spec-to-API cross-check |
| Event booking (learner) | Delivery | [design/schedule/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/schedule/) (admin) | [pages/events.md](https://github.com/intersective/practera-app/blob/main/specs/pages/events.md) | — | [objects/event.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/objects/event.md) | ⚠️ Needs spec-to-API cross-check |
| Home / milestone tree | Delivery | — | [pages/home.md](https://github.com/intersective/practera-app/blob/main/specs/pages/home.md) | — | [objects/experience.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/objects/experience.md) | ⚠️ Needs spec-to-API cross-check |
| QR check-in (learner) | Delivery | [design/schedule/components/attendance-tab.md](https://github.com/intersective/practera-admin-app/blob/main/specs/design/schedule/components/attendance-tab.md) (admin) | [pages/checkin.md](https://github.com/intersective/practera-app/blob/main/specs/pages/checkin.md) | — | [mutations/event.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/mutations/event.md) | ⚠️ Needs spec-to-API cross-check |
| Enrolment management | Delivery | [deliver/enrolments/](https://github.com/intersective/practera-admin-app/tree/main/specs/deliver/enrolments/) | — | — | [mutations/enrolment.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/mutations/enrolment.md) | ✅ Aligned (admin-side) |
| Programme design | Design | [design/design/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/design/) | — | — | [mutations/content.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/mutations/content.md) | ✅ Aligned |
| Scheduling (admin) | Design | [design/schedule/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/schedule/) | — | — | [objects/event.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/objects/event.md) | ✅ Aligned |
| Automation (ELSA) | Design | [design/automation/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/automation/) | — | — | [queries/automation.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/queries/automation.md) | ✅ Aligned |
| AI Experts | Design | [design/ai-experts/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/ai-experts/) | — | — | [objects/ai-expert.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/objects/ai-expert.md) | ✅ Aligned |
| Metrics / KPIs | Reporting | [report/metrics/](https://github.com/intersective/practera-admin-app/tree/main/specs/report/metrics/) | — | — | [queries/metric.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/queries/metric.md) | ✅ Aligned |
| Custom reports | Reporting | [report/reports/](https://github.com/intersective/practera-admin-app/tree/main/specs/report/reports/) | — | — | [queries/reports.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/queries/reports.md) | ✅ Aligned |
| Campaign management | Sourcing | — | — | [specs/pages/admin-campaigns.md](https://github.com/intersective/practera-project-hub/blob/main/specs/pages/admin-campaigns.md) | — (own DB) | ✅ Spec exists |
| Project brief intake | Sourcing | — | — | [specs/pages/intake.md](https://github.com/intersective/practera-project-hub/blob/main/specs/pages/intake.md) | — (own DB) | ✅ Spec exists |
| Learner project application | Sourcing | — | [pages/home.md (project brief modal)](https://github.com/intersective/practera-app/blob/main/specs/pages/home.md) | [specs/pages/learner-projects.md](https://github.com/intersective/practera-project-hub/blob/main/specs/pages/learner-projects.md) | — (own DB) | ⚠️ Cross-system: app→project-hub integration needs spec |
| Team management | Delivery | [deliver/teams/](https://github.com/intersective/practera-admin-app/tree/main/specs/deliver/teams/) | — | [specs/api/campaigns.md](https://github.com/intersective/practera-project-hub/blob/main/specs/api/campaigns.md) | [mutations/team.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/mutations/team.md) | ✅ Aligned |
| Contribution rating (Team 360) | Delivery | [deliver/feedback/team360-tab.md](https://github.com/intersective/practera-admin-app/blob/main/specs/deliver/feedback/team360-tab.md) | [pages/contribution-rating.md](https://github.com/intersective/practera-app/blob/main/specs/pages/contribution-rating.md) | — | — | ⚠️ API spec missing for submission mutation |
| Meeting polls | Delivery | [design/schedule/components/poll-panel.md](https://github.com/intersective/practera-admin-app/blob/main/specs/design/schedule/components/poll-panel.md) | [pages/meeting-poll.md](https://github.com/intersective/practera-app/blob/main/specs/pages/meeting-poll.md) | — | [objects/meeting.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/objects/meeting.md) | ⚠️ Needs spec-to-API cross-check |
| Auth (JWT handoff) | Foundation | [foundation/auth.md](https://github.com/intersective/practera-admin-app/blob/main/specs/foundation/auth.md) | [auth/index.md](https://github.com/intersective/practera-app/blob/main/specs/auth/index.md) | [specs/api/auth.md](https://github.com/intersective/practera-project-hub/blob/main/specs/api/auth.md) | [handler.md](https://github.com/intersective/practera-graphql-api/blob/main/specs/handler.md) | ✅ Aligned |

## Known Issues and Gaps

> Human-in-the-loop review required for items flagged ⚠️ below.

### 1. practera-app specs are draft — need `specguard align`

17 specs were bootstrapped from source but test alignment has not run yet. Running `specguard align --app app-v3` in the practera-app repo will map existing `.spec.ts` unit tests to the new spec scenarios.

**Action:** Run `specguard align --app app-v3` and review the output for unaligned tests.

### 2. practera-app to practera-graphql-api API cross-check needed (⚠️)

The practera-app specs document page behaviour but do not yet reference specific GraphQL operations (query/mutation names, field names). Each ⚠️ row in the matrix above needs a manual review to confirm:
- The correct GraphQL operations are named in the app spec
- The field types match what the API spec defines
- Error handling is consistent

**Action (human-in-the-loop):** For each ⚠️ row, open the app spec and the API spec side-by-side and verify alignment. Flag any mismatches as issues in the relevant repo.

### 3. Contribution rating mutation not in API spec

The `contribution-rating` page in practera-app submits Team 360 ratings, but there is no dedicated GraphQL mutation spec for this in practera-graphql-api. The submission likely uses an assessment mutation but this is not confirmed.

**Action (human-in-the-loop):** Confirm which GraphQL mutation handles contribution rating submission and update both specs accordingly.

### 4. App → project-hub integration not fully specced

Learners can view project briefs via a modal on the home page (practera-app), but the integration between practera-app and practera-project-hub (how briefs surface to learners in-app) is not fully specified in either repo.

**Action (human-in-the-loop):** Determine the data flow (does project-hub push to Practera, or does practera-app call project-hub?) and add a spec for this integration.

### 5. Admin-app audit log spec missing (minor)

The architecture index references `report/audit/index.md` for an audit log viewer at `/audit`, but the spec file does not exist in practera-admin-app.

**Action:** Create `specs/report/audit/index.md` in practera-admin-app.

### 6. project-hub test alignment pending

The practera-project-hub SpecGuard config is in place. Running `specguard align --app project-hub` will map the existing Jest and Playwright tests to the new SpecGuard specs.

**Action:** Run `specguard align --app project-hub` and review.
