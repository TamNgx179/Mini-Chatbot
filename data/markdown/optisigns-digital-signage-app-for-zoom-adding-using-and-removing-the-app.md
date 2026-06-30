# OptiSigns Digital Signage App for Zoom — Adding, Using, and Removing the App

Article URL: https://support.optisigns.com/hc/en-us/articles/52523606879251-OptiSigns-Digital-Signage-App-for-Zoom-Adding-Using-and-Removing-the-App
Article ID: 52523606879251
Last Updated: 2026-06-11T22:24:43Z

## About the OptiSigns–Zoom integration

OptiSigns connects to your Zoom account at the account level, using either the OptiSigns app from the Zoom App Marketplace (admin OAuth) or a Server-to-Server OAuth app created in your own Zoom account. The integration lets OptiSigns turn idle Zoom Rooms into digital signage: it lists the Zoom Rooms on your account and uses the Digital Signage feature built into Zoom Rooms to display your OptiSigns content between meetings. No software is installed on the room device, and meetings are never affected — content clears the moment a meeting starts.

The app requests the following Zoom scopes:

- `zoom_rooms:read:list_rooms:admin` — Allows OptiSigns to list the Zoom Rooms on your account so they can appear in your OptiSigns screen fleet.
- `zoom_rooms:read:room:admin` — Allows OptiSigns to read a single room's details when refreshing it.
- `zoom_rooms:read:list_devices:admin` — Allows OptiSigns to read room hardware details (model, OS, firmware version) shown in the room's device-info panel.
- `zoom_rooms:read:room_settings:admin` — Allows OptiSigns to read a room's current digital signage settings before making any change.
- `zoom_rooms:update:room_settings:admin` — Allows OptiSigns to assign the signage URL to a room and update its signage settings (layout, mute, display period).
- `zoom_rooms:write:digital_signage_library_contents:admin` — Allows OptiSigns to create (and later remove) its signage entry in your Zoom digital signage content library.
- `zoom_rooms:update:room_control:admin` — Allows OptiSigns to restart the Zoom Rooms app on a room, only when you request it.
- `zoom_rooms:read:alert:admin` — Allows OptiSigns to read room alerts so it can show room health.
- `user:read:user:admin` — Allows OptiSigns to read the connecting admin's basic profile (name, email), used only to label the connection in OptiSigns.

OptiSigns stores: room name and ID, device model / OS / firmware, online-offline status and last-seen time, and references to the signage content it created. Credentials (OAuth tokens, or the Server App Client Secret) are encrypted at rest and are never written to logs or returned over any API.

OptiSigns never accesses meeting content, recordings, transcripts, chat, calendars, or participant data — the integration requests no meeting scopes at all.

---

## Adding the app

