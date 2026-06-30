# How to Use the Website App and Display URLs on OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/360016382473-How-to-Use-the-Website-App-and-Display-URLs-on-OptiSigns
Article ID: 360016382473
Last Updated: 2026-02-03T18:12:07Z

### In this article, we'll show you how to set up the Website app to display basic websites on your digital signs.

- [What You'll Need](#WhatYouNeed)
- [Setting Up a Website App](#SettingUp)
- [Deploying a Website App](#Deploying)

To display Websites on your digital signs, you can use the **Website app**. Here is how to set one up.

---

## What You'll Need

- An OptiSigns account - [**Free Plan or higher**](https://www.optisigns.com/pricing)
- A Website URL
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653-What-hardware-and-devices-are-supported) - if on Free plan, one of [these devices](https://support.optisigns.com/hc/en-us/articles/33940834613139-What-Do-I-Get-With-an-OptiSigns-Free-Plan#Devices)
- A screen, [set up and paired with OptiSigns](https://support.optisigns.com/hc/en-us/articles/18823504383891-OptiSigns-Getting-Started-Guide)

---

## Setting Up a Website App

On the OptiSigns portal, go to **Assets → Add Asset → Apps.**

![optisigns add asset](https://support.optisigns.com/hc/article_attachments/48787486790547)

Select **Website**:

![optisigns website app selection](https://support.optisigns.com/hc/article_attachments/48787464573587)

Fill in the name and the link (URL) of the site you want to use.  
You can also specify refresh interval if you want the player to automatically refresh the link at certain interval.

![optisigns website app interface](https://support.optisigns.com/hc/article_attachments/48787464575763)

- **Name** - The Name of your Website within OptiSigns. This is for organizational purposes within the OptiSigns portal, and will NOT be displayed on your signs.
- **URL** - The URL of the website you wish to display.

|  |
| --- |
| **NOTE** |
| Every website is different - many will not allow Embedding, or others have specific security requirements. Even if it does not display in the Preview pane on the right, we recommend attempting to push this to your screen to be sure it will display properly. If not, you may need to use the [**Advanced Website** app](https://support.optisigns.com/hc/en-us/articles/5149077938835-How-to-use-Advanced-Website-App), or [**Web Scripting** app](https://support.optisigns.com/hc/en-us/articles/1500012522362-How-to-use-the-Web-Scripting-App) if your website requires login or authentication. |

- **Update Interval** - Choose how often to refresh the website to provide up-to-date data. By default, this is set to 600 seconds (10 minutes). Note that, if a Website app is used as part of a Playlist, it will always automatically refresh when it is brought up.
  - **Load only first time (no refresh)** - When toggled, will only load the website when it is first displayed on the sign. Choose this if you notice interrupted playback when trying to load a website (usually caused by latency or network issues).

---

## Deploying a Website App

You can deploy your new Website app as an individual asset, or as part of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573-How-to-Create-and-Use-the-Split-Screen-App).

To get your new Website asset to a screen, go to the **Screens** tab, then click the screen you want to assign it to.

![optisigns screens](https://support.optisigns.com/hc/article_attachments/48787464579475)

This brings up the **Edit Screen** tab:

![optisigns edit screen select asset](https://support.optisigns.com/hc/article_attachments/48787464582035)

Here, select **Asset** under Content type, then hit **Select Asset**.

Then, select your created Website Asset:

![optisigns select asset](https://support.optisigns.com/hc/article_attachments/48787464585619)

Now hit **Save**. Your Website asset will now display on screen.

You can also deploy it as part of a split screen, allowing you to show other assets at the same time. See how in our [Split Screen app article.](https://support.optisigns.com/hc/en-us/articles/360026559573-How-to-Create-and-Use-the-Split-Screen-App)

In order to display multiple web pages, you can create individual Website assets, then place them in a [Playlist](https://support.optisigns.com/hc/en-us/articles/28295104605843-How-to-Create-Use-Playlists). The asset or playlist can also be placed in a [Schedule](https://support.optisigns.com/hc/en-us/articles/360016981853-Creating-and-Using-Schedules-with-OptiSigns).

### That's all!

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
