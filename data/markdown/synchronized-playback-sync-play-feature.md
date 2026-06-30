# Synchronized playback (Sync Play) feature

Article URL: https://support.optisigns.com/hc/en-us/articles/4412065189267-Synchronized-playback-Sync-Play-feature
Article ID: 4412065189267
Last Updated: 2026-06-10T19:08:01Z

With OptiSigns you can enable screens to play in-sync. This means:

- If content published screens are **the same**, all screens will play the content at the same time.
- If content published screens are **different**, it will start playing them from the beginning

Supported on: Android, Fire TV, Windows, Linux, MacOS, ChromeOS, Webplayer

Note:

- When Sync Play enabled, playlists may not start from the beginning (because they are synced).
- When Sync Play is enabled, subplaylist control features will no longer apply.
- Devices do not need to be on the same network, nor there's any special configuration needed on devices.
- Devices time need to be updated, and devices needs to be in the same time zone.
- Android, Fire TV requires updates to 5.13.7 or newer.
- Windows, Linux, MacOS, ChromeOS, and Webplayer don't have the timer server setting yet.

To use the Sync Play feature, just select the screens you want to enable this feature for.

### 1. Click **Edit** -> **Advanced** -> check **Sync Play**

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4412061147539)

### 2. Open the side menu of the OptiSigns app on your screen. Go to the Sync Play Timeserver.

#### 

2-1. Set 1 device to **Server** in the Sync Play Timeserver.

**![](https://support.optisigns.com/hc/article_attachments/15528184732691)**2-2. Set other devices to **Default**

![](https://support.optisigns.com/hc/article_attachments/15528056933779)

Or **Client**. Make sure all other devices connect to the same IP Server.

![](https://support.optisigns.com/hc/article_attachments/15528219929747)

Another option: If you cannot find any server, you can set all devices to Google NTP.

![](https://support.optisigns.com/hc/article_attachments/15528222917779)

### That's it. All screens will sync up.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at[support@optisigns.com](mailto:support@optisigns.com)
