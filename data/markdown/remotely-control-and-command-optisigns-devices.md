# Remotely Control and Command OptiSigns Devices

Article URL: https://support.optisigns.com/hc/en-us/articles/360055486554-Remotely-Control-and-Command-OptiSigns-Devices
Article ID: 360055486554
Last Updated: 2025-09-24T18:58:23Z

### In this article, we’ll explore all the options for issuing commands remotely to OptiSigns devices.

- [What You’ll Need](#WhatYouNeed)
- [For Individual Devices](#IndividualDevices)
  - [Getting Started](#GettingStarted)
  - [Reboot Player](#Reboot)
  - [Take Screenshots](#Screenshot)
  - [Add/Remove WiFi](#WiFi)
  - [Update Time Zone](#TimeZone)
  - [View Device Info](#DeviceInfo)
  - [Remote Command History](#History)
  - [Additional Commands](#Additional)
  - [Remotely View Player Output](#RemoteView)
  - [Via the Mobile Admin App](#MobileAdminApp)
- [For Multiple OptiSigns Players](#MultiplePlayers)
  - [Enabling Remote Command Feature on Account](#EnableOnAccount)
  - [How to Execute Remote Commands](#HowtoExecuteRemoteCommands)
  - [Controlling Remote Commands Received by Player](#ControllingRemoteCommands)

OptiSigns Players ([**OptiStick**](https://shop.optisigns.com/products/optisigns-android-stick-player-2), [**Pro**](https://shop.optisigns.com/products/optisigns-promax-signage-player), or [**ProMax**](https://shop.optisigns.com/products/optisigns-promax-signage-player)) have an MDM software pre-provisioned on them to provide remote management capability. This can be used for troubleshooting, changing settings from the OptiSigns portal, remote monitoring, and more.

---

## What You’ll Need

- OptiSigns Player (OptiStick, Pro, or ProMax)
- OptiSigns [**Pro Plus**](https://www.optisigns.com/pricing) subscription or greater

|  |
| --- |
| **NOTE** |
| The OptiSigns Android Stick is capable of receiving **individual commands**. However, in order to send commands to **multiple devices simultaneously**, you will need an OptiSigns Pro or ProMax player. |

---

## For Individual Devices

The following applies to individual Optisticks and OptiSigns Pro and ProMax players. In order to get started, the player must be paired and online. Commands cannot be sent to offline or powered off players.

### Getting Started

To begin, navigate to your **Screens** tab within OptiSigns.

![optisigns screens tab](https://support.optisigns.com/hc/article_attachments/43590071759123)

Here, find the device/screen you want to send remote commands to. Then, hit **Edit**.

![open edit screen tab](https://support.optisigns.com/hc/article_attachments/43590071760659)

This will bring up the **Edit Screen** menu. Here, click **Advanced**.

![optisigns edit screen advanced](https://support.optisigns.com/hc/article_attachments/43590071762067)

Under the **Advanced** tab, you’ll find a set of green buttons like the ones below. This row of buttons are called the **MDM buttons** and are used for sending Remote Commands.

![optisigns edit screen mdm buttons](https://support.optisigns.com/hc/article_attachments/43590071763603)

|  |
| --- |
| **NOTE** |
| The MDM buttons ***will not appear***on non-OptiSigns devices or screens. |

### Reboot Player

The first option is to Reboot the player. Hit the button to do this.

![reboot mdm button](https://support.optisigns.com/hc/article_attachments/43590102856595)

You’ll be asked whether or not you want to reboot the player. Hit **Reboot** again to do so.

![reboot screen confirmation](https://support.optisigns.com/hc/article_attachments/43590102859283)

This will reboot the player, remotely.

### Take Screenshot

The second option is to take a screenshot. Hit the button to do this.

![take screenshot mdm button](https://support.optisigns.com/hc/article_attachments/43590102860179)

You’ll be asked if you want to take a screenshot. Hit **Take screenshot** to do so.

![take screenshot confirmation](https://support.optisigns.com/hc/article_attachments/43590102861075)

A screenshot of your display will appear in the area below:

![display screenshot](https://support.optisigns.com/hc/article_attachments/43590102862483)

This image can be saved and used for any purpose you wish.

### Add/Remove WiFi

The third option is to Add/Remove WiFi. Hit the button to get started.

![wifi mdm button](https://support.optisigns.com/hc/article_attachments/43590071774611)

This will open the **WiFi access points** menu. Here, you’ll see the WiFi access points saved on the device. In order to add more to it, hit **Add new WiFi access point**.

![wifi access points menu](https://support.optisigns.com/hc/article_attachments/43590071775763)

This will open the **Add WiFi access point details** window:

![add wifi access point details menu](https://support.optisigns.com/hc/article_attachments/43590071776531)

Enter your WiFi information in, and click **Add**. The new access point will be saved to the device.

### Update Time Zone

The fourth option is to update the Time Zone. Hit the button to get started.

![time zone mdm button](https://support.optisigns.com/hc/article_attachments/43590071778067)

This will open the **Update Time Zone** popup. Simply choose the Time Zone you’d like to update the device to here.

![update time zone menu](https://support.optisigns.com/hc/article_attachments/43590102868627)

### View Device Info

To check the device info, click the **“i” button**. It will pull up the hardware and network info of the device.

![device info mdm button](https://support.optisigns.com/hc/article_attachments/43590102869651)

You may find the info of interest to you. One common example is if you are using some network monitoring tool, you can use the MAC address to lookup the device in the other systems.

![device info view menu](https://support.optisigns.com/hc/article_attachments/43590071782291)

### Remote Command History

The last button shows the Remote Command history.

![remote command history mdm button](https://support.optisigns.com/hc/article_attachments/43590102871955)

This allows you to go through a history of the remote commands, what device it was on, and the execution result of the command.

![remote commands history menu](https://support.optisigns.com/hc/article_attachments/43590071783699)

### Additional Commands

Hitting the arrow near the buttons brings up a list of additional commands.

**![additional commands menu](https://support.optisigns.com/hc/article_attachments/43590071784723)**

- **Refresh & Relaunch:** Refresh and relaunch your screen. This is useful if your screen is frozen or is not functioning as intended, but you don't want to reboot the device.
- **Send HDMI CEC** - Use HDMI CEC commands to remotely turn on/off TV. Please make sure HDMI CEC support is enabled on the TV.
- **Send RS232:**This is used to utilize RS232 Commands to remotely turn your TV On/Off.
- **Get used storage/free storage:** Gives information on your used and free device storage.
- **Install OptiSigns Versions:** Lets you remotely install different versions of OptiSigns. If you downgrade from the current version, please make sure to turn off Auto Updates, otherwise it will automatically update to the current version (Android Stick Player only).
- **Disable Auto Update:** This will allow you to remotely disable automatic updates on your OptiSigns player. This is useful when you downgrade from the current version (Android Stick Player only).
- **Install APK:** Remotely install APK with a direct link/URL to the APK file (Android Stick Player only).

### Remotely View Player Output

Using the Remote Control feature, it’s possible to view what’s actually playing on your device, and make changes via the device menu with a mouse.

This is different from the Preview feature, which shows an approximation of what an Asset or Playlist will look like on your screen. The Remote Control feature allows you to actually remote into the device and see what’s playing, and interact with the device software directly.

To do this, hit **More** from within the **Advanced** section of the **Edit Screen**menu:

![edit screen advanced menu more](https://support.optisigns.com/hc/article_attachments/43590071786131)

Then, next to **Remote Control**, hit **Activate**.

![remote control activate](https://support.optisigns.com/hc/article_attachments/43590071786771)

A pop up will appear asking if you’re sure you want to activate Remote Control. Hit **Activate**.

![remote control activate](https://support.optisigns.com/hc/article_attachments/43590071787795)

Another box will appear informing you that it may take several seconds to fully remote into the device. Close this box, then scroll up to the main Remote Command area. Another option will have appeared: hit **Remote** to access the device.

![remote into device mdm button](https://support.optisigns.com/hc/article_attachments/43590071790483)

This will bring up a new browser window for you to view and control the device.

![remote mdm browser window](https://support.optisigns.com/hc/article_attachments/43590071792019)

### Via Mobile Admin App

The OptiSigns [Mobile Admin App](https://www.optisigns.com/mobile-app) lets you remotely control your devices in the same way as above. Simply download the app, and access your digital signage hardware through your mobile device.

See our [Mobile Admin App article](https://support.optisigns.com/hc/en-us/articles/30003143806099-How-to-Use-the-OptiSigns-Mobile-Admin-App) for more information.

---

## For Multiple OptiSigns Players

It’s possible to send basic remote commands to individual players, segments of OptiSigns players (defined via [tagging](https://support.optisigns.com/hc/en-us/articles/38062664690195-Tagging-in-OptiSigns)), or all your OptiSigns players simultaneously. These commands allow for mass provisioning, updating, and troubleshooting. This section applies to Pro and ProMax players only, not the OptiStick.

The ability to do this needs to be activated. Simply contact us at [support@optisigns.com](mailto:support@optisigns.com) to be given the ability to send remote commands.

### Enabling Remote Commands Feature on Account

Remote Command Execution is disabled by default. To use it, it will need to be turned on. To do this, navigate to [the Preferences section](https://app.optisigns.com/app/s/preference-settings) in the OptiSigns portal.

|  |
| --- |
| For security reasons, **only the account owner** can enable or disable Remote Command Execution. |

![enabling remote commands on account](https://support.optisigns.com/hc/article_attachments/43590071793427)

### How to Execute Remote Commands

To submit the command to manage the devices remotely, you will need to go to the remote command execution console. Click **Screens**, then the **More Options (Three Dots)**

Screens -> More Options Icon -> Execute Remote Commands

![more options execute remote commands](https://support.optisigns.com/hc/article_attachments/43590071795219)

The Execute Remote Commands console can be broken down into three sections:

- **Section 1** - Where you specify the target of the commands.
- **Section 2** - The command you want to execute.
- **Section 3** - The execution result and history.

![execute remote commands steps](https://support.optisigns.com/hc/article_attachments/43590102885907)

For section 1, there are 2 types of targets you can choose from:

- **Screens** - You can select the screen name here, it can be one screen or multiple screens.
- **Tags** - Utilizing tags, you can execute the command on a group of devices. In the below example, the command will be submitted to all devices tagged as Windows or Raspberry Pi.

![target and tags execute remote commands](https://support.optisigns.com/hc/article_attachments/43590071798035)

For section 2, you can enter the command you want to execute in the text box. The command needs to be OS-specific, depending on the OS your device is running on (Android for Android Stick, Linux for OptiSigns Pro / ProMax players), you will need to build the scripts accordingly. Once you have your commands ready, just click the submit button. The command will be pushed to the devices for execution.

Other than the free-form scripts, there are some common commands built into the platform, to achieve these functions, you will just need to select it from the drop-down menu. Depending on the type of device OS, the command will be submitted accordingly.

![refresh and relaunch](https://support.optisigns.com/hc/article_attachments/43590071799571)

After a command is executed, it will appear in section 3: the command history.

|  |
| --- |
| **NOTE** |
| The **Refresh & Relaunch**command can be used on any device. The **Reboot Device**command cannot be used on certain Android devices. |

### Controlling Remote Commands Received by Players

In some cases, you may not want some of your devices to be controlled remotely for any reason. The ability to receive remote commands can be toggled on the device.

Go to the side menu on the OptiSigns player, click **Advanced Options**, and you'll find the toggle for **Execute Remote Commands**. Toggling this off will cause the device to reject remote commands.

![controlling remote commands in-app menu](https://support.optisigns.com/hc/article_attachments/43590102889363)

### That’s all!

OptiSigns is a leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
