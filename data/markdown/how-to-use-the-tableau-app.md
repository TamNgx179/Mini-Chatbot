# How to Use the Tableau App

Article URL: https://support.optisigns.com/hc/en-us/articles/39250660729747-How-to-Use-the-Tableau-App
Article ID: 39250660729747
Last Updated: 2026-01-06T22:36:49Z

### In this article, we’ll show you how to set up and use the Tableau app to display Dashboards on digital signs.

- [What You’ll Need](#WhatYouNeed)
- [Step 1: Set Up OptiSigns as a Connected App in Tableau](#Step1)
- [Step 2: Set Up Tableau Integration in OptiSigns](#Step2)
- [Step 3: Creating a Tableau Asset](#Step3)
- [Additional Notes](#Notes)

With the Tableau app, it’s possible to securely display Tableau dashboards on your large TVs and screens. This can dramatically increase communication and information across office spaces.

To do this, you’ll need to follow three steps:

1. Set up OptiSigns as a Connected App within Tableau
2. Set up the Tableau Integration in OptiSigns
3. Create a Tableau Asset and Assign it to a Screen

Let’s get started.

---

## What You’ll Need

- OptiSigns [Pro Plus](https://www.optisigns.com/pricing) subscription or greater
- A screen, [set up and paired](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv) with OptiSigns
- Tableau Cloud account
- A fully created Tableau Report
- Administrator Access within OptiSigns. See [Managing User Roles](https://support.optisigns.com/hc/en-us/articles/360046356113-Advanced-Security-Managing-User-Roles) for more information.

---

## Step 1: Set Up OptiSigns as a Connected App in Tableau Cloud

To view Private reports in OptiSigns, it needs to be set up as a **Connected App** in Tableau Cloud. If you’re only interested in displaying Public reports, this step can be skipped - however, we ***highly recommend*** it, as setting up this integration will allow you to use it for any future reports you want to display from this account. If you are only interested in displaying Public reports, though, feel free to [skip to step 3](#Step3).

To begin, find your **Settings** tab within Tableau. Once there, click **Connected Apps** → **New Connected App**.

![new connected app tableau](https://support.optisigns.com/hc/article_attachments/39250613919635)

Select **Direct Trust**.

![direct trust dropdown tableau](https://support.optisigns.com/hc/article_attachments/39250613922451)

You’ll open the Create Connected App window. Here, you can give your connected app a name (we recommend “OptiSigns” so you know it’s for us), restrict its access, and provide allowed domains. For the purposes of this example, we’ll apply it to “All projects” and “All domains.”

![create connected app window tableau](https://support.optisigns.com/hc/article_attachments/39250613923987)

Once created, it will appear in a list of Connected Apps. Select the app.

On this screen, you'll want to **Enable** the OptiSigns app by hitting the **Three Dots**. Then, you'll want to hit **Generate New Secret**:

![Screenshot 2025-03-22 at 5.27.26 PM.jpg](https://support.optisigns.com/hc/article_attachments/39672709375507)

The blurred out values are your **Secret ID, Secret Value, and Client ID**. These values will be critical to setting up your integration with OptiSigns, so keep this tab open.

With this information and the app Enabled in Tableau, we can configure the integration in OptiSigns.

---

## Step 2: Set Up Tableau Integration in OptiSigns

Before starting this step, you should have:

1. Your **Secret ID, Secret Value, and Client ID** from your Connected App in Tableau on hand
2. Your Connected App set to Enable

When you’re ready to go, navigate to the **Integrations** tab within OptiSigns:

![integrations tab optisigns](https://support.optisigns.com/hc/article_attachments/39250660697107)

Under the Tableau section of the Integrations page, select **Add Connection**.

![](https://support.optisigns.com/hc/article_attachments/39597853563283)

The **Add** window will pop up:

![add integrations window optisigns](https://support.optisigns.com/hc/article_attachments/39250613933203)  
You’ll need to fill in 5 values:

- **Name -** The name of the integration. Put whatever you want to help identify it.
- **Email -** The email associated with your Tableau account. This ***has to match***.
- **Client ID -** The Client ID from [the last step](#Step1).
- **Secret ID -** The Secret ID from the last step.
- **Secret Value -** The Secret Value from the last step.

Last, make sure the **Active** box is checked. When unchecked, this saves the integration but does not activate it.

Once these values are filled in, hit **Add**. We are now ready to create a Tableau Asset.

---

## Step 3: Create a Tableau Asset and Assign it to a Screen

Now that we’ve got the Tableau integration set up, it’s time to create a Tableau asset. This asset determines how your report will show up on your screens.

|  |
| --- |
| **NOTE** |
| See [**Note 2**](#Note2) if your workbook contains Broad Views. |

First, find the report you’d like to display. Hit **Share:**

![](https://support.optisigns.com/hc/article_attachments/39364492002579)

On the Share View window, hit **Copy Link**:

![share view copy link tableau](https://support.optisigns.com/hc/article_attachments/39250613936275)

Now go back to the OptiSigns portal and hit **Files/Assets** → **Apps:**

![optisigns files/assets tab app](https://support.optisigns.com/hc/article_attachments/39250613937555)

Now find the **Tableau** app.

![tableau app optisigns](https://support.optisigns.com/hc/article_attachments/39250660711955)

Clicking the app will open this window:

![](https://support.optisigns.com/hc/article_attachments/39597827693203)

- **Name -** The name of your Asset. This is used entirely in OptiSigns and can be anything you like.
- **Tableau Shared Report URL -** This is where you’ll input the Share URL you copied earlier.
- **Update Interval -** Denotes how often the app will sync, measured in seconds.
- **Authenticate with Connected App Integration -** Tick this box if you want to use Private reports. Since we set this up in [Steps 1](#Step1) and [2](#Step2), we recommend ticking this box. If you skipped those steps and only want to use Public reports, no need to check the box.

|  |
| --- |
| **NOTE** |
| Tableau Cloud only allows 600 Update Interval requests per user/hour. See [**Note 3**](#Note3) for more information and solutions on how to handle this. |

Now it's time to authenticate your Shared Report URL with an appropriate Connected App Integration you set up earlier:

![](https://support.optisigns.com/hc/article_attachments/39597827694099)

- **Connected App Integration -** Select the integration [you set up in Step 2](#Step2) in this box.

Once you input the **Tableau Shared Report URL** and have selected your Integration, hit **Save** and your report should appear as a Preview:

![](https://support.optisigns.com/hc/article_attachments/39597827695763)

Once you have tailored it to your liking, you can **Close** it. This will create a Tableau asset that can be added to a Playlist or directly assigned to a screen:

![](https://support.optisigns.com/hc/article_attachments/39597853567251)

In order to display different tabs of a report, select the tab you'd like to view on Tableau site, then hit **Share**, same way as before:

![tableau report share](https://support.optisigns.com/hc/article_attachments/39250660703635)

You'll then create a new Asset with that Share link as the **Site URL**:

![](https://support.optisigns.com/hc/article_attachments/39597827698067)

To display all the tabs in a report on a screen, these Assets can be placed in a [Playlist](https://support.optisigns.com/hc/en-us/articles/28295104605843-How-to-Create-Use-Playlists) to show the complete report.

## Additional Notes

#### Note 1

Content display may vary based on device type and screen resolution.

#### Note 2

**If your workbook contains broad views:**

- - - Create Custom Views on the Tableau site and use the Custom View's URL as the Shared Report URL.![](https://support.optisigns.com/hc/article_attachments/39597853568787)
    - Set the View Size to either **Fit Width**, **Fit Height**, or **Entire View**:  
      ![](https://support.optisigns.com/hc/article_attachments/39597827704979)

#### Note 3:

[Tableau currently limits](https://help.tableau.com/current/online/en-us/to_site_capacity.htm) its maximum number of refresh requests to 600 per hour/user. This means you'll want to be careful on how you set the "Update Interval," especially if you have numerous devices wanting to display Tableau reports.

We have several recommendations on how to handle this with multiple devices:

1. Set the Update Interval to match the number of devices. For example, if you have 50 devices, you can have a maximum Update Interval of 5 minutes (300 s) for a single report. With more devices this Update Interval will need to be longer, with less, it can be shorter.
2. For using Reports in a Playlist, the Report will update each time it is played. You'll need to set the proper duration, factoring in the number of reports and the number of devices. For example, if you have 10 reports on a single playlist across 5 devices, you can have a Playlist duration of 5 minutes (300 s).
3. To scale beyond these limitations, you'll need to create more connected apps under different Tableau Cloud users. Each Tableau Cloud user will have 600 requests an hour.

#### Note 4:

In addition, Tableau has a [**Data Freshness Policy**](https://help.tableau.com/current/online/en-us/data_freshness_policy.htm)which limits the number of refreshes of a workbook using a live connection. This is a setting within Tableau that controls your refresh rate.

To change this, go to the workbook you want to edit. Hit the **Info button** **→ Edit Freshness Policy...** then click **Ensure data is fresh every:** and set it to your desired freshness.

![](https://support.optisigns.com/hc/article_attachments/47980799604755)

There are a few critical points to note here.

- Tableau limits your refreshes to **12 per day**. This means that, if you set it to 10 minutes for example, you'll refresh your report every ten minutes for the first two hours, then you'll have to wait another 22 hours before it refreshes again.
- This means the minimum refresh timer we recommend is **2 hours.** This means your data will be refreshed consistently every two hours. This can be tuned further depending on your use case - for example, if you don't need it to update after 6pm, you can set it to **90 minutes**.

### That’s all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
