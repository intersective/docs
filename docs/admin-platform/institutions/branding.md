# Branding Your Institution

Institution branding ensures learners, reviewers, and coordinators see **your organisation's identity** when they use Practera — not a generic platform look. The logo and primary colour appear in the Admin Platform top bar, the learner app, and many automated emails.

![Screenshot](../../assets/placeholder.png)

---

## Where to configure branding

1. Open the **Institution menu** by clicking your institution badge in the top bar
2. Select **Settings**
3. Open the **Branding** section

CS administrators can reach the same settings from **Institutions** → select institution → **Settings** tab → **Branding**.

Experience-level branding (for a single program) is configured separately under [Experience Settings](../experiences/settings.md). Institution branding applies as the default across all experiences unless overridden.

---

## Primary colour

Set your institution's **primary colour** — the accent used for buttons, highlights, and key UI elements.

| Method | How |
|--------|-----|
| **Hex code** | Enter a six-digit hex value (for example, `#1A4B8C`) |
| **Colour picker** | Click the swatch and choose visually |

The primary colour is applied in:

- **Admin Platform** — top bar accent, action buttons, and highlight states
- **Practera App** — learner-facing buttons and navigation accents (where experience branding does not override)
- **Emails** — headers and call-to-action buttons in system notifications

!!! tip "Choose a colour with sufficient contrast"
    Very light colours can make white button text hard to read. Test your choice on both the admin top bar and a learner activity screen. Your marketing team's brand guidelines usually specify an accessible primary and an alternate for digital use.

---

## Logo upload

Upload your institution logo so it appears alongside the Practera interface chrome.

| Requirement | Recommendation |
|-------------|----------------|
| **Format** | SVG (preferred) or PNG with transparent background |
| **Dimensions** | At least **200 × 80 pixels**, or wider with similar aspect ratio |
| **File size** | Keep under 500 KB for fast loading |

The logo appears in:

- **Admin top bar** — next to or in place of generic institution text
- **Learner-facing emails** — magic links, reminders, and feedback notifications
- **Selected learner app screens** — login and program header areas

!!! note "SVG scales best"
    If you have both formats, prefer SVG. It stays sharp on high-resolution displays and emails that scale images.

---

## How branding flows to users

```
Institution Settings → Branding
        │
        ├── Admin Platform top bar (all coordinators at institution)
        ├── Learner emails (enrolment, reminders, feedback)
        └── Practera App (default theme for all experiences)
                │
                └── Experience Settings → Branding (optional override per program)
```

When an experience sets its own logo or primary colour, that **experience override** takes precedence for learners in that program only. Coordinators still see institution branding in areas not scoped to a single experience.

---

## Previewing your changes

Branding updates are saved when you confirm the change in Settings. To see the result:

1. Save your logo and colour
2. **Refresh the page** (or log out and back in)
3. Check the **top bar** in the Admin Platform and, if possible, open the **Practera App** as a test learner

!!! tip "Send yourself a test email"
    Trigger a magic link login to your own email address after updating branding. Email clients are the most common place where logo sizing issues appear.

---

## Troubleshooting

| Issue | What to try |
|-------|-------------|
| Logo looks blurry | Upload a higher-resolution PNG or switch to SVG |
| Colour did not update | Hard-refresh the browser (Ctrl+F5 / Cmd+Shift+R) |
| Old logo in emails | Email templates cache briefly; wait a few minutes and resend a test |
| Experience shows different branding | Check **Experience Settings → Branding** for a program-level override |

---

## Related guides

- [Branding Your Experience](../../help-articles/onboarding/branding-your-experience.md) — program-level visual identity
- [Experience Settings](../experiences/settings.md) — per-experience colour and logo
- [Institution Overview and Tabs](overview.md) — where Settings lives in the institution detail page
- [Changing Institution Settings](../../help-articles/institution-set-up/changing-institution-settings.md) — additional institution configuration

---

*Last updated: August 2026*
