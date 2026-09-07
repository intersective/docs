# Experience Designer

The Experience Designer is your authoring canvas. Use it to build the complete structure of your program — milestones, activities, and tasks — and to manage the media files used throughout.

Navigate to **Design** in the left sidebar (route `/design`).

![Screenshot](../../assets/placeholder.png)

---

## Two tabs

The Designer has two tabs at the top:

- **Structure** — the main experience design canvas.
- **Media** — the media library for this experience (see [Media Library](media-library.md)).

---

## Understanding the hierarchy

Practera experiences are structured as a three-level hierarchy:

```
Experience
├── Milestone 1
│   ├── Activity A
│   │   ├── Task 1 (Assessment)
│   │   └── Task 2 (Topic)
│   └── Activity B
│       └── Task 3 (Event)
└── Milestone 2
    └── ...
```

- **Milestones** — major phases or stages of the program (e.g. "Research", "Analysis", "Delivery").
- **Activities** — groups of tasks within a milestone. Learners see activities as steps to complete.
- **Tasks** — the actual learning objects: assessments, topics, events, todos, and more.

---

## Working with milestones

### Add a milestone

Click **+ Add Milestone** at the bottom of the milestone list. Name it and press **Enter**.

### Reorder milestones

Drag the handle (≡) on the left of a milestone row to move it up or down.

### Edit milestone settings

Click the milestone name to expand its settings: name, description, due date, and lock/hide controls.

### Delete a milestone

Click the **⋮ menu** on a milestone row → **Delete**. You must remove all activities first.

---

## Working with activities

### Add an activity

1. Click a milestone to expand it.
2. Click **+ Add Activity** inside the milestone.
3. Name the activity.

### Reorder activities

Drag activities within a milestone using the (≡) handle.

### Edit activity settings

Click an activity to open the **Activity Preview Panel** on the right. From there you can edit the name, description, lead image, and lock/hide settings.

---

## Working with tasks

### Add a task

1. Select an activity (click its name).
2. The **Block Palette** appears in the right panel.
3. Click a task type to add it to the activity.

### Task types

| Task type | Description |
|-----------|-------------|
| **Assessment** | Learner submits work; reviewer gives feedback |
| **Topic** | Static content: text, video embed, file, audio |
| **Event** | A live session (workshop, coaching call) |
| **Todo** | Individual checklist task |
| **Team Todo** | Collaborative checklist shared by the team |
| **Survey** | Embedded form/poll (Qualtrics or similar) |
| **Video** | Embedded video (YouTube, Vimeo, Kaltura) |
| **PDF** | Embedded PDF document |

### Edit a task

Click the task in the activity list to open its **inline editor**. Each task type has relevant fields:

- **Assessment**: title, instructions, due date, reviewer type (auto/manual), question builder
- **Topic**: title, rich text content, attachments, video URL, audio file
- **Event**: title, date/time, location, description

For complex assessments, click **Full Screen** to open a dedicated editor.

### Reorder tasks

Drag tasks within an activity using the (≡) handle.

### Delete a task

Click the **⋮ menu** on a task row → **Delete** (with confirmation).

---

## Lock / Hide controls

Every milestone, activity, and task has **Lock** and **Hide** controls:

- 🔒 **Lock** — learners can see the item but cannot interact with it until it is unlocked (e.g. by a trigger or manual unlock).
- 👁 **Hide** — the item is completely invisible to learners.

Use these for adaptive learning pathways — lock advanced content until a prerequisite is complete.

See **Expert → Triggers** to set up automatic unlock rules.

---

## Role visibility

Target content to specific roles:

1. Click a task to open its settings.
2. Under **Role Visibility**, choose: **All**, **Learner only**, **Reviewer only**, or **Coordinator only**.

This is useful for adding reviewer-only briefings or coordinator-only reference materials within the same activity.

---

## Autosave

The Designer saves automatically as you work. A **Saving…** indicator appears in the top right corner. Once the save completes, it changes to **Saved ✓**.

If a save fails (e.g. network error), an error banner appears. Do not close the tab — wait for connectivity to return and the save will retry automatically.

---

## Import and export

### Export experience

Click the **⋮ menu** in the top right of the Designer → **Export JSON**. Downloads a complete JSON snapshot of the experience structure — useful as a backup or for cloning to another instance.

### Import experience

Click **⋮ menu** → **Import JSON** → select a previously exported file. This overwrites the current structure with the imported one.

!!! warning
    Importing overwrites all existing milestones, activities, and tasks. Export first if you want to keep the current structure.

---

## Related

- [Media Library](media-library.md) — manage files for your experience
- [Calendar](calendar.md) — schedule events linked to activities
- [The Experience Designer Overview](../../help-articles/becoming-a-practera-power-user/the-experience-designer-overview.md) (Help Center)
