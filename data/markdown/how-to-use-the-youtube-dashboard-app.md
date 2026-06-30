# How to Use the YouTube Dashboard App

Article URL: https://support.optisigns.com/hc/en-us/articles/48626115821459-How-to-Use-the-YouTube-Dashboard-App
Article ID: 48626115821459
Last Updated: 2026-02-02T15:32:55Z

### In this article, we'll show how to display YouTube Dashboard information on your digital signs with OptiSigns.

- [What You'll Need](#WhatYouNeed)
- [Accessing Looker Studio and Linking YouTube Dashboard Data](#AccessingLooker)
- [Generating Your Dashboard from a Template](#GeneratingDashboard)
- [Creating a YouTube Dashboard App](#CreatingApp)
- [Deploying a YouTube Dashboard App](#DeployingApp)

With the YouTube Dashboard app, it's possible to display near real-time dashboards of information pulled straight from YouTube Dashboard. These dashboards are created in Google Looker Studio and can be customized, then communicated throughout the company via digital signage.

Let's get started.

---

## What You'll Need

- An OptiSigns account - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
- A YouTube Studio account, set up and enabled
- Access to Looker Studio
- An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653-What-hardware-and-devices-are-supported)
- A screen, [set up and paired with OptiSigns](https://support.optisigns.com/hc/en-us/articles/18823504383891-OptiSigns-Getting-Started-Guide)

---

## Accessing Looker Studio and Linking YouTube Analytics Data

In order to get your YouTube Analytics data into the proper format, you'll need to export it to Looker Studio. Start by going to [lookerstudio.google.com](https://lookerstudio.google.com) and logging in with your Google Account.

Now, connect your account as a data source by clicking **Create** then **Data source**:

![](https://support.optisigns.com/hc/article_attachments/48626106655379)

Now click **YouTube Analytics** as your Connector.

![](https://support.optisigns.com/hc/article_attachments/48626115789843)

You'll need to **Authorize** Looker Studio to use your YouTube Channel, set the **Account**, then hit **Connect.**

![](https://support.optisigns.com/hc/article_attachments/48626115793043)

Once connected, you'll be able to set your data, including which fields and parameters you'd like to include in Looker Studio. Select whichever you'd like to display.

From here, you have two options:

1. Click **Create Report**. This will allow you to create and customize your YouTube Analytics report from scratch. Do this if you want granular control over how your data looks.
2. Use a **YouTube Channel** template. This will allow you to quickly organize your data. Use this if you want your data on screen quickly.

This guide will assume you choose to use a Template. If you choose Create Report, feel free to skip to the next section.

---

## Generating Your Dashboard from a Template

Back out to the Looker Studio homepage, then select **YouTube Channel Report**.

![](https://support.optisigns.com/hc/article_attachments/48626106662035)

This will generate a sample report. Click **Use My Own Data:**

![](https://support.optisigns.com/hc/article_attachments/48626106663315)

Now, choose the **Account,** then hit **Add.**

If done correctly, you'll see a green dot in the Use my own data area.

Now, set up the report the way you like it. Then, hit **Share**, and make sure the report is set to **Public:**

![](https://support.optisigns.com/hc/article_attachments/48656734362515)

This allows it to be set up, and is necessary for it to display.

---

## Creating Your YouTube Dashboard App

Once you have your report set up the way you'd like to display it, click **Edit**:

![](https://support.optisigns.com/hc/article_attachments/48626115798675)

Now go to **File → Embed report**.

![](https://support.optisigns.com/hc/article_attachments/48626106668691)

Now you should be on the **Embed Report** screen. Click **Enable embedding**, then make sure it is displaying an Embed Code. Change your **Width** and **Height** to match the resolution of the display you plan to use as a digital sign - we generally recommend 1920x1080 if you're unsure - then click **Copy to Clipboard.**

![](https://support.optisigns.com/hc/article_attachments/48626115803027)

Next, go to the OptiSigns portal. Go to **Assets → Add Asset → Apps.**

![](https://support.optisigns.com/hc/article_attachments/48626106670611)

Select **YouTube Dashboard:**

![](https://support.optisigns.com/hc/article_attachments/48626115806995)

Now you can set up your YouTube Dashboard app:

![](https://support.optisigns.com/hc/article_attachments/48626106675603)

- **Name -** The name of your YouTube Dashboard asset. This is for organizational purposes within OptiSigns only and will not display on your screens.
- **Embed Code** **-** The Embed Code you retrieved a moment ago should be pasted into this field.
- **Update Interval -** How often OptiSigns will ping your Embed URL to update the data displayed on it. This is measured in seconds.

|  |
| --- |
| **NOTE** |
| The Preview at this stage may display oddly. This is ok. We recommend pushing your YouTube Dashboard app to a real screen for proper testing. Afterward, we can come back to this and alter the Width and Height elements if they need adjusting. |

Now, hit **Save**. You'll have created a YouTube Dashboard app.

---

## Deploying a YouTube Dashboard App

You can deploy your new YouTube Dashboard app as an individual asset, or as part of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573-How-to-Create-and-Use-the-Split-Screen-App).

To get your new YouTube Dashboard asset to a screen, go to the **Screens** tab, then click the screen you want to assign it to.

![](https://support.optisigns.com/hc/article_attachments/48626106679315)

This brings up the **Edit Screen** tab:

![](https://support.optisigns.com/hc/article_attachments/48656464012819)

Here, select **Asset** under Content type, then hit **Change** next to Selected Asset.

Then, select your created Google Analytics Asset:

![](https://support.optisigns.com/hc/article_attachments/48626115811347)

Now hit **Save**. Your Google Analytics asset will now display on screen.

|  |
| --- |
| **NOTE** |
| You may need to alter the Width and Height on the Embed Code to get it to display exactly the way you want it. Be sure to push it to the intended screen first to test it - the Preview sometimes looks odd. |

You can also deploy it as part of a split screen, allowing you to show other assets at the same time. See how in our [Split Screen app article.](https://support.optisigns.com/hc/en-us/articles/360026559573-How-to-Create-and-Use-the-Split-Screen-App) It can also be displayed in a Playlist or Schedule.

### That's all!

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
