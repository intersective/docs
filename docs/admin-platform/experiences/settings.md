# Experience Settings

**Experience Settings** is where you configure the identity, appearance, and behaviour of a single program. Access it from the **Setup** section in the sidebar, from the **Settings** action on an experience card, or by navigating to `/settings` while an experience is selected.

![Screenshot](../../assets/placeholder.png)

---

## Opening Settings

Make sure the correct experience is selected in the top bar before opening Settings — all changes apply to that program only.

| Access path | Steps |
|-------------|-------|
| **Sidebar** | Select your experience → **Setup → Settings** |
| **Institution menu** | **Experiences** → card menu → **Settings** |
| **Direct URL** | `/settings` (with an experience active) |

Institution-wide settings (logo, LTI, feature flags) are configured separately under **Institution → Settings**, not on this page.

---

## Settings sections

Experience Settings is organised into six areas. Each section appears as its own panel on the settings page.

| Section | What you configure |
|---------|-------------------|
| **General** | Experience name, description, duration, lead image, and status (Draft / Live / Inactive) |
| **Branding** | Primary colour and logo shown to learners in the Practera App |
| **Guides** | URLs for the learner guide and reviewer guide (linked from the learner and reviewer interfaces) |
| **Notifications** | Toggles for which notification categories are sent (reminders, feedback alerts, enrolment notices, and more) |
| **Integrations** | External tool URLs, webhooks, and LTI-related options for this experience |
| **Roles** | Custom display names for participant roles (for example, renaming "Mentor" to "Industry Partner") |

### General

Use **General** to set the fundamentals learners and coordinators see everywhere:

- **Name** — the program title on cards, emails, and the top bar
- **Description** — a short summary shown on the Experiences list and in some reports
- **Duration** — expected program length (used for scheduling hints and reporting)
- **Lead image** — hero image for the experience in the learner app
- **Status** — Draft, Live, or Inactive (you can also change status via the **Go Live** control in the top bar)

### Branding

Experience-level branding overrides the default look for learners in **this program only**:

- **Primary colour** — accent colour in the learner app for this experience
- **Logo** — optional program-specific logo

!!! tip "Primary colour affects admin chrome too"
    The primary colour you set here also influences the **top bar border** and **user avatar background** in the Admin Platform while this experience is selected. Choose a colour that meets contrast guidelines so text remains readable.

### Guides

Provide links to documentation your institution hosts externally:

- **Learner guide URL** — help article or handbook for participants
- **Reviewer guide URL** — instructions for mentors, experts, and peer reviewers

Learners and reviewers see these links in context within the Practera App.

### Notifications

Toggle notification categories on or off for this experience. Turning a category off stops automated emails and in-app alerts for that type — useful during testing or when your institution sends equivalent communications through another system.

!!! warning "Disabling reminders affects learner behaviour"
    If you turn off submission reminders, expect lower on-time submission rates. Review the [Determining Which Notifications Get Sent](../../help-articles/onboarding/determining-which-notifications-get-sent.md) guide before bulk-disabling categories.

### Integrations

Configure experience-scoped integration endpoints:

- Links to external tools embedded in activities
- Webhook endpoints (where enabled)
- LTI launch options specific to this program

Institution-level LTI credentials are managed under [Institution Integrations](../institutions/integrations.md).

### Roles

The **Roles** section lets you rename standard role labels for this experience without changing permissions. For example, you might display "Coach" instead of "Mentor" throughout the learner interface. Permission behaviour is unchanged — only the visible label updates.

---

## Autosave

Experience Settings uses **automatic saving**. When you edit a field, your change is saved shortly after you stop typing — there is no separate Save button.

!!! note "Autosave timing"
    Changes are saved automatically after a brief pause (approximately 800 milliseconds) once you finish editing a field. You may see a subtle saving indicator near the top of the page. Wait for saving to complete before navigating away if you have made important changes.

If autosave fails (for example, due to a network interruption), an error message appears. Refresh the page and re-enter the change, or try again when your connection is stable.

---

## Tips for coordinators

- Set **General → Name** and **Description** early — they appear on the Experiences list and in coordinator reports
- Upload a **lead image** before going live; it is the first thing learners see when they open the program
- Configure **Notifications** before your first enrolment wave so reminders are active from day one
- Use **Roles** to match your institution's terminology — it reduces confusion for learners and reviewers

---

## Related guides

- [Branding Your Experience](../../help-articles/onboarding/branding-your-experience.md) — visual identity best practices
- [Changing Experience Settings](../../help-articles/onboarding/changing-experience-settings.md) — legacy walkthrough with additional detail
- [Going Live](go-live.md) — publish when settings are complete
- [Institution Branding](../institutions/branding.md) — institution-wide logo and colours

---

*Last updated: August 2026*
