# Connect Microsoft Teams Rooms to OptiSigns Digital Signage

Article URL: https://support.optisigns.com/hc/en-us/articles/52350277262483-Connect-Microsoft-Teams-Rooms-to-OptiSigns-Digital-Signage
Article ID: 52350277262483
Last Updated: 2026-06-24T18:39:16Z

Turn idle Microsoft Teams Rooms into digital signage. When a room is between meetings, OptiSigns plays your assigned content — announcements, dashboards, branding, menus — right on the room display, and clears it the instant a meeting starts.

This guide covers the **two ways to connect a Teams Room to OptiSigns**, so you can pick the one that fits how your organization works.

---

## Two ways to connect

|  | **Signage URL**  ·  *Recommended, fastest start* | **Service Principal** |
| --- | --- | --- |
| **What it gives you** | Get content on a room in minutes — no app registration. | OptiSigns **discovers and lists all your Teams Rooms** (model, online/offline, health) in one place. |
| **Microsoft setup** | None in Azure. You paste a URL in the Teams Rooms portal. | An Entra admin registers a read-only app and grants two permissions. |
| **Best for** | Getting started, a few rooms, or when you can't register an Azure app. | Managing a fleet of rooms and seeing their status alongside your other screens. |
| **Who can set it up** | A Teams Rooms admin. | A Microsoft **Entra (Azure AD) admin**, one time. |

> **Important — read this first.** Microsoft does **not** offer a way for apps to push content to Teams Rooms automatically. So with **either** method, the final step is a **one-time manual paste** of an OptiSigns signage URL into the Teams Rooms portal. The **Service Principal** method doesn't push content for you — it gives OptiSigns *visibility* into your rooms. Many teams use **both**: Service Principal to see every room, and Signage URLs to deliver the content.

---

## What you'll need

