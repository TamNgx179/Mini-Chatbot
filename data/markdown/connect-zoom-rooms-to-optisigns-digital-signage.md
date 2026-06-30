# Connect Zoom Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage
Article ID: 52069065128723
Last Updated: 2026-06-11T22:22:00Z

Turn idle Zoom Rooms into digital signage. When a Zoom Room is not in a meeting, OptiSigns plays your assigned content — images, videos, dashboards, web apps — between meetings, and clears it the moment a meeting starts.

This guide walks a Zoom Account Owner or Admin through the one-time setup at the account level, and then per-room signage activation.

---

## What you'll need

- A **Zoom account with the Owner or Admin role** (required to install and authorize the OptiSigns Marketplace app, or to create the Server-to-Server OAuth credentials).
- Any Zoom plan that includes **Zoom Rooms licensing**.
- An **OptiSigns account**. [Sign up for a free trial](https://app.optisigns.com) — you only pay for rooms you activate signage on.
- At least one **Zoom Room** with a recent Zoom Rooms client. OptiSigns does not filter by vendor — any Zoom Room that Zoom returns from the inventory API will appear in your fleet (Neat, Poly, Logitech, DTEN, Yealink appliances, and Zoom Rooms for Windows / macOS).

---

## How OptiSigns works on Zoom Rooms

OptiSigns uses the **Digital Signage** feature built into Zoom Rooms. There is no OptiSigns app installed on the device. Instead, OptiSigns pushes a signage URL + display schedule to each room via Zoom's REST API; the Zoom Rooms client renders that URL between meetings and hides it the moment a meeting starts.

There is **no impact on meeting quality**, screen-sharing, whiteboard, or Zoom Apps features.

---

## Step 1 — Sign in to OptiSigns

Go to [app.optisigns.com](https://app.optisigns.com) and sign in (or create your account).

---

## Step 2 — Open the Zoom Rooms page

In the left navigation under **Room Integrations**, click **Zoom Rooms**.

![Connect Zoom Rooms in the left nav](https://support.optisigns.com/hc/article_attachments/52352814423187)

---

## Step 3 — Choose a connection method

OptiSigns offers two ways to connect, side-by-side:

![Empty Zoom Rooms page showing Server App and Marketplace App cards](https://support.optisigns.com/hc/article_attachments/52352797082387)

| Method | Best for | What you do |
| --- | --- | --- |
| **Server App** | IT-led rollout / strict change control | Create a Server-to-Server OAuth app in your Zoom Marketplace, paste the Account ID + Client ID + Client Secret into OptiSigns. |
| **Marketplace App** *(recommended for most customers)* | SMB / fast onboarding | One-click install of the OptiSigns Digital Signage app from the Zoom Marketplace. |

Both methods request the same Zoom permissions:

- **Read Zoom Rooms inventory** — to list your rooms
- **Push signage URLs** — to assign content to a room
- **Read room events** — to know when a room is idle vs. in a meeting

> Under the hood these map to Zoom's 2024 granular scope taxonomy (`zoom_rooms:read:list_rooms:admin`, `zoom_rooms:update:room_settings:admin`, `zoom_rooms:read:digital_signage_library_contents:admin`, etc.). The exact scope list is shown by Zoom on the install screen.

### Option A — Marketplace App (one-click)

1. Click **Connect with Zoom** on the Marketplace card.
2. A new tab opens at **marketplace.zoom.us** with the OptiSigns Digital Signage app install screen.
3. Review the requested scopes and click **Authorize** (or **Allow**). You must be signed in as the Account Owner, or an Admin with **Manage Marketplace Apps** privilege.
4. You'll be redirected back to OptiSigns automatically — your rooms appear in the list within a few seconds.

> If you see **"You don't have permission to install this app,"** ask your Zoom Account Owner to pre-approve OptiSigns at the account level (Marketplace Manage Permissions), or to grant you the right role.

### Option B — Server App (Server-to-Server OAuth)

1. In the Zoom Marketplace, **Build App Server-to-Server OAuth**.
2. Add the scopes shown on the card above and activate the app.
3. Click **Add Server App** on the OptiSigns card and paste your **Account ID**, **Client ID**, and **Client Secret**.
4. OptiSigns will validate the credentials and pull your room inventory immediately.

---

## Step 4 — Confirm the connection

Once connected, the status bar shows the account email and the room count. From here you can refresh the inventory or disconnect.

![Connected status bar showing Sync now and Disconnect](https://support.optisigns.com/hc/article_attachments/52352814631315)

- **Sync now** — re-fetch rooms from Zoom (rooms also sync automatically on a schedule).
- **Disconnect** — see [Disconnecting OptiSigns](#disconnecting-optisigns).

Your Zoom Rooms now appear in the device table alongside any Android, ChromeOS, Linux, or Webex devices on your account.

---

## Step 5 — Activate signage on a room

By default rooms are listed but **not activated** — they don't consume an OptiSigns license until you turn signage on. Activation is per-room.

1. Click any room in the table to open its detail drawer.
2. Click **Activate Signage License**.

![Room drawer with Activate Signage License button and Zoom Settings card](https://support.optisigns.com/hc/article_attachments/52353026119443)

The drawer also shows the room's **Health**, recent **Commands**, **Device info** (Model, OS, Platform, Paired date), and the **Zoom Settings** card.

---

## Step 6 — Assign content

Once the room is activated, content is assigned the same way as any other OptiSigns screen:

1. From the room drawer, click **Assign Content** (or **Change Content** if content is already assigned).
2. Pick an Asset, Playlist, or Schedule.
3. Save.

Within **10–30 seconds**, your content will appear on the Zoom Room between meetings. Start a test call — content clears the instant the meeting connects, and reappears when the room becomes idle.

---

## Configure Zoom Settings (optional)

The **Zoom Settings** card in the room drawer exposes the signage behavior that OptiSigns pushes to the device:

| Setting | What it does | Notes |
| --- | --- | --- |
| **Mode** | Layout used by the Zoom Rooms digital signage renderer | Defaults to the standard content-only layout. The HDMI layout is intentionally not exposed (Zoom rejects it over REST). |
| **Display Period** | Two minute offsets that control when signage shows: **start displaying N min after a meeting ends** and **stop displaying N min before the next meeting**. | Toggle off to show signage whenever the room is idle. |
| **Mute** | Mute audio on the signage playback. | On by default — recommended for meeting rooms. |
| **Enable** | Master toggle for the signage feature on this room. | Turn off temporarily without releasing the OptiSigns license. |

Changes apply within **~10 seconds** via Zoom's REST API.

---

## Disconnecting OptiSigns

1. From the OptiSigns Zoom Rooms page, click **Disconnect** on the status bar.
2. Confirm in the dialog:

![Disconnect Zoom confirmation dialog](https://support.optisigns.com/hc/article_attachments/52352754968339)

Disconnecting releases all OptiSigns screen licenses currently consumed by Zoom Rooms and stops syncing rooms from Zoom.

> **Heads-up:** Disconnecting from OptiSigns does **NOT** remove any signage URL already pushed to your Zoom Rooms. To clear content from a room, push an empty signage URL before disconnecting, or remove it manually from the Zoom admin portal.

3. (Optional, for Marketplace install) To fully revoke OptiSigns' Zoom access token, go to **marketplace.zoom.us Manage Added Apps OptiSigns Digital Signage Remove**.

---

## Troubleshooting

**My rooms don't appear after connecting.**
Click **Sync now** on the status bar. If the table is still empty, confirm at least one Zoom Room is provisioned and recently online in your Zoom admin portal. Initial sync can take up to a minute on large accounts.

**The room drawer shows "Could not load settings" in the Zoom Settings card.**
The room has not returned settings to Zoom yet (most common when the room appliance is offline or has been recently reset). Wait until the room is online (Health = active), click **Sync now**, then reopen the drawer.

**Content shows but doesn't clear when a meeting starts.**
Check the **Display Period** toggle in the Zoom Settings card — if it's on with a very small "stop displaying ... before meeting" offset, content can hang on for a few seconds. Either lower the start offset or disable Display Period to use Zoom's default behavior.

**"You don't have permission to install this app" on the Zoom Marketplace.**
You're not signed in as the Account Owner or an Admin with Marketplace install permission. Ask your Zoom account owner to pre-approve OptiSigns at the account level, or to grant your account the appropriate role.

**A specific room shows "Digital Signage not enabled."**
Open the room in the Zoom admin portal **Account Settings Zoom Rooms Digital Signage** ensure Digital Signage is enabled at the account, location, or room level. The next OptiSigns push will succeed automatically.

**Where does OptiSigns store the credentials?**
The Marketplace OAuth token (or the Server App Client Secret) is encrypted at rest with an account-scoped key. They are never written to logs or returned over the API.

---

## Pricing

OptiSigns Zoom Rooms integration uses a screen license, same as any other device on your account. Free trial available — you're only billed once you activate signage on a room. [See full pricing](https://www.optisigns.com/pricing)

---

## Need help?

- **Email:** support@optisigns.com
- **More guides:** [support.optisigns.com](https://support.optisigns.com)

---

## Related documentation

For full details on the Zoom permissions (scopes) OptiSigns uses, how to add or remove the app, and what happens to your data after removal, see [OptiSigns Digital Signage App for Zoom — Adding, Using, and Removing the App](https://support.optisigns.com/hc/en-us/articles/52523606879251).
