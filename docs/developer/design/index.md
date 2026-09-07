<!-- status: living -->

# Experience Design

The Experience Design stage is where coordinators and programme designers build and configure learning experiences. All design tooling lives in practera-admin-app and is backed by practera-graphql-api.

### Programme Structure Designer

Drag-drop milestone/activity/task tree. Role-based content visibility (`target_roles`). Lock/reveal triggers based on achievements. Import/export of programme JSON. Full-screen structure diagram.

[Spec: design/design/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/design/)

### Content Authoring

Topic editor (TipTap rich text), assessment question builder (multiple types), task type editors (inline and fullscreen), rich media embedding.

[Spec: design/structure/editors/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/design/structure/editors/)

### Media Library

TUS-protocol file uploads to S3. Cross-experience media browser. File picker component (modal + pagination). Rename/delete/preview.

[Spec: design/media/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/media/)

### Scheduling

ProScheduler calendar for event management. Event form (details, schedule, video, notifications tabs). QR-based attendance tracking. Meeting polls. Comms integration (±90 days).

[Spec: design/schedule/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/schedule/)

### Automation (ELSA)

Rule-based automation engine. Trigger rules CRUD. Credentials/badges CRUD. Activity log (ELSA todo actions).

[Spec: design/automation/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/automation/)

### AI Experts

Scoped AI experts (experience/institution/global). Version management. Testing interface. Knowledge file uploads. Library publishing and approval workflow. Expert chat panel.

[Spec: design/ai-experts/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/ai-experts/)

### Settings

Experience and institution settings: general, branding, custom roles, LTI 1.3, AI provider config, taxonomy (configurable terminology), notification templates. AI model capability mappings.

[Spec: design/settings/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/settings/)

### Library

Cross-experience content library: programme templates, media files, AI experts. Hero cards, recently added strip, category navigation.

[Spec: design/library/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/library/)

### Go-Live Checklist

Pre/post-launch validation checklist. Guided go-live workflow with configurable settings.

[Spec: design/checklist/](https://github.com/intersective/practera-admin-app/tree/main/specs/design/checklist/)
