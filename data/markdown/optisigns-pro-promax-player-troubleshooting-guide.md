# OptiSigns Pro/ProMax Player Troubleshooting Guide

Article URL: https://support.optisigns.com/hc/en-us/articles/40736654972563-OptiSigns-Pro-ProMax-Player-Troubleshooting-Guide
Article ID: 40736654972563
Last Updated: 2026-01-13T21:20:16Z

### In this article, we troubleshoot the most common issues our customers face when using an OptiSigns Pro or ProMax Player.

- [Best Practices](#BestPractices)
- [The Troubleshooting Option](#TroubleshootingOption)
- [Hardware Troubleshooting](#Hardware)
  - [Network Troubleshooting](#Network)
  - [Power, HDMI & TV Connection Troubleshooting](#Connection)
  - [Blank Screen Troubleshooting](#BlankScreen)
  - [Fixing the OnHold Warning](#OnHold)
  - [App Freezes, Video Assets not Playing full video or Asset Not Loaded Fully](#AppFreezes)
  - [How to Factory Reset the OptiSigns Pro/ProMax Player](#FactoryReset)
- [Security Settings Troubleshooting](#SecuritySettings)
  - [Using the Device Log](#DeviceLog)
  - [Static IP](#StaticIP)
  - [Internal Websites and Root Certificates](#InternalWebsite)
- [Pro/ProMax Player RMA Process](#RMAProcess)

If you’ve got an OptiSigns Pro or ProMax Player and you’re having issues, you’ve come to the right place. For first time setup, see our [**Set Up the OptiSigns Pro Player**](https://support.optisigns.com/hc/en-us/articles/32272215514131-Optisigns-Pro-Digital-Signage-Player) or [**Set Up the OptiSigns ProMax Player**](https://support.optisigns.com/hc/en-us/articles/38680194603155-OptiSigns-ProMax-Player) articles. For more on the Pro or ProMax player features, see our [**Advanced Features**](https://support.optisigns.com/hc/en-us/articles/35577511423635-OptiSigns-Pro-Player-Advanced-Features) article.

---

## Best Practices

- Set up the [**Mobile Admin App**](https://support.optisigns.com/hc/en-us/articles/30003143806099-How-to-Use-the-OptiSigns-Mobile-Admin-App). This will allow you to use numerous features remotely, including the Remote Keyboard app and remote monitoring.
- Keep the player in an indoor, air conditioned environment
- Ensure your player is up-to-date. We release frequent OTA updates - see more below.

By default, our Pro Players are set to receive a weekly automatic OTA update at **Sunday 00:00** (also known as Saturday night). If the players are offline at that time, it’s possible to miss the OTA update. We recommend changing the OTA update to a time when the players are online, but not being used for anything mission critical.

These OTA updates often bring with them new and advanced features, stability updates, security updates, patches, and more, so we ***highly recommend*** scheduling an update time that works for you. If none do, be sure to occasionally **Check for Updates**.

---

## The Troubleshooting Option

Your first stop when running into a problem with the OptiSigns Pro or ProMax player should be the **Troubleshooting** page. This is an option on the Side Menu:

![troubleshooting page menu location](https://support.optisigns.com/hc/article_attachments/40736654908563)

Choosing this option will open the Troubleshooting screen:

![troubleshooting screen](https://support.optisigns.com/hc/article_attachments/40736654909587)

- **Check Internet Connection**: Verifies whether the device has an active internet connection.
- **Check Connection to API Services**: Tests the device's connection to OptiSigns services, including APIs and MDMs.
  - **Note**: If this check fails, it may be due to a firewall blocking the connection. Refer to our [**Whitelist Article**](https://support.optisigns.com/hc/en-us/articles/360047275934) for the required URLs and ports.
- **Check File Downloading**: Confirms the status of downloadable files (e.g., images, videos) being downloaded to the device.
- **Network Information**: Displays the current network the device is connected to.
  - **WiFi/Ethernet Details**: Includes IP Address, SSID, Signal Strength, Channel, Connection Type, and MAC Address.
- **Device Information:**
  - Screen Name, Pairing Code, Screen Resolution, OptiSigns App Version, OptiSigns MDM App Version, OS Version, Manufacturer, Model, Serial Number
  - Heartbeat/Polling Interval: Indicates how frequently the device communicates with OptiSigns servers and the last received signal.
- **Running Time**: Shows how long the OptiSigns app has been running on the device.
- **Storage**: Displays used and total storage capacity.
- **Memory**: Displays used and total memory capacity.
- **Current System Time**: Shows the current system time on the device.
- **System Time Zone**: Displays the time zone configured on the device.
- **Assigned Content Type**: Indicates the type of content the device is playing (e.g., Asset, Playlist, Schedule).
- **Assigned Content Name**: Provides the name of the content being displayed.
- **Device Created Date**: Displays the date the device was activated.
- **Operational Schedule Assigned**: Shows whether an operational schedule is assigned (**Y/N**).
- **Mute Status**: Displays the current audio status of the device.
- **Heavy Content Status**: Indicates whether the device is handling heavy content (e.g., 4+ zones or SplitScreen with 4K video) (**Y/N**)

---

## Hardware Troubleshooting

Here we will cover the most common hardware troubleshooting issues our support team encounters with our OptiSigns Pro and ProMax players. Following these steps will resolve 90%+ of issues.

### Network Troubleshooting

This is, by far, the most common issue people encounter. Devices experiencing network issues typically appear “Offline” in the OptiSigns portal, even when they are powered on and have content assigned to them.

![optisigns screen offline](https://support.optisigns.com/hc/article_attachments/40736654910739)

The first stop should be the [**Troubleshooting Page**](#TroubleshootingOption). The upper left box details network status. If all the text is green, this means there are no network issues. Any red text will require further troubleshooting.

To identify and resolve network issues:

- Create a mobile hotspot, then have your Pro or ProMax player connect with it. A successful connection indicates a problem with your general Wi-Fi connection.
- Try a different network. You may need to move the device to get connected. A successful connection indicates a problem with your general Wi-Fi connection.
- If you have firewalls, make sure OptiSigns is whitelisted. Refer to our [**Whitelist Article**](https://support.optisigns.com/hc/en-us/articles/360047275934) for the required URLs and ports.
- Plug in an Ethernet cable to see if it can still connect.
- After trying to connect with these methods, [**Factory Reset**](#FactoryReset) the device, then perform initial setup again.
- If the device still cannot connect to any network, [**contact our support team**](https://support.optisigns.com/hc/en-us/articles/35626165056787-How-to-Contact-OptiSigns-Support). After a bit of troubleshooting, you may be asked to submit an [**RMA request**](#RMAProcess)**.**

### Power Cable, HDMI & TV Connection Troubleshooting

- Ensure device is powered on and the LED light on the power button is on
- Try a different HDMI/DP port on your TV
- Try a different TV or monitor

### Blank Screen Troubleshooting

If your device and screen are on, but only displays a black screen:

- Network issues, **see above**.
- Check to make sure there is a Playlist or Asset assigned to your screen.
- Make sure your Timezones and Schedules match, including your Operational Schedule and normal schedule.
- Check your firewall settings, and ensure you’ve [**Whitelisted OptiSigns IP addresses and ports**](https://support.optisigns.com/hc/en-us/articles/360047275934-Whitelist-OptiSigns-IP-addresses-ports).
- Check your Operational Schedule, and verify its power settings are not set to Off. If an Operation Schedule’s power settings are set to Off, it will remain off during the designed time.

If the device is still not displaying content after you’ve checked these try a [**Factory Reset**](#FactoryReset).

### Fixing the OnHold Warning

![OnHold warning](https://support.optisigns.com/hc/article_attachments/40736684864403)

This warning displays when the device is in the [**OnHold Folder**](https://support.optisigns.com/hc/en-us/articles/1500003244381-About-the-OnHold-Devices-Folder). This happens when you’ve ordered more devices than you had licenses for. Any devices above your license limit will automatically be placed in the OnHold folder and will need to be removed, even when the license limit has been raised.

### App Freezes, Video Assets not Playing full video or Asset Not Loaded Fully

To handle any of these issues, hit the **Refresh & Relaunch** option of the OptiSigns Player, then reboot. You may need to Factory Reset if the problem persists.

### How to Factory Reset an OptiSigns Pro or ProMax Player

Sometimes, it might be necessary to perform a factory reset on your OptiSigns Pro Player.

To do this, attach a keyboard to the Player. Then, **Reboot** it. As it restarts, rapidly tap the **↑ arrow** (the **End** key may also work). It will boot into this screen:

![optisigns pro player boot screen](https://support.optisigns.com/hc/article_attachments/40736654916499)

Here, you have several additional options. Hit **Factory Reset**. You’ll receive this prompt:

![factory reset password screen](https://support.optisigns.com/hc/article_attachments/40736654917395)

You’ll need to enter your **admin password.**

Once entered, you’ll see a screen like this:

![factory reset in progress](https://support.optisigns.com/hc/article_attachments/40736684873363)

Afterwards, your factory defaults will be restored.

---

## Security Settings and Advanced Feature Troubleshooting

The Pro and ProMax Players offer advanced security settings and features that are indispensable for an enterprise environment. Below are the most common and helpful suggestions we have when trying to enable some of these more advanced settings.

See our [**Pro/Pro Max Player Advanced Features**](https://support.optisigns.com/hc/en-us/articles/35577511423635-OptiSigns-Pro-Player-Advanced-Features) article for information on setting these up.

### Using the Device Log

There are two ways to use the **Device Log** feature:

1. By plugging in an external device to the player, then hitting the **Device Log** button on the **About** menu. This will bring up a box letting you know the log has been exported to the external device:

![device log export confirmation](https://support.optisigns.com/hc/article_attachments/40736654921235)

2. By using the ***collectDeviceLog*** [**Remote Command**](https://support.optisigns.com/hc/en-us/articles/4408658251027-How-to-use-Remote-Command-Execution-Windows-Linux) from the OptiSigns portal. This will provide a download link that you can use to obtain the log:

![execute remote command device log](https://support.optisigns.com/hc/article_attachments/40736684875283)

This can be extremely helpful for troubleshooting any issues that might have occurred when the device was not being closely monitored.

### Static IP

When setting up a Static IP, make sure you’ve selected the appropriate static IP setting, depending on whether you’re using a WLAN or Ethernet connection.

![static IP wlanip vs ethip](https://support.optisigns.com/hc/article_attachments/40736684876691)

Next, ensure you’ve input the correct information in the IP Address, Default Gateway, Subnet Mask, and DNS Server fields.

![static ip options](https://support.optisigns.com/hc/article_attachments/40736654945427)

See our [**Advanced Settings for the Pro/ProMax Player**](https://support.optisigns.com/hc/en-us/articles/35577511423635-OptiSigns-Pro-Player-Advanced-Features) article for more information.

### Internal Website and Certificates

For installation on a Gen 3 Pro or ProMax Player, your certificate must have a **.crt** extension. However, it is important that this certificate is signed and contains your public key. These are usually generated as **.pem** files. You’ll need to rename your certificate (.pem) file and change its extension to **.crt** for your internal website to properly display.

![certificate file option](https://support.optisigns.com/hc/article_attachments/40736684879635)

See our article on [**how to install a root certificate and set up your internal website display**](https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens) for more information.

---

## Pro/ProMax Player RMA Process

Please try to go through the above common troubleshooting steps before submitting an RMA request.

Devices will be tested in the RMA process. If they work normally, the customer will be charged a restocking fee.

Our RMA process is as follows:

- Device is eligible for RMA only if it is still within the 12-month warranty period.
- Fill out [**this RMA form**](https://share.hsforms.com/1cTorC26VQqGd-bF-zyzsTwca5m5) (with proof of purchase in the last 12 months).
- RMA request is reviewed within 3 business days.
- New device ships within 3-5 business days to most places in the U.S.
- Return the old device within 30 days.

### That's all!

If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
