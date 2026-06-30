# Connect Google Meet Hardware to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage
Article ID: 52412502456083
Last Updated: 2026-06-15T19:14:07Z

Turn idle Google Meet hardware into digital signage. When a room is between meetings, OptiSigns plays your assigned content — announcements, dashboards, branding, menus — right on the room display, and the device returns to the normal Meet UI the moment a meeting starts.

This guide covers the **two ways to connect Google Meet hardware to OptiSigns**, so you can pick the one that fits how your organization works.

---

## Two ways to connect

|  | **Signage URL**  ·  *Recommended, fastest start* | **Service Account** |
| --- | --- | --- |
| **What it gives you** | Get content on a room in minutes — no Google Cloud setup. | OptiSigns **discovers and lists all your Meet hardware** (model, online/offline) in one place. |
| **Google setup** | None. You paste a URL in the Google Admin Console. | A Workspace super-admin registers a read-only service account with domain-wide delegation. |
| **Best for** | Getting started, a few rooms, or when you can't set up a service account. | Managing a fleet of rooms and seeing their status alongside your other screens. |
| **Who can set it up** | A Google Workspace admin. | A Google Workspace **super-admin**, one time. |

> **Important — read this first.** Google does **not** offer a way for apps to push content to Meet hardware automatically. So with **either** method, the final step is a **one-time paste** of an OptiSigns signage URL into the **Google Admin Console**. The **Service Account** method doesn't push content for you — it gives OptiSigns *visibility* into your rooms. Many teams use **both**: a Service Account to see every room, and Signage URLs to deliver the content.
>
> A third method, **Marketplace OAuth**, is shown as **Coming soon** in the app — use **Signage URL** or **Service Account** for now.

---

## What you'll need

