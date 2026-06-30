# How to Use OptiSigns with Microsoft Teams Rooms

Article URL: https://support.optisigns.com/hc/en-us/articles/36911639377683-How-to-Use-OptiSigns-with-Microsoft-Teams-Rooms
Article ID: 36911639377683
Last Updated: 2025-09-04T18:42:32Z

### In this article, we will explain how to set up OptiSigns for use with Microsoft Teams Rooms’ new Digital Signage option.

- [Prerequisites](#Prerequisites)
- [Configure the Source within Teams Rooms Pro Management Portal and OptiSigns Web Player](#Configure)
- [Send to a Teams Rooms Device](#Send)
- [Set Up the Virtual Screen App (ALTERNATE METHOD)](#SetUp)

Microsoft has released a new Digital Signage option for their [Microsoft Teams Rooms](https://www.microsoft.com/en-us/microsoft-teams/microsoft-teams-rooms) application, which allows digital signage to be displayed on a Microsoft Teams Rooms device. This will cause Teams Rooms screens and devices to display digital signage content when idle.

![teams rooms using digital signage](https://support.optisigns.com/hc/article_attachments/36911639363347)

---

## Prerequisites

Before getting started, you’ll need:

- Microsoft Teams Rooms Pro on Windows 5.1 or later
- A configured Microsoft Teams Rooms device
- An active OptiSigns subscription

Once this is accomplished, we can move on to the next step.

---

## Configure the Source within Teams Rooms Pro Management Portal and OptiSigns Web Player

Navigate to your Teams Rooms Pro Management Portal. On the left toolbar, expand the **Settings** section then click **Digital signage**.

![teams rooms pro manager digital signage setting](https://support.optisigns.com/hc/article_attachments/36911639368723)

On this screen, ensure the Digital signage switch is **On** (it should be by default), then click **Add Source**.

![teams rooms digital signage screen steps](https://support.optisigns.com/hc/article_attachments/36911646828435)

This screen will appear:

![teams rooms add digital signage source](https://support.optisigns.com/hc/article_attachments/36911646829075)

The **Name and Description** sections are purely for MS Teams Rooms - provide a name and description which will help you identify your signs in case you want to make several. Once inputted, hit **Next**.

Now you’ll need to Select source. We recommend using the OptiSigns Web Player for this. It allows frequent updates and is extremely easy to set up. Simply input the following URL as your Custom Source:

```
https://webplayer.optisigns.com/
```

![custom source ms teams rooms optisigns web player](https://support.optisigns.com/hc/article_attachments/37071139357331)

The last screen is a Review screen. If everything looks good, hit Finish.

Last, you'll need to input your pairing code:

![optisigns web player + pairing code](https://support.optisigns.com/hc/article_attachments/37071127510291)

See our article on [Setting Up and Adding Screens](https://support.optisigns.com/hc/en-us/articles/360016374813-Set-up-add-a-screen) for more information.

---

## Send to a Teams Rooms Device

Whichever method you've used, you'll need to send your Source to a Teams Rooms device. To begin, click **Assign to rooms**.

![teams rooms assign to rooms choice](https://support.optisigns.com/hc/article_attachments/36911639371667)

Choose the Source you made in the last step, then hit **Next**.

![teams rooms assign to rooms select source](https://support.optisigns.com/hc/article_attachments/36911639373203)

Now you’ll be reviewing your preferences for how to display signage on your Rooms app.

![teams rooms assign to rooms review preferences](https://support.optisigns.com/hc/article_attachments/36911646833939)

There are several parts to take note of here:

- **Show Teams Rooms banner** - Displays Room information over top of your digital signage when selected. Remove if you do not want this overlay.
- **Display Period** - These settings allow you to configure how quickly your display changes from Teams Rooms settings to your signage.
- **Allow screen timeout when device is idle** - When selected, this will keep your default screen settings for timing it out. Deselect this if you want your signage to continuously display.

Once you’ve tweaked these settings to your liking, hit **Next**. You’ll be taken to the Assign rooms screen.

![teams rooms assign rooms](https://support.optisigns.com/hc/article_attachments/36911646834451)

Here, simply choose the Room you want the signage to display it. Hit **Next**.

![teams rooms assign rooms select schedule](https://support.optisigns.com/hc/article_attachments/36911639374867)

These options change when these changes will be applied. Pick one, then hit **Next**.

Now you’ll review all these changes. Simply hit **Submit**, and you’re done.

---

## Set Up the Virtual Screen App (ALTERNATE METHOD)

Set up a [Virtual Screen app](https://support.optisigns.com/hc/en-us/articles/360055900513-How-to-create-and-use-Virtual-Screen-App) as an alternative to the OptiSigns Web Player. This app will provide an alternate URL to use as a Source in our Microsoft Teams Rooms Portal to set up digital signage.

To get started, click **Files/Assets** within the OptiSigns app and navigate to **Apps**.

![optisigns portal files assets app](https://support.optisigns.com/hc/article_attachments/36911646823955)

Search for **Virtual Screen App**, then select it.

![virtual screen app optisigns](https://support.optisigns.com/hc/article_attachments/36911646824467)

You’ll see a screen similar to this:

![virtual screen app config optisigns](https://support.optisigns.com/hc/article_attachments/36911639366931)

You’ll need to fill in the information on the side.

![virtual screen app information filled in](https://support.optisigns.com/hc/article_attachments/36911646826515)

For this, there are a couple things to note.

First, the **Screen** you select will be what displays on your Microsoft Teams Rooms display. This screen should be configured with the digital signage you want to display there.

Second, the **Share Type** should be set to **URL Link**. It is this URL you will input into the Teams Rooms Professional Portal in the next step.

Now, hit **Save**. Your asset/playlist will show on the right side of the screen, and you’ll receive the URL you need.

![virtual screen app completely configured](https://support.optisigns.com/hc/article_attachments/36911639367955)

This Virtual Room app will now be saved as an Asset on OptiSigns. By clicking on it, you will be able to access the URL anytime. You'll want to enter this into your Custom source within the Teams Rooms Pro Management portal.

![teams rooms digital signage select source](https://support.optisigns.com/hc/article_attachments/36911646830483)

---

### That’s all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
