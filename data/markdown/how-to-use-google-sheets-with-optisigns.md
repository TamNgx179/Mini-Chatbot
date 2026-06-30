# How to use Google Sheets with OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/360056977214-How-to-use-Google-Sheets-with-OptiSigns
Article ID: 360056977214
Last Updated: 2025-12-12T21:10:43Z

### Google Sheets is among one of the most popular spreadsheet applications available online. In OptiSigns, you can set up a Google Sheets app so that whenever changes are made on your Sheet it will automatically show up on your screen.

|  |
| --- |
| **Google Sheets app is currently only available on Standard and above plans.** |

In this article, we'll cover:

- [How to create a Google Sheet App](#Create)
  - [Option 1: Setting Up a Private Sheet](#1)
  - [Option 2: Setting Up a Public Sheet](#2)
- [Limitations](#Limitation)

---

## How to Create a Google Sheet App

Open the [**OptiSigns portal**](https://app.optisigns.com/app/screenManagement) → Go to [**Files/Assets page**](https://app.optisigns.com/app/assetManagement)

Click **Apps** → Search for **Google Sheets** and click on the app:

![](https://support.optisigns.com/hc/article_attachments/33979969417107)

There are two ways you can set up your Google Sheets:

1. [Using a private Sheet](#1)
2. [Using a public Sheet](#2)

Depending on how you have your document set up, please pick the option that best suits your use case.

---

## Option 1: Setting Up a Private Sheet

***This option is useful if you have private information on your Sheet or want more access and customization of your Sheet in OptiSigns.***

In Google Sheets, **open the Google Sheet** you'd like to import **→ Copy the URL**

![](https://support.optisigns.com/hc/article_attachments/33979909649171)

Return to your Google Sheets app in the OptiSigns portal.

**Name** your asset → **Paste the Sheet's URL** into the URL box → Click **Next**

![](https://support.optisigns.com/hc/article_attachments/33979909650835)

A **"Sign** **In With Google"** box will appear beneath the URL box, click on it.

![chrome_QH2y6SgYtm.jpg](https://support.optisigns.com/hc/article_attachments/33979969425299)

A Google authorization pop-up window will appear → Follow the steps to authenticate your account connected to the Google Sheets → Click **Continue**

![chrome_eX5jtfgERa.jpg](https://support.optisigns.com/hc/article_attachments/33979909659027)

Once permission is granted, you can **customize** and **set up** your Google Sheet asset:

![](https://support.optisigns.com/hc/article_attachments/34038249680403)

- **Select Sheet:** Allows you to select a single sheet from within the Google Sheet to display
  - ***Reload Sheets:*** This will refresh the data to get an updated list Sheets available within that entire document for you to choose from.
- **Customize Display Region:** Allows you to input the Start Cell and End Cell to select the region shown on your display.
  - *This **cannot** be unselected or selected once the asset is first saved. If selected upon creating the app, you can continuously adjust the display region whenever you'd like.*
- **Scale:** Adjust how you'd like the Sheet to scale and display on the screen.
- **Orientation:** Choose between Landscape or Portrait
- **Speed:** Adjusts the speed at which data transitions.
  - ***Slow or 5:*** 19 seconds
  - ***Medium or 10:*** 14 seconds
  - ***Fast or 15:*** 9 seconds
- **Force Sync Interval:** System will force sync at the hour interval you select. (*Minimum: 1 hour*)

Once done, Click **Save.**

![](https://support.optisigns.com/hc/article_attachments/33979969438483)

|  |
| --- |
| **App must be saved before changes will appear in Preview.** |

#### Additional Features

After creating your asset, your URL box will now have a **"Refresh Data"** button. This button will update your Google Sheets data to make sure the latest information is shown on your device when clicked.

![](https://support.optisigns.com/hc/article_attachments/33979909670931)

When you update your Sheet, Google will also send a notification to our system, which will either update the new data automatically after 5 minutes, during the set Force Sync Interval, or when you click the Refresh Data button above.

---

## Option 2: Setting Up a Public Sheet

***This method is useful if you want closer to real-time updates on your screen and a sharing experience similar to Google Docs.***

In your Sheet, go to **Files** → **Share** → **Publish to Web** → Click **Publish -> OK.**

![mceclip2 (1).jpg](https://support.optisigns.com/hc/article_attachments/39888202657043)

![mceclip1.jpg](https://support.optisigns.com/hc/article_attachments/39888202658195)

|  |
| --- |
| **If you do not publish AND share your Sheet, OptiSigns will have you go through the authentication process shown in the previous section. An error message may appear telling you the Sheet isn't published** |

**Copy this** **published link** → Return to your Google Sheets app in the OptiSigns portal.

![Screenshot 2025-03-31 at 6.20.55 PM.jpg](https://support.optisigns.com/hc/article_attachments/39888173187987)

**Name** your asset → **Paste the published link** into the URL box.

Click **Next**.

![](https://support.optisigns.com/hc/article_attachments/33979969448083)

**Set up Update Interval:** You can specify in seconds, how often the app should check for updated sheets:

- **Default/Minimum:** 600 seconds
- 0 means it will only check your data when it loads the first time.

Once done, click **Save**.

---

## Limitations

- **Update Intervals:**
  - **Private Sheet:**Google will notify our system when you update your Sheet, and we will reload the information in as little as 5 minutes, up to one hour (or whenever you set your Force Sync Interval).
  - **Published Sheet:** Google updates the webpage automatically every 5 minutes. Your screens should then update in around 5-10 minutes, up to the Force Sync interval (minimum 1 hour).
- **Hidden Sheet:** If you try to import a hidden Sheet, we will not be able to access the content. This will cause the Preview window or Screens to display as black.
- **Custom Display Region:**
  - Currently, it is only supported for Private Sheet.
  - This must be set up during the creation of the asset. Once this is selected for an asset, it cannot be unselected. Or, if you do not select it upon creating the asset, you cannot select it later.
  - If you set up Custom Display Region, you can always adjust the inputted cells and scaling.

---

#### That's it! Your Google Sheets is now set up and ready to go.

Explore what else you can do with Google Sheets below:

- [How to add Google Sheets as a DataSource for OptiSync](https://support.optisigns.com/hc/en-us/articles/29838866920211)
- [How to Display Birthday Lists with OptiSync Data Mapping and Google Sheets](https://support.optisigns.com/hc/en-us/articles/29979283289235)

If you have any questions, please reach out to our Customer Support team at support@optisigns.com
