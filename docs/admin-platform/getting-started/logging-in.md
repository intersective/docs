# Logging In

Every session in the Practera Admin Platform begins at the **Practera Login App**. This is a dedicated sign-in page — separate from the learner app — that verifies your identity and sends you to the correct admin interface for your role and institution.

![Screenshot](../../assets/placeholder.png)

---

## Where to log in

Open the Login App using one of these URLs:

- **Standard login:** [login.practera.com](https://login.practera.com)
- **Institution-branded login:** your organisation may provide a custom URL (for example, `login.youruniversity.edu`). Check with your program administrator if you are unsure.

Bookmark the URL you use most often. You will return here whenever your session expires or you sign out.

---

## Magic link login (recommended)

Practera uses **passwordless login** by default. You do not need to remember a password.

1. **Enter your email address** — use the email your administrator registered for you.
2. **Check your inbox** — Practera sends a one-time magic link within a minute or two.
3. **Click the link** — your browser opens the Admin Platform and you are signed in.

!!! note "Link expiry"
    Magic links are single-use and expire after a short period. If the link has expired, return to the Login App and request a new one.

!!! tip "Check spam folders"
    If you do not receive the email, check your junk or spam folder. Add the sender to your safe-senders list if your institution filters external mail aggressively.

---

## Passkey login (optional)

If your organisation has enabled passkeys, you can sign in faster using **Face ID, Touch ID, Windows Hello, or a hardware security key** — no email required after the first setup.

1. On the Login App, choose the passkey option (if shown).
2. Enter your email address.
3. Complete the biometric or key prompt when your browser asks.

Passkeys are tied to the device and browser where you registered them. Register a passkey on each device you regularly use for admin work.

---

## After you sign in

The Login App checks your account and routes you to the right place:

- **Coordinators and administrators** → Practera Admin Platform
- **Learners and reviewers** → Practera App (the learner interface)

### Wrong platform / wrong role

If you land on the learner app or see an **access denied** or **wrong role** message, your account may be registered with a different role than you expected.

| Symptom | Likely cause | What to do |
|---------|--------------|------------|
| Redirected to the learner app | Your account is enrolled as a learner, not an admin | Ask your institution administrator to assign you a coordinator or admin role |
| "Unauthorized" or blank page | Your account is not linked to this institution's stack | Confirm you are using the correct login URL for your region or institution |
| No experiences visible | You are logged in but have no admin permissions | Contact your institution administrator to grant access |

!!! warning "Do not share login links"
    Magic links grant full access to your account. Never forward them to colleagues. Each person must log in with their own email address.

---

## How sessions work

When you sign in successfully, Practera stores a secure token in your browser. This keeps you logged in as you move between pages — you do not need to re-enter your email for every visit.

| Detail | Behaviour |
|--------|-----------|
| **Session duration** | Your session lasts up to **7 days** from the last successful login |
| **Storage** | The token is saved in your browser's local storage on that device |
| **Expiry** | After 7 days, or if an administrator revokes access, you will be prompted to log in again |
| **Multiple tabs** | All open Admin Platform tabs share the same session |

!!! note "Shared computers"
    If you use a shared or public computer, always log out when you finish. Closing the browser tab does not always end your session.

---

## Logging out

To end your session explicitly:

1. Click your **name** in the top-right corner of the Admin Platform.
2. Select **Log Out**.

You are returned to the Login App. Your browser token is cleared, and anyone using that computer afterward will need to sign in again.

You can also use **Refresh** in the same menu to reload your permissions without signing out — useful if an administrator has just changed your role.

---

## Troubleshooting

**I never received the magic link**

- Wait two minutes, then request a new link.
- Confirm you typed your email correctly.
- Check with your administrator that your account exists and is active.

**The magic link opens but I am not logged in**

- Try a different browser or disable strict privacy extensions temporarily.
- Ensure cookies and local storage are enabled for the Practera domain.

**I was logged out unexpectedly**

- Sessions expire after 7 days of inactivity.
- Your administrator may have removed your access or changed your role.
- Log in again; if the problem persists, contact your administrator.

---

## What's next?

- [Navigation](navigation.md) — learn the layout of the Admin Platform
- [Switching experiences](switching-experiences.md) — select the program you want to manage
