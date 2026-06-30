# Room Integrations: Turn Your Meeting Rooms into Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52113036672403-Room-Integrations-Turn-Your-Meeting-Rooms-into-Digital-Signage
Article ID: 52113036672403
Last Updated: 2026-06-15T19:14:16Z

![OptiSigns Room Integrations — one place to manage and push digital signage to all your meeting room systems](https://support.optisigns.com/hc/article_attachments/52113329657491)

Your meeting rooms sit idle most of the day. OptiSigns **Room Integrations** put that screen time to work: when a room is between meetings, OptiSigns plays your content — announcements, dashboards, branding, menus, or emergency messages — right on the room display, and clears it the instant a meeting starts.

No extra hardware. No app to install on the room. You connect your meeting-room platform once, and your rooms appear in OptiSigns ready to receive signage.

---

## Supported platforms

| Platform | How your content reaches the room | Setup guide |
| --- | --- | --- |
| **Zoom Rooms** | Pushed automatically over Zoom's API | [Connect Zoom Rooms to OptiSigns](https://support.optisigns.com/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage) |
| **Cisco Webex Rooms** | Pushed automatically over Webex's API | [Connect Cisco Webex Rooms to OptiSigns](https://support.optisigns.com/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage) |
| **Microsoft Teams Rooms** | Paste a signage URL (no push API) | [Connect Microsoft Teams Rooms to OptiSigns](https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage) |
| **Google Meet hardware** | Paste a signage URL (no push API) | [Connect Google Meet Hardware to OptiSigns](https://support.optisigns.com/hc/en-us/articles/52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage) |

> Zoom and Webex deliver signage fully automatically — OptiSigns publishes your content to the room over each vendor's official API. Microsoft Teams Rooms and Google Meet hardware don't offer a push API, so for those you paste an OptiSigns signage URL into the vendor's admin console once — the setup guide walks you through it.

---

## How Room Integrations work

Every platform follows the same flow — connect once, then manage all your rooms from one place.

**1. Connect your platform account.**
From the OptiSigns left navigation under **Room Integrations**, choose your platform. An admin connects OptiSigns at the organization level (via OAuth, a service account, or a pasted signage URL), so one connection covers every room on that platform. Admins, permission scopes, and syncing are handled centrally — there's no room-by-room setup.

**2. Your rooms sync into OptiSigns.**
Once connected, OptiSigns pulls in your rooms and keeps them in sync, each with its live Online / Offline status straight from the vendor. New rooms appear on the next sync, and you can click **Sync** to refresh on demand.

**3. Activate a signage license.**
Rooms start as "discovered, not yet signage." Open a room and select **Activate Signage License** to turn it into an OptiSigns screen, then configure its settings. Each activated room uses **one screen license** from your plan (see *Licensing* below).

**4. A Virtual Screen URL is generated.**
OptiSigns mints a stable, secure **Virtual Screen URL** for each activated room — your screen, delivered as a URL.

**5. The URL is pushed to the room system.**
OptiSigns pushes that URL to the room over the platform's official API, where it becomes the room's idle-screen content. (For platforms without a push API, OptiSigns generates the URL and walks you through a one-time paste in the vendor portal.)

**6. Live on the idle screen.**
When the room is idle, your assigned content plays. Updates are instant and real-time. The moment a meeting starts — or someone wakes the room — the display returns to its normal meeting UI; signage resumes automatically when the room goes idle again.

There is **no impact** on meeting quality, audio/video, screen sharing, or scheduled-meeting display.

---

## What you can put on an idle room screen

Once a room is activated it behaves like any other OptiSigns screen — assign an asset, playlist, or schedule. Common uses:

- **Announcements & news** — company updates, HR news, events, policies
- **Dashboards & KPIs** — Power BI, metrics, operational dashboards
- **Branding & culture** — values, welcome messages, internal communications
- **Emergency messaging** — critical alerts and time-sensitive instructions

---

## Licensing

A room signage license uses **one screen license** from your existing OptiSigns pool — the same licenses you use for any other screen. You only consume a license on rooms you actually activate; discovered-but-not-activated rooms are free.

To set part of your pool aside for room integrations, use **Manage** on the Connect page to reserve a number of room-integration licenses. You can change the reservation any time.

---

## What you'll need

- An **OptiSigns account** on a plan that includes Room Integrations. [Start a free trial](https://www.optisigns.com/free-trial) — you only pay for rooms you activate.
- The **Owner** or **Admin** role in OptiSigns.
- Admin access to your meeting-room platform to authorize the one-time connection.
- At least one room that's online and signed in on the platform you're connecting.

---

## Get started

Pick your platform and follow its setup guide:

- **[Connect Zoom Rooms →](https://support.optisigns.com/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage)**
- **[Connect Cisco Webex Rooms →](https://support.optisigns.com/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage)**
- **[Connect Microsoft Teams Rooms →](https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage)**
- **[Connect Google Meet Hardware →](https://support.optisigns.com/hc/en-us/articles/52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage)**

---

## Frequently asked questions

**Do I need to install anything on the room?**
No. OptiSigns uses each platform's built-in digital-signage / idle-screen feature. Nothing is installed on the room device.

**Will this interrupt meetings?**
No. Signage only appears when the room is idle. Any incoming or scheduled meeting takes over the display immediately; signage resumes when the room is idle again.

**What does the room's status mean?**
The Online / Offline status comes from the meeting-room platform itself — it reflects whether the room is reachable on the vendor's side. A room can be Online but not yet showing signage if you haven't activated a license or assigned content.

**My room isn't showing up, or its info looks stale.**
OptiSigns syncs rooms on a schedule. Click **Sync** on the platform's Connect page to refresh immediately; newly added rooms appear on the next sync.

**How is a room different from a regular screen?**
Once activated, a room *is* a regular OptiSigns screen for content purposes — you assign assets, playlists, and schedules the same way. The difference is how it's connected (through the vendor) and that it only displays while the room is idle.

**What happens if I disconnect a platform?**
Disconnecting stops syncing and removes the OptiSigns signage URL from your rooms. Rooms you already activated keep their licenses unless you remove them. You can reconnect at any time.

---

## Related articles

- [Connect Zoom Rooms to OptiSigns](https://support.optisigns.com/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage)
- [Connect Cisco Webex Rooms to OptiSigns](https://support.optisigns.com/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage)
- [Connect Microsoft Teams Rooms to OptiSigns](https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage)
- [Connect Google Meet Hardware to OptiSigns](https://support.optisigns.com/hc/en-us/articles/52412502456083-Connect-Google-Meet-Hardware-to-OptiSigns-Digital-Signage)
- [OptiSigns Help Center](https://support.optisigns.com/hc/en-us)
