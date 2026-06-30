# Connect Cisco Webex Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage
Article ID: 51343184586643
Last Updated: 2026-06-15T19:13:59Z

Turn idle Cisco Webex Rooms, Boards, and Desks into digital signage. When the device is in Standby, OptiSigns plays your assigned content — images, videos, dashboards, web apps — and clears it instantly the moment a meeting starts.

This guide walks a Webex Full Administrator through the one-time setup at the organization level, and then per-room signage activation.

---

## What you'll need

- **A Webex account** with the **Full Administrator** role for your organization. Any Webex tier with paired RoomOS devices is supported. (Required to approve OptiSigns in Webex Control Hub — read-only and device-only admins cannot consent.)
- **An OptiSigns account.** [Sign up for a free trial](https://www.optisigns.com/free-trial) — you only pay for rooms you activate signage on.
- **At least one WebEngine-capable RoomOS device** paired to your Webex org. Supported models include:
- Cisco Board Pro / Board Pro G2
- Cisco Desk Pro / Desk Mini
- Cisco Codec Pro / Codec EQ
- Cisco Room Bar Pro
- Cisco Room Kit EQX

> Older devices (Codec Plus, Room Kit Mini, original Board) do not support WebEngine and cannot run OptiSigns content. [Check WebEngine compatibility on the Cisco support site](https://help.webex.com/article/n7v7gxq).

---

## How OptiSigns works on Webex devices

OptiSigns uses the **Webex Digital Signage / Standby** feature built into RoomOS. We do not install an app on the device — instead, we set the device's signage URL via Webex's official Device Configurations API. Your content plays through the WebEngine browser only when the room is idle, and the device automatically returns to its normal meeting UI on any incoming call, scheduled meeting, or wake-on-presence.

There is no impact on meeting quality, screen-sharing, or Webex Assistant features.

---

## Step 1 — Sign in to OptiSigns

Go to [**app.optisigns.com**](https://app.optisigns.com/) and sign in (or create your account).

---

## Step 2 — Open the Webex Rooms page

In the top navigation, open **Devices**. In the left sidebar under **Room Integrations**, click **Webex Rooms**. Since you haven't connected yet, you'll see the **Control Hub OAuth** card with everything you need to get started.

![OptiSigns Devices — Room Integrations — Webex Rooms, the not-connected Control Hub OAuth card](https://support.optisigns.com/hc/article_attachments/52411191588755)

---

## Step 3 — Authorize OptiSigns in Cisco Control Hub

Click **View setup steps** to review exactly what OptiSigns will do and the permissions it needs, then click **Authorize in Cisco Control Hub**.

A new browser tab opens at Cisco Control Hub. Sign in as a **Webex Full Administrator** and approve the **OptiSigns Digital Signage** Service App for your organization. OptiSigns requests five scopes:

| Scope | What it's for |
| --- | --- |
| `spark-admin:devices_read` | Reads the Webex Rooms inventory and device-group membership. |
| `spark-admin:devices_write` | Pushes the signage URL to each Webex device via device configurations. |
| `spark:xapi_commands` | Sends xAPI commands (refresh, restart app) over Service App tokens. |
| `spark:xapi_statuses` | Reads device health signals (online state, peripheral status). |
| `spark-admin:organizations_read` | Reads org metadata to sanity-check the Org ID you paste. |

![The Connect with Cisco Control Hub OAuth dialog — the four setup steps and all five required scopes](https://support.optisigns.com/hc/article_attachments/52411197221395)

> If you see a permission error, you're not signed in as a Full Administrator. Ask your Webex admin to either approve OptiSigns for the org or grant you the Full Administrator role.

---

## Step 4 — Paste your Org ID and verify

Return to the OptiSigns tab. In the **Webex Organization ID** field, paste your organization's ID (find it in Control Hub under **Organization Settings → identifier**), then click **Verify Connection**.

OptiSigns mints Service App tokens and begins syncing. Within a few seconds the header flips to **Connected**, and your Webex rooms appear in the list alongside any Android, ChromeOS, or Linux signage devices on your account. Use **Sync now** any time to pull the latest inventory.

![Connected: the Webex Rooms list showing the org, rooms synced, and per-room push state](https://support.optisigns.com/hc/article_attachments/52411218876819)

---

## Step 5 — Activate signage on a room

By default, rooms are listed but **not activated**. Activation is per-room billing — you pay only for rooms with signage turned on.

1. Click any Webex room in the list to open its detail drawer.
2. Click **Activate Signage License**. The drawer shows how many licenses are available.
3. Confirm — your subscription updates immediately.

![The room detail drawer with the Activate Signage License button and available license count](https://support.optisigns.com/hc/article_attachments/52411212058003)

---

## Step 6 — Push content

With the room activated, you can assign content like any other OptiSigns screen. In the room drawer, click **Assign Content** (or **Change Content** if something is already playing), pick an **Asset**, **Playlist**, or **Schedule**, and save. The drawer shows what's currently playing and the room's signage URL.

![The activated room drawer — currently-playing content, Change Content and Remove Signage, and the signage URL](https://support.optisigns.com/hc/article_attachments/52411202243731)

Walk to the device. Within 10–30 seconds, your content appears during Standby. Try a test call — content should clear instantly when the call connects.

---

## Configure signage behavior (optional)

In the room drawer, the **Webex Settings** card lets you tune how signage plays on that device:

| Setting | What it does | Recommended |
| --- | --- | --- |
| **Interaction Mode** | Whether touch on a Board/Desk wakes the device or interacts with content | **Non-interactive (kiosk)** for lobby/info screens; **Interactive (touch)** for kiosk-style content |
| **Auto-refresh** | How often the device reloads the signage URL (`0 = never`) | 30 minutes (default) |
| **Mute** | Whether videos play with sound | Off (default) |
| **Enable** | Master on/off for digital signage — disabling preserves the URL so you can re-enable later | On |

Click **Save** to apply. Changes reach the device within about 10 seconds via Webex's API.

![The Webex Settings card — Interaction Mode, Auto-refresh, Mute, and Enable](https://support.optisigns.com/hc/article_attachments/52411197957267)

---

## Disconnecting OptiSigns

**From OptiSigns:** Webex Rooms page → **Disconnect Cisco Webex**. This stops content delivery, releases the screen licenses, and removes the signage URL from all paired devices.

**From Webex Control Hub:** Apps & Integrations → OptiSigns Digital Signage → **Remove**. This revokes our access token. Use this if you want to fully de-authorize the integration.

---

## Troubleshooting

**My rooms don't appear after Verify Connection.** Wait 30 seconds and click **Sync now** — the initial inventory sync can take up to a minute on large orgs. If still empty, confirm you have at least one paired device on a WebEngine-capable model (see "What you'll need" above).

**Content shows but doesn't clear when a meeting starts.** This usually means Standby is disabled on the device. In Control Hub, open the device → Configurations → search "Standby" → ensure `Standby Control = On`.

**Content looks zoomed-in or cropped.** Webex Boards and Desks render at 1920×1080. Use OptiSigns' built-in resolution settings on the asset, or design content at 1920×1080 for safe rendering across all devices.

**I get an authorization error in Control Hub.** You're not signed in as a Full Administrator. Ask your Webex admin to either approve OptiSigns at the org level or grant your account the Full Administrator role.

**A specific device shows "WebEngine not enabled."** Open the device in Control Hub → Configurations → set `WebEngine.Mode = On`. OptiSigns will retry automatically.

---

## Pricing

The OptiSigns Webex Rooms integration uses a screen license just like any other OptiSigns screen. A free trial is available — you're only billed once you activate signage on a room. [See full pricing](https://www.optisigns.com/pricing).

---

## Need help?

- Email: [support@optisigns.com](mailto:support@optisigns.com)
- More guides: [support.optisigns.com](https://support.optisigns.com)
- Related: [Connect Zoom Rooms to OptiSigns](https://support.optisigns.com/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage) · [Connect Microsoft Teams Rooms to OptiSigns](https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage)
