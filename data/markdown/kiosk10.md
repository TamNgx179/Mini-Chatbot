# Kiosk10

Article URL: https://support.optisigns.com/hc/en-us/articles/44652521310099-Kiosk10
Article ID: 44652521310099
Last Updated: 2026-05-28T16:41:17Z

![5(2).png](https://support.optisigns.com/hc/article_attachments/44668581927443)

### This guide will walk you through setting up the OptiKiosk 10 Countertop Digital Signage Kiosk and getting started with OptiSigns.

- [What’s in the Box](#WhatintheBox)
- [Setting Up the OptiKiosk 10](#SettingUp)
  - [Step 1: Unboxing and Assembly](#Step1)
  - [Step 2: Connect to the Internet](#Step2)
  - [Step 3: Pair Kiosk to OptiSigns](#Step3)
- [Troubleshooting](#Troubleshooting)
  - [Hardware Troubleshooting](#HardwareTroubleshooting)
    - [Network Troubleshooting](#NetworkTroubleshooting)
    - [Blank Screen Troubleshooting](#BlankScreenTroubleshooting)
    - [App Freezes, Video Assets Not Playing Full Video, or Asset Not Loaded Fully](#FreezesEtAll)
    - [Performing a Factory Reset](#FactoryReset)
- [Safety and Compliance](#Safety)

A compact and portable interactive display, the OptiKiosk 10 is designed for lobbies, retail spaces, and high-traffic areas.

|  |
| --- |
| **NOTE** |
| Your kiosk includes a printed quick start guide for basic setup. This page provides detailed instructions and troubleshooting tips. |

---

## What’s in the Box

Each OptiKiosk 32 includes:

- OptiKiosk 32 device
- Power cord & adapter
- Stand assembly kit\*
- Quick start guide

\* Only with Stand and Battery models

---

## Setting Up the OptiKiosk 10

To set up the OptiKiosk 10, no additional tools are necessary. Just follow the following steps and it will be up and running.

### Step 1: Unboxing & Assembly

Place the OptiKiosk 10 on a flat surface and connect the power adapter to the device and a standard power outlet. The device should turn on automatically once connected to power. If it remains off, press and hold the power button (⏻) on the back of the device for 2–5 seconds to turn on.

### Step 2: Connect to the Internet

Your kiosk must be connected to the internet to display content.

![](https://support.optisigns.com/hc/article_attachments/44668980784019)

Connect using either of the following methods:

**Method 1: Connect via WiFi Settings**

1. On the Welcome Screen, tap anywhere to open the WiFi setup. Or, open the **Settings app** → **Network & Internet** → **Internet**.
2. Select your WiFi network and enter your password.

**Method 2: Connect using the OptiSigns Admin App**

1. On the Welcome Screen, follow the instructions to download the OptiSigns Admin App.
2. Use the app to configure WiFi on the kiosk.

Optional: Confirm Your Connection

- Open the OptiSigns app (pre-installed on the kiosk).
- Swipe right from the left edge of the screen to open the side menu.
- Select Troubleshooting and check the network connection status.

### Step 3: Pair Your Kiosk with OptiSigns

|  |
| --- |
| **IMPORTANT NOTE** |
| In order to use the OptiKiosk, you will need an [**OptiSigns subscription**](https://www.optisigns.com/pricing). To use it as a display, you can use any plan. To use it in Kiosk mode, you’ll need our [**Engage plan**](https://support.optisigns.com/hc/en-us/articles/23565267463315-Engage-Plan-FAQs). |

1. After connecting to the internet, the device will generate a pairing code like below. 

   ![](https://support.optisigns.com/hc/article_attachments/44668980788627)

   Either scan the QR code, or log in to the [**OptiSigns Portal**](https://app.optisigns.com/) and click on **Add Screen** to pair the device. For more details, refer to our article on **Setting Up and Adding Screens**. An OptiKiosk 10 functions as a single screen under your OptiSigns subscription.
2. Assign Content - To assign content, click **ASSIGNED.** If no content is assigned, it will say "Stop Playing".  
   **![how to assign content](https://support.optisigns.com/hc/article_attachments/44652492406163)**
3. Click the **Content Type** drop down list and choose between **Asset**, **Playlist,** or **Schedule**, depending on what you wish to display. If you haven't created any Assets or Playlists yet, you can use one of the default assets or simple playlists that were automatically created with your OptiSigns account.  
   ![edit screen assign content](https://support.optisigns.com/hc/article_attachments/44652492406547)  
   From here, you can **Preview** your content. To push it to your OptiKiosk, hit **Save**.

**That's all!** Congratulations, you have set up your OptiKiosk 10.

---

## **Troubleshooting**

Your first stop when running into a problem with the OptiKiosk should be the **Troubleshooting Page**. This is an option on the side menu.

To access it, swipe right on the left edge of your screen to open the side menu of the OptiSigns app. Navigate to **Troubleshooting** under the **Advanced Options** section.

![troubleshooting side menu how to access](https://support.optisigns.com/hc/article_attachments/44652492407187)

Now you can view detailed information about the app’s status and connectivity to assist with troubleshooting.

![optisigns troubleshooting screen information](https://support.optisigns.com/hc/article_attachments/44652521299731)

- **Check Internet Connection**: Verifies whether the device has an active internet connection.
- **Check Connection to API Services**: Tests the device's connection to OptiSigns services.
  - Note: If this check fails, it may be due to a firewall blocking the connection. Refer to our [Whitelist Article](https://support.optisigns.com/hc/en-us/articles/360047275934) for the required URLs and ports.
- **Check File Downloading**: Confirms the status of downloadable files (e.g., images, videos) being downloaded to the device.
- **Network Information**: Displays the current network the device is connected to.
  - WiFi/Ethernet Details: Includes IP Address, SSID, Signal Strength, Channel, Connection Type, and MAC Address.
- **Device Information:**
  - Screen Name, Pairing Code, Screen Resolution, OptiSigns App Version, OptiSigns MDM App Version, OS Version, Manufacturer, Model, Serial Number
  - Heartbeat/Polling Interval: Indicates how frequently the device communicates with OptiSigns servers and the last received signal.
- **Running Time:** Shows how long the OptiSigns app has been running on the device.
- **Storage:** Displays used and total storage capacity.
- **Memory:** Displays used and total memory capacity.
- **System Time:** Shows the current system time on the device.
- **System Time Zone:** Displays the time zone configured on the device.
- **Assigned Content Type:** Indicates the type of content the device is playing (e.g., Asset, Playlist, Schedule).
- **Assigned Content Name:** Provides the name of the content being displayed.
- **Device Created Date:** Displays the date the device was activated.
- **Operational Schedule Assigned:** Shows whether an operational schedule is assigned (Y/N).
- **Mute Status:** Displays the current audio status of the device.
- **Heavy Content Status:** Indicates whether the device is handling heavy content (e.g., 4+ zones or SplitScreen with 4K video) (Y/N). This will usually result in lag.

### **Hardware Troubleshooting**

Here, we will cover the most common hardware troubleshooting issues our support team encounters.

#### **Network Troubleshooting**

This is, by far, the most common issue people encounter. Devices experiencing network issues typically appear “Offline” in the OptiSigns portal, even when they are powered on and have content assigned to them.

![device offline optisigns portal](https://support.optisigns.com/hc/article_attachments/44652521300243)

**To identify and resolve network issues:**

- Create a mobile hotspot, then have your OptiKiosk connect with it. A successful connection indicates a problem with your general Wi-Fi connection.
- Try a different network. You may need to move the device to get connected. A successful connection indicates a problem with your general Wi-Fi connection.
- If you have firewalls, make sure OptiSigns is whitelisted. Refer to our [Whitelist Article](https://support.optisigns.com/hc/en-us/articles/360047275934) for the required URLs and ports.
- Plug in an Ethernet cable to see if it can still connect.
- After trying to connect with these methods, Factory Reset the device, then perform initial setup again.
- If the device still cannot connect to any network, [contact our support team](https://support.optisigns.com/hc/en-us/articles/35626165056787-How-to-Contact-OptiSigns-Support).

#### **Blank Screen Troubleshooting**

If your device and screen are on, but only displays a black screen:

- Network issues, see above.
- Check to make sure there is a Playlist or Asset assigned to your screen.
- Make sure your Timezones and Schedules match, including your Operational Schedule and normal schedule.
- Check your firewall settings, and ensure you’ve [Whitelisted OptiSigns IP addresses and ports](https://support.optisigns.com/hc/en-us/articles/360047275934-Whitelist-OptiSigns-IP-addresses-ports).
- Check your Operational Schedule, and verify its power settings are not set to Off. If an Operational Schedule’s power settings are set to Off, it will remain off during the designed time.

If the device is still not displaying content after you’ve checked these, try a Factory Reset.

#### **App Freezes, Video Assets Not Playing Full Video, or Asset Not Loaded Fully**

To handle any of these issues, hit the Refresh & Relaunch option, then reboot. You may need to Factory Reset if the problem persists.

#### **Factory Reset**

If your kiosk is still operable, you can perform a soft factory reset directly from the system settings:

1. Open the **Settings** app.
2. Scroll down and select System.
3. Tap Reset options.
4. Choose Erase all data (factory reset).
5. Confirm your choice to begin the reset.

This will erase all data from the kiosk’s internal storage, including Google accounts, system and app data, downloaded apps, music, photos, and any other user content. After the reset is complete, the device will restart with its original factory settings.

---

## **Safety & Compliance**

For safety, compliance, recycling, and other important information, please see:  
[discover.optisigns.com/device-safety-info](https://discover.optisigns.com/device-safety-info)

### **That's all!**

If you have further questions, please contact us:

- Email: <support@optisigns.com>
- Phone: [+1 (832) 410-8132](tel:18324108132)
