# Data Deletion

Practera provides tools to permanently delete personal data in accordance with GDPR and other data-protection regulations.

!!! warning "Deletion is irreversible"
    All deletion actions are permanent. Learner submissions, reviews, personal profiles, and activity history cannot be recovered after deletion. Always confirm the scope before proceeding.

---

## Where to find deletion tools

There are two entry points:

- **Institution → Settings → Data Deletion** — institution-level deletion settings and exemptions.
- **Institution → Experiences tab → Deletion Records** — audit trail of all past deletion actions.

![Screenshot](../../assets/placeholder.png)

---

## Deletion exemption

Some institutions are legally required to retain data for a minimum period (e.g. accreditation evidence). An exemption prevents automated scheduled deletion from running on this institution.

1. Navigate to **Institution → Settings → Data Deletion**.
2. Toggle **Deletion Exemption** to *On*.
3. The institution is now marked as exempt. Automated deletion will not run until the exemption is lifted.

!!! note
    Exemption does not prevent **manual** deletion requests initiated by a CS admin.

---

## Manual deletion request

Use this to fulfil a specific learner's right-to-erasure request, or to remove all inactive user data from a completed experience.

1. Navigate to **Institution → Settings → Data Deletion → Request Deletion**.
2. Choose the scope:
   - **Specific user** — enter the learner's email address.
   - **All inactive users** — removes data for users with no activity in the last 90 days.
   - **Full experience** — removes all participant data for a selected experience (use after an experience has been archived and no longer needs its data).
3. Review the **preview count** — the number of users and records affected.
4. Type **CONFIRM** in the confirmation field.
5. Click **Delete**.

A background job runs the deletion. You will receive an email confirmation once it completes (typically within a few minutes).

---

## Deletion audit trail

Every deletion action is logged and visible in the **Deletion Records** tab:

| Column | Description |
|--------|-------------|
| **Date** | When the deletion completed |
| **Requested by** | Admin who initiated it |
| **Scope** | Specific user / inactive / full experience |
| **Records deleted** | Count of records removed |
| **Status** | Completed / Failed |

This log is read-only and retained for 7 years to support compliance audits.

---

## User-initiated deletion (Right to Erasure)

If a learner requests deletion of their data:

1. Locate them in **Institution → Users**.
2. Click their name to open their profile.
3. Scroll to **Danger Zone → Delete User Data**.
4. Confirm the deletion.

Alternatively, email **support@practera.com** with the learner's email address and institution name, and the Practera support team will process it within 72 hours.

---

## Related

- [Institution overview](overview.md)
- [Integrations](integrations.md)
- [Deleting User Data](../../help-articles/essentials/deleting-user-data.md) (Help Center)
