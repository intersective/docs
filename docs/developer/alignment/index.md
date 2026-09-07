<!-- status: draft — updated as specs are bootstrapped -->

# Alignment Status

This page tracks spec coverage across Practera repos and flags known gaps between frontend and backend specifications.

## Spec Coverage

| Repo | Specs | Format | Status |
|------|-------|--------|--------|
| practera-admin-app | 193 | SpecGuard Living Specs | ✅ Good coverage |
| practera-graphql-api | 270 | SpecGuard Living Specs | ✅ Good coverage |
| practera-login-app | 32 | SpecGuard Living Specs | ✅ Good coverage |
| practera-login-api | 59 | SpecGuard Living Specs | ✅ Good coverage |
| practera-project-hub | 9 | Speckit format | 🔄 Needs SpecGuard conversion |
| practera-app | 0 | None (SpecGuard configured) | ❌ Needs bootstrapping |

## Capability Alignment Matrix

| Capability | Stage | Admin-App Spec | App Spec | Project-Hub Spec | API Spec | Status |
|------------|-------|---------------|----------|-----------------|----------|--------|
| Assessment submission | Delivery | deliver/feedback/submissions-table.md | ❌ No spec | — | mutations/assessment.md | ⚠️ Gap |
| Assessment review | Delivery | deliver/feedback/submission-drawer.md | ❌ No spec | — | resolvers/mutations/saveReviewAnswer.md | ⚠️ Gap |
| Chat / messaging | Delivery | deliver/chat/ | ❌ No spec | — | mutations/chat.md | ⚠️ Gap |
| Milestone / activity tree | Delivery | — | ❌ No spec | — | objects/activity.md | ⚠️ Gap |
| Topic content viewer | Delivery | — | ❌ No spec | — | objects/topic.md | ⚠️ Gap |
| Pulse check | Delivery | — | ❌ No spec | — | objects/pulse-check.md | ⚠️ Gap |
| Badges / achievements | Delivery | — | ❌ No spec | — | objects/achievement.md, mutations/achievement.md | ⚠️ Gap |
| Event booking (learner) | Delivery | design/schedule/ (admin only) | ❌ No spec | — | objects/event.md, mutations/event.md | ⚠️ Gap |
| Enrolment management | Delivery | deliver/enrolments/ | — | — | mutations/enrolment.md | ✅ Aligned |
| Programme design | Design | design/design/ | — | — | mutations/content.md, mutations/experience.md | ✅ Aligned |
| Scheduling (admin) | Design | design/schedule/ | — | — | objects/event.md | ✅ Aligned |
| Automation (ELSA) | Design | design/automation/ | — | — | queries/automation.md | ✅ Aligned |
| AI Experts | Design | design/ai-experts/ | — | — | objects/ai-expert.md, queries/ai.md | ✅ Aligned |
| Metrics / KPIs | Reporting | report/metrics/ | — | — | queries/metric.md | ✅ Aligned |
| Custom reports | Reporting | report/reports/ | — | — | queries/reports.md | ✅ Aligned |
| Campaign management | Sourcing | — | — | spec.md (Speckit) | — | 🔄 Speckit→SpecGuard |
| Project brief intake | Sourcing | — | — | spec.md (Speckit) | — | 🔄 Speckit→SpecGuard |
| Learner project application | Sourcing | — | — | spec.md (Speckit) | — | 🔄 Speckit→SpecGuard |
| Team management | Delivery | deliver/teams/ | — | mutations/team (via API) | mutations/team.md | ✅ Aligned |

## Known Gaps

### Critical: practera-app has no Living Specs

The learner-facing Angular app has ~20 page modules with zero SpecGuard Living Specs. All learner-side capabilities are implemented but undocumented at the spec level. Every row with "❌ No spec" in the App Spec column above is a gap from this cause.

Pages needing specs: home, activity-mobile, activity-desktop, assessment-mobile, review-mobile, review-desktop, topic-mobile, chat (list/room/info/preview), events (list/detail), badges-certificates, due-dates, checkin, settings, notifications, meeting-poll, contribution-rating, experiences, plus auth flows.

**Action:** Run `specguard reverse --app app-v3` to bootstrap baseline specs from source.

### Moderate: practera-project-hub uses Speckit (not SpecGuard)

The project hub has 9 Speckit format files (spec.md, plan.md, tasks.md, data-model.md, contracts/openapi.yaml, etc.). These need conversion to SpecGuard Living Specs to enable drift detection and test alignment.

**Action:** Add `.specguard/config.json`, run `specguard reverse --all`, import speckit user stories as SpecGuard scenarios.

### Minor: Admin-app audit log spec missing

The architecture index references `report/audit/index.md` for an audit log viewer at `/audit`, but this spec file does not exist yet.
