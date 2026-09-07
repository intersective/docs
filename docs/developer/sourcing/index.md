<!-- status: living -->

# Project Sourcing

The Project Sourcing stage enables institutions to attract and onboard industry clients, collect structured project briefs, and assign approved projects to learning experiences. It is implemented in practera-project-hub (Next.js 16 + Prisma).

Specs live at: https://github.com/intersective/practera-project-hub/tree/main/specs/002-industry-project-web-platform/

> **Note:** practera-project-hub currently uses Speckit format (not SpecGuard Living Specs). See [Alignment Status](../alignment/index.md).

### Campaign Management

Admins create campaigns by selecting project brief templates and setting active windows. The system generates a unique, shareable intake URL for each campaign, scoped to the admin's institution (from JWT). URLs expire at campaign end.

[Feature Spec — User Story 1](https://github.com/intersective/practera-project-hub/tree/main/specs/002-industry-project-web-platform/spec.md)

### AI-Guided Project Brief Intake

External clients access the intake URL without authentication. An AI chatbot (OpenAI/Claude), guided by the selected brief templates, collects project details via conversation. A traditional form is also available. Draft created on first name/email capture. Chat state and brief ID persisted in localStorage for resumption.

[Feature Spec — User Story 2](https://github.com/intersective/practera-project-hub/tree/main/specs/002-industry-project-web-platform/spec.md)

### Brief Lifecycle and Approval

Briefs progress through: `DRAFT` → `CLIENT_APPROVED` → `ADMIN_APPROVED` → `ARCHIVED`. Admin edits to a `CLIENT_APPROVED` brief revert it to `DRAFT` and trigger a client re-approval email. Briefs must reach `CLIENT_APPROVED` before admin can approve.

[Feature Spec — User Story 3](https://github.com/intersective/practera-project-hub/tree/main/specs/002-industry-project-web-platform/spec.md)

### Experience Assignment

Admins fetch Practera experiences via the GraphQL API and assign `ADMIN_APPROVED` briefs to them. If the experience doesn't exist locally, it is auto-created. Admins set application periods (start/end dates) per experience and can manually close/reopen applications per brief.

[Feature Spec — User Story 4](https://github.com/intersective/practera-project-hub/tree/main/specs/002-industry-project-web-platform/spec.md)

### Learner Application

Learners authenticate via JWT (`participant` role) and view projects assigned to their experience. They can apply for up to 5 projects with unique priorities (1–5) during the application window. Applications can be cancelled and resubmitted within the window.

[Feature Spec — User Story 7](https://github.com/intersective/practera-project-hub/tree/main/specs/002-industry-project-web-platform/spec.md)

### Team Creation

Admins create teams in Practera experiences via the GraphQL API. Team data is stored in Practera (not in project-hub's own database).

[Feature Spec — User Story 5](https://github.com/intersective/practera-project-hub/tree/main/specs/002-industry-project-web-platform/spec.md)
