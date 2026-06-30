# How to Use the Microsoft Meeting Room App

Article URL: https://support.optisigns.com/hc/en-us/articles/4406214738707-How-to-Use-the-Microsoft-Meeting-Room-App
Article ID: 4406214738707
Last Updated: 2026-03-25T21:28:34Z

- [What You'll Need](#WhatYouNeed)
- [Creating a Microsoft Meeting Room App](#Creating)
  - [(OPTIONAL) Allow Booking](#AllowBooking)
- [Deploying a Microsoft Meeting Room App](#Deploying)
- [Frequently Asked Questions](#FAQs)

With OptiSigns you can display Microsoft meeting rooms schedules, see when the room is busy.

(Optionally) **Allow booking**, so user can scan QR Code or touch the screens to book meeting room.

Singe room view screenshot is below, you can view a live example [here](https://social-player.optisigns.com/meeting-calendar/?asset_id=oRuJf4DS9Ng6vSZ57):

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4406259553939)

---

## What You'll Need

- An OptiSigns account - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653-What-hardware-and-devices-are-supported)
- A screen, [set up and paired with OptiSigns](https://support.optisigns.com/hc/en-us/articles/18823504383891-OptiSigns-Getting-Started-Guide)

You'll also need a Microsoft Account with these conditions:

- Set up room mailboxes. See how to [here](https://docs.microsoft.com/en-us/microsoft-365/admin/manage/room-and-equipment-mailboxes?view=o365-worldwide) (section Set up room and equipment mailboxes). **Ensure** the Auto accept meeting request option is turned **On.**
- If your Microsoft account lacks Global administrator access, you'll need to ask your Global administrator to delegate access for room resource’s calendar to your account by:
  1. Going to [Microsoft admin center.](https://admin.microsoft.com/adminportal)
  2. Navigating to **Resources** **→** **Room & equipment**.

     ![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4406214340499)
  3. Click the room name and click **Edit** or **Show all** in Delegates section.
  4. Select your account in **Manage delegates** and click **Save changes**.

After that, you're ready to move on to the next step.

---

## Creating a Microsoft Meeting Rooms App

To display Microsoft Meeting Rooms onscreen, you'll need to create an app within OptiSigns.

First, go to the [OptiSigns Portal](http://app.optisigns.com/). Go to **Files/Assets → Add Asset → Apps.**

![](https://support.optisigns.com/hc/article_attachments/50258994637203)

Select **Microsoft Meeting Room**.

![](https://support.optisigns.com/hc/article_attachments/50258994638611)

The below screen should appear:

![](https://support.optisigns.com/hc/article_attachments/50258994645651)

Here, you have two options. If you have used a Microsoft account on the OptiSigns platform, you can select it from the dropdown. If you have not, you'll need to hit **Login with Work Account**, enter in your Microsoft account information, and grant OptiSigns the necessary permissions. Then, hit **Next** within OptiSigns.

The below screen should then appear (with nothing filled in), along with a Preview:

![](https://support.optisigns.com/hc/article_attachments/50258978907795)

- **Name** **-** Name of your Microsoft Meeting Room Wall, this is the name of the wall in your asset list. It will **not** be displayed on your screens.
- **Rooms** - Select list of rooms you want to display. You can choose as many as you like.

|  |
| --- |
| **IMPORTANT** |
| **Rooms** may only be selected **once** during asset creation and cannot be changed later. To do this, simply delete the old asset and create a new one. |

- **Allow Booking -** Check this to allow booking of the meeting room via a QR code displayed on the screen. We will go over this more in the **Allow Booking** section of the article below.

You may also switch between **Landscape** and **Portrait** for your Preview, depending on the orientation of the display you wish to display the app on.

#### Theme Settings

Toggle this open or closed. These settings will be reflected in the Preview on the right.

- **Theme -** Choose between Light and Dark theme for your displays.
- **Background Image -** Choose between the Default image, or a Custom Background image. If Custom is chosen, a new option will appear:

![](https://support.optisigns.com/hc/article_attachments/50258994650387)

- **Choose Photo -** Select the photo you wish to use as a Background Image. This must be an existing asset within OptiSigns.
- **Font Size -** Change the size of the font on your Microsoft Meeting Room Display

#### Advanced

Toggle this open or closed. These settings will be reflected in the Preview on the right.

![](https://support.optisigns.com/hc/article_attachments/50258978909843)

- **Time Format -** Change between 12 hour and 24 hour clocks.
- **Timezone -** Change the timezone of the meeting. This defaults to the used device's timezone, but can be specified here if needed.
- **Language -** Choose between a variety of language options for the display.

### (Optional) Allow Booking

You can check Allow Booking and input instruction.

User can scan QR code or touch the screen (if it's a tablet) to book the meeting room.

If user scan QR code, they can book the meeting from their mobile phone browser.

![](https://support.optisigns.com/hc/article_attachments/50258994655123)

![](https://support.optisigns.com/hc/article_attachments/50258994655635)

Click **Save**. You can change the wall any time by click on it in the Files/Assets tab.

Now you're ready to deploy it.

---

## Deploying a Microsoft Meeting Room App

You can deploy your new Microsoft Meeting Room app as an individual asset, or as part of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573-How-to-Create-and-Use-the-Split-Screen-App).

To get your new Microsoft Meeting Room asset to a screen, go to the **Screens** tab, then click the screen you want to assign it to.

![](https://support.optisigns.com/hc/article_attachments/50258994657555)

This brings up the **Edit Screen** tab:

![](https://support.optisigns.com/hc/article_attachments/50258994661651)

Here, select **Asset** under Content type, then hit **Browse** next to Selected Asset (if needed).

Then, select your created Microsoft Meeting Room asset:

![](https://support.optisigns.com/hc/article_attachments/50258994662547)

Now hit **Save**. Your Microsoft Meeting Room asset will now display on screen.

|  |
| --- |
| **NOTE** |
| Be sure to push the app to the intended screen first to test it - the Preview sometimes looks odd. |

You can also deploy it as part of a split screen, allowing you to show other assets at the same time. See how in our [Split Screen app article.](https://support.optisigns.com/hc/en-us/articles/360026559573-How-to-Create-and-Use-the-Split-Screen-App) It can also be displayed in a Playlist or Schedule.

---

## Frequently Asked Questions

#### Why does using Meeting Room require giving OptiSigns Admin permission to use?

OptiSigns uses Microsoft APIs for integration. In order for our integrations to work, the integration has to be approved by an administrator. This is the same across all integrations using Microsoft APIs.

This administrator access is only needed for first time access. Once the OptiSigns app is approved for use, other users can use OptiSigns directly.

### **That's all!**

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