In OptiSigns, sign in at [app.optisigns.com](https://app.optisigns.com), then open **Room Integrations → Zoom Rooms** in the left navigation. There are two ways to connect; both use the same Zoom permissions listed above:

- **Marketplace App** — Click **Connect with Zoom**. You are redirected to the Zoom App Marketplace to review the requested scopes and approve access (you must be the Zoom Account Owner, or an Admin with Marketplace install permission). After approval, you are returned to OptiSigns and your rooms appear within a few seconds.
- **Server App** — Create a Server-to-Server OAuth app in the Zoom Marketplace with the scopes listed above, then click **Add Server App** in OptiSigns and paste the app's Account ID, Client ID, and Client Secret. OptiSigns validates the credentials and pulls your room inventory immediately.

If approval fails or you land back in OptiSigns without a successful connection, see Troubleshooting below. For a step-by-step walkthrough with screenshots, see [Connect Zoom Rooms to OptiSigns Digital Signage](https://support.optisigns.com/hc/en-us/articles/52069065128723).

---

## Using the integration

When connected, your Zoom Rooms appear in OptiSigns alongside your other screens. Rooms do not consume an OptiSigns license until you activate signage on them. For each room you activate, OptiSigns assigns a signage URL to the room through Zoom's REST API; the Zoom Rooms client then displays your assigned OptiSigns content (images, videos, playlists, schedules) whenever the room is idle, and hides it during meetings.

OptiSigns periodically syncs the room list and room status from Zoom, and pushes signage-setting changes (layout, mute, display period) that you make in OptiSigns. Regarding meetings and call content: OptiSigns does not join, store, or access the content of meetings; video meetings run entirely on Zoom, and Zoom's own terms and policies apply to them.

---

## Removing the app — in OptiSigns

From the **Room Integrations → Zoom Rooms** page, click **Disconnect** and confirm. OptiSigns then:

- Revokes the OAuth grant with Zoom's token-revoke endpoint (Marketplace install). For a Server App there is no revoke endpoint on Zoom's side — the short-lived token simply expires; you can also deactivate the app in your Zoom Marketplace to invalidate the credentials immediately.
- Attempts to remove the OptiSigns signage entry and the OptiSigns-created library content from each room (best-effort — if a room can't be reached, leftovers can be removed in the Zoom admin portal).
- Releases all OptiSigns screen licenses used by Zoom Rooms, removes the synced room records, and stops syncing.
- Deletes the locally stored, encrypted Zoom credentials.

Revocation is best-effort: a failure talking to Zoom does not block the local disconnect, so you can always unlink the app in OptiSigns.

---

## Removing the app — in the Zoom App Marketplace

You can also uninstall on Zoom's side: go to **marketplace.zoom.us → Manage → Added Apps**, find **OptiSigns**, and click **Remove**. Zoom notifies OptiSigns through the app deauthorization webhook; OptiSigns then automatically runs the same cleanup as the in-product disconnect for the matching Zoom account — revoking access, removing pushed signage, releasing licenses, and deleting stored credentials — and confirms data-deletion compliance back to Zoom, honoring the data-retention choice you make on Zoom's uninstall screen.

---

## What happens to your data after removal

- After you disconnect or deauthorize, OptiSigns revokes (where Zoom supports it) and deletes the locally stored Zoom credentials.
- The synced room inventory and the screens created for activated rooms are removed, and their licenses are released.
- Operational audit records (for example, which admin connected or disconnected the integration, and when) may be retained where needed for audit, security, and service-integrity purposes, as described in the [OptiSigns Privacy Policy](https://www.optisigns.com/privacy-policy).
- Your OptiSigns content (assets, playlists, schedules) is not affected.

If you need account-level deletion or data access requests, contact [support@optisigns.com](mailto:support@optisigns.com).

---

## Troubleshooting

- **OAuth errors during connect:** confirm you approved the app in Zoom as the Account Owner (or an Admin with Marketplace install permission) and retry from the OptiSigns Zoom Rooms page. If Zoom shows "You don't have permission to install this app," ask your Zoom Account Owner to pre-approve OptiSigns at the account level.
- **Rooms don't appear after connecting:** click **Sync now** on the Zoom Rooms page. Confirm at least one Zoom Room is provisioned in your Zoom admin portal; initial sync can take up to a minute on large accounts.
- **Signage doesn't show on a room:** ensure Digital Signage is enabled for that room in the Zoom admin portal (**Account Settings → Zoom Rooms → Digital Signage**). The next OptiSigns push succeeds automatically once enabled.
- **If disconnect appears stuck:** retry from OptiSigns first; if the issue persists, contact us with what you observed (without pasting secrets).

---

## FAQ

**Which scopes does OptiSigns request?** The nine scopes listed under "About the OptiSigns–Zoom integration" above. Zoom also displays the full list on the authorization screen before you approve.

**Does OptiSigns access meetings, recordings, or chat?** No. OptiSigns requests no meeting scopes and does not store or access the audio/video content of calls. It only manages the digital signage shown while a room is idle.

**Can I reconnect after removal?** Yes. Open **Room Integrations → Zoom Rooms** in OptiSigns and complete the connection again; your rooms re-sync within seconds.

**What does OptiSigns keep after disconnect?** Zoom credentials are removed; certain operational records may be retained under the Privacy Policy as noted above.

---

## Reporting a security issue

Email [support@optisigns.com](mailto:support@optisigns.com) with the subject "Security" so we can prioritize handling.