- **An OptiSigns account** on a plan that includes device management (MDM / room integrations), with the **Owner** or **Super Admin** role. [Start a free trial](https://www.optisigns.com/free-trial) — you only pay for rooms you activate signage on.
- **Microsoft Teams Rooms Pro.** Digital signage is a **Teams Rooms Pro** capability — rooms on Teams Rooms **Basic** can't display signage.
- At least one **Teams Room that's online and signed in**.
- **For the Service Principal method only:** a Microsoft **Entra (Azure AD) Global Administrator** who can register an app and grant admin consent.

---

## How it works

OptiSigns generates a secure **signage URL** for each screen you want to show on a room. Microsoft's Teams Rooms Pro platform has a built-in **Digital signage** feature that can display a custom URL while the room is idle. You paste the OptiSigns URL there once; from then on the room plays whatever you assign in OptiSigns, and updates are live.

When a meeting starts — or someone wakes the room — the display returns to the normal Teams Rooms UI automatically, and signage resumes when the room goes idle again. There's no impact on meeting quality, audio/video, or scheduled meetings.

---

## Open the Teams Rooms page

In OptiSigns, open **Devices** in the top navigation, then in the left sidebar under **Room Integrations**, click **Teams Rooms**. If you haven't connected yet, you'll see the two methods side by side.

![OptiSigns Teams Rooms — the two ways to connect: Signage URL (recommended) and Service Principal](https://support.optisigns.com/hc/article_attachments/52411707887891)

Pick your method below.

---

# Method 1 — Connect with a Signage URL (recommended)

No Azure setup. You'll mint a URL in OptiSigns, give it content, and paste it into the Teams Rooms portal.

### Step 1 — Mint a Signage URL

On the **Signage URL** card, click **Mint URLs** (shown above).

In the **New Signage URL** dialog, give the URL a **Name** (for example, your room or location — `Atlanta Lobby`). The optional **Target label** is just a note to help you remember where you'll paste it; it doesn't control anything. Click **Next**.

![The New Signage URL dialog — name the URL, then click Next](https://support.optisigns.com/hc/article_attachments/52411718641811)

### Step 2 — Assign content

Clicking **Next** creates the URL and opens the **Signage URLs** tab (the page now shows **Connected · Signage URLs only**). On the new row, click **+ Assign content**.

In the **Assign content** dialog, choose a **Content Type** — **Asset**, **Playlist**, or **Schedule** — then pick the specific item to play. Click **Save**.

![The Assign content dialog — pick a Content Type, choose the item, then Save](https://support.optisigns.com/hc/article_attachments/52411676905875)

OptiSigns copies the new signage URL to your clipboard and shows the paste instructions. (You can reopen them any time with **Show me how to paste** on the Signage URLs tab.)

### Step 3 — Paste the URL into the Teams Rooms portal

In the **Paste your Signage URL in Teams Rooms portal** dialog, click **Open Teams Admin Portal**. Then, in Microsoft's portal:

1. Sign in and open **Digital signage**.
2. Click **Add source** and give it a clear name (matching your room or group).
3. Choose **Custom URL**, paste the OptiSigns URL, then **Review → Finish**.
4. Select the new source → **Assign to devices** → pick your Teams Room(s) → **Apply**.

![The paste-instructions dialog — copy the URL, then click Open Teams Admin Portal](https://support.optisigns.com/hc/article_attachments/52411723276051)

Within about 30 seconds the room fetches the URL and your content appears during idle. Start a test meeting — content should clear instantly when the meeting connects.

> Repeat Steps 1–3 to mint a URL for each room or room group. You manage all minted URLs (and reassign their content any time) under the **Signage URLs** tab.

---

# Method 2 — Connect with a Service Principal

This connects a **read-only** Microsoft Entra app so OptiSigns can discover and list all your Teams Rooms automatically. (You'll still deliver content with a signage URL — see "Put content on a room" below.)

### Step 1 — Register an app in Microsoft Entra

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a **Global Administrator**.
2. Go to **Identity → Applications → App registrations → + New registration**.
3. **Name** it (for example, `OptiSigns Teams Rooms`), choose **single tenant**, and leave **Redirect URI** blank. Click **Register**.
4. On the app's **Overview** page, copy the **Application (client) ID** and **Directory (tenant) ID** — you'll paste these into OptiSigns.

### Step 2 — Grant the Microsoft Graph permissions

1. In the app, open **API permissions → + Add a permission → Microsoft Graph → Application permissions**.
2. Add the two read-only scopes OptiSigns requires: **`TeamworkDevice.Read.All`** (reads your Teams Rooms inventory) and **`TeamworkAppSettings.Read.All`** (reads device health — online/offline, peripheral issues). Tip: click **Copy all scopes** on the OptiSigns setup screen and paste them straight into the Entra picker.
3. Click **Grant admin consent for <your tenant>**. Both should show **Granted**.

![OptiSigns Service Principal setup steps and the two required read-only Graph scopes — use Copy all scopes](https://support.optisigns.com/hc/article_attachments/52411718955411)

### Step 3 — Create a client secret

1. In the app, open **Certificates & secrets → Client secrets → + New client secret**.
2. Give it a description and an expiry, then **Add**.
3. **Copy the secret Value immediately** — Microsoft only shows it once. If you navigate away you'll have to create a new one.

### Step 4 — Connect in OptiSigns

Back on the OptiSigns **Teams Rooms** page, on the **Service Principal** card, click **Add Service Principal**. Paste:

- **Name** — any label (for example, `Contoso Teams SP`)
- **Application (client) ID** — from Step 1
- **Directory (tenant) ID** — from Step 1
- **Client Secret** — from Step 3

Click **Test Connection**. OptiSigns validates the credentials against Microsoft Graph and shows your tenant name on success — then **Save** lights up. Click **Save**.

![The Add Service Principal dialog — fill the four fields, then Test Connection before Save](https://support.optisigns.com/hc/article_attachments/52411702980627)

Within a few minutes your Teams Rooms appear in the **Devices** tab, each with its model and live online/offline status.

*[Screenshot to add: the connected **Devices** tab showing "Connected · <tenant> · N rooms synced" and the synced room list — captured once a Microsoft tenant with Teams Rooms is connected.]*

### Put content on a room

Discovering rooms doesn't put content on them — that still uses a signage URL. From the **Signage URLs** tab, click **New Signage URL** and follow **Method 1, Steps 1–3** above to mint a URL, assign content, and paste it into the Teams Rooms portal for that room.

---

## Licensing

Activating signage on a Teams Room uses **one screen license** from your OptiSigns pool — the same licenses you use for any other screen. Discovered rooms that you haven't activated are free; you're only billed for rooms you turn signage on for. [See full pricing →](https://www.optisigns.com/pricing)

---

## Troubleshooting

**"Test Connection" fails with "Invalid client credentials."** Re-check the Application (client) ID, Directory (tenant) ID, and Client Secret — copy them exactly from the Entra app. If the secret has expired, create a new one in **Certificates & secrets** and paste the new value.

**"Test Connection" fails with a permissions error.** You haven't granted admin consent. In Entra, open the app's **API permissions**, confirm the two Microsoft Graph scopes show **Granted for <tenant>**, then click **Grant admin consent**. Consent changes take about a minute.

**My rooms don't appear after saving the Service Principal.** The first inventory sync can take a few minutes. Click **Sync now** on the Teams Rooms page to refresh. Confirm the app has `TeamworkDevice.Read.All` with admin consent.

**I pasted the URL but nothing shows on the room.** Confirm the room is **online** and licensed for **Teams Rooms Pro** (Basic doesn't include digital signage). Make sure you pasted the full URL (it begins with `https://`) as a **Custom URL** source, and that the source is **assigned to that device** in the Teams Rooms portal.

**Content shows but doesn't clear when a meeting starts.** This is controlled by the Teams Rooms digital-signage setting in Microsoft's portal — confirm signage is set to display only while the room is idle.

**The Teams Rooms portal says the URL is invalid.** The URL may have been truncated on copy. Return to the OptiSigns **Signage URLs** tab, click **Copy** on that URL again, and re-paste.

---

## Need help?

- Email: [support@optisigns.com](mailto:support@optisigns.com)
- More guides: [support.optisigns.com](https://support.optisigns.com)
- Related: [Connect Zoom Rooms to OptiSigns](https://support.optisigns.com/hc/en-us/articles/52069065128723-Connect-Zoom-Rooms-to-OptiSigns-Digital-Signage) · [Connect Cisco Webex Rooms to OptiSigns](https://support.optisigns.com/hc/en-us/articles/51343184586643-Connect-Cisco-Webex-Rooms-to-OptiSigns-Digital-Signage)