- **An OptiSigns account** on a plan that includes device management (MDM / room integrations), with the **Owner** or **Super Admin** role. [Start a free trial](https://www.optisigns.com/free-trial) — you only pay for rooms you activate signage on.
- **Google Meet hardware** (ChromeOS-based Meet devices) enrolled in your Google Workspace.
- A **Google Workspace admin** who can paste a signage URL in the Admin Console.
- **For the Service Account method only:** a Google Workspace **super-admin** who can create a service account and grant domain-wide delegation.

---

## How it works

OptiSigns generates a secure **signage URL** for each screen you want to show on a room. You set that URL as the room's digital-signage URL in the **Google Admin Console**; from then on the room plays whatever you assign in OptiSigns, and updates are live. When a meeting starts — or someone wakes the room — the display returns to the normal Meet UI automatically, with no impact on meeting quality or scheduled meetings.

---

## Open the Google Meet page

In OptiSigns, open **Devices** in the top navigation, then in the left sidebar under **Room Integrations**, click **Google Meet**. If you haven't connected yet, you'll see the connect methods.

![OptiSigns Google Meet — choose how to connect: Signage URL (recommended), Service Account, and Marketplace OAuth (coming soon)](https://support.optisigns.com/hc/article_attachments/52412499875091)

Pick your method below.

---

# Method 1 — Connect with a Signage URL (recommended)

No Google Cloud setup. You'll mint a URL in OptiSigns, give it content, and paste it into the Google Admin Console.

### Step 1 — Mint a Signage URL

On the **Signage URL** card, click **Mint URLs**. In the **New Signage URL** dialog, give the URL a **Name** (for example, your room or location). The optional **Target label** is just a note to help you remember where you'll paste it; it doesn't control anything. Click **Next**.

![The New Signage URL dialog — name the URL, then click Next](https://support.optisigns.com/hc/article_attachments/52412466531475)

### Step 2 — Assign content

Clicking **Next** creates the URL and opens the **Signage URLs** tab. On the new row, click **+ Assign content**, choose a **Content Type** — **Asset**, **Playlist**, or **Schedule** — pick the item to play, and **Save**. OptiSigns copies the signage URL to your clipboard.

### Step 3 — Paste the URL in the Google Admin Console

Open the [Google Admin Console](https://admin.google.com/ac/meet/devices), go to **Devices → Google Meet hardware**, select the device or organizational unit (OU) you want, and set its **digital signage URL** to the OptiSigns URL you copied. (OptiSigns shows the exact steps in the **paste instructions** dialog, and you can reopen them any time with **Show me how to paste** on the Signage URLs tab.)

Within about a minute the room fetches the URL and your content appears while the room is idle. Start a test meeting — content should clear when the meeting connects.

> Repeat Steps 1–3 to mint a URL for each room or OU. You manage all minted URLs (and reassign their content any time) under the **Signage URLs** tab.

---

# Method 2 — Connect with a Service Account

This connects a **read-only** Google Cloud service account so OptiSigns can discover and list all your Meet hardware automatically. (You'll still deliver content with a signage URL — see "Put content on a room" below.)

### Step 1 — Review the setup steps and scopes

On the **Service Account** card, click **View setup steps**. OptiSigns walks you through creating the service account and lists the two read-only scopes it needs.

![The setup-steps dialog — the five steps and the two read-only Admin SDK scopes; use Copy all scopes](https://support.optisigns.com/hc/article_attachments/52412466682259)

In the Google Cloud Console (as a Workspace super-admin):

1. Create a project and enable the **Admin SDK API**.
2. Create a **Service Account** and download its **JSON key**.
3. In the Workspace **Admin Console**, grant the service account **domain-wide delegation** for the two scopes below. Tip: click **Copy all scopes** in OptiSigns and paste them straight into the scope picker.

| Scope | What it's for |
| --- | --- |
| `…/auth/admin.directory.device.chromeos` | Reads Meet hardware (ChromeOS device) inventory. |
| `…/auth/admin.directory.device.chromeos.readonly` | Reads device health signals (online/offline, OS version). |

### Step 2 — Add the service account in OptiSigns

Back on the **Service Account** card, click **Add Service Account** and fill in:

- **Display Name** — any label (for example, `Acme Workspace`)
- **Service Account Email** — from the JSON key
- **Impersonation Email** — a Workspace **super-admin** email the service account will impersonate (a dedicated admin is recommended)
- **Service Account JSON Key** — paste the entire downloaded JSON file

Click **Test Connection**. OptiSigns validates the credentials against Google and shows your workspace domain on success — then **Save & Connect** lights up. Click it.

![The Add Service Account dialog — fill the fields, then Test Connection before Save & Connect](https://support.optisigns.com/hc/article_attachments/52412503183251)

Within a few minutes your Meet hardware appears in the **Devices** tab, each with its model and live online/offline status.

![The connected Devices tab — discovered Google Meet hardware with status and model](https://support.optisigns.com/hc/article_attachments/52412490811667)

### Put content on a room

Discovering rooms doesn't put content on them — that still uses a signage URL. From the **Signage URLs** tab, click **New Signage URL** and follow **Method 1, Steps 1–3** above to mint a URL, assign content, and paste it into the Google Admin Console for that room or OU.

---

## Licensing

Activating signage on a Meet room uses **one screen license** from your OptiSigns pool — the same licenses you use for any other screen. Discovered rooms you haven't activated are free; you're only billed for rooms you turn signage on for. [See full pricing](https://www.optisigns.com/pricing).

---

## Troubleshooting

**"Test Connection" fails with an invalid-key error.** Re-paste the **entire** JSON key file (it must include `private_key` and `client_email`). If you regenerated the key, download and paste the new one.

**"Test Connection" fails with a delegation or scope error.** Domain-wide delegation isn't granted, or the scopes don't match. In the Workspace Admin Console, confirm the service account's client ID is delegated **both** `admin.directory.device.chromeos` scopes, then try again. Consent changes take about a minute.

**My rooms don't appear after saving the service account.** The first inventory sync can take a few minutes. Click **Sync now** on the Google Meet page. Confirm the impersonation email is a **super-admin** and the Admin SDK API is enabled.

**I pasted the URL but nothing shows on the room.** Confirm the device is **online**, and that you set the OptiSigns URL as the room's digital-signage URL on the **correct OU/device** in the Google Admin Console. Make sure you pasted the full URL (it begins with `https://`).

**Content shows but doesn't clear when a meeting starts.** This is handled by Google's Meet hardware signage behavior — content displays only while the room is idle and returns to the Meet UI on a call.

---

## Need help?

- Email: [support@optisigns.com](mailto:support@optisigns.com)
- More guides: [support.optisigns.com](https://support.optisigns.com)
- Related: [Connect Zoom Rooms to OptiSigns](https://support.optisigns.com/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage) · [Connect Microsoft Teams Rooms to OptiSigns](https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage) · [Connect Cisco Webex Rooms to OptiSigns](https://support.optisigns.com/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage)
