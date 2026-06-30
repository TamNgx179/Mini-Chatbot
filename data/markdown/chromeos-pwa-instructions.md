# ChromeOS PWA Instructions

Article URL: https://support.optisigns.com/hc/en-us/articles/49039295567891-ChromeOS-PWA-Instructions
Article ID: 49039295567891
Last Updated: 2026-05-05T15:48:27Z

### In this article, we will show how to set up OptiSigns on ChromeOS devices. This can be used for mass provisioning across numerous Chrome boxes without the use of any Chrome apps.

- [What You'll Need](#WhatYouNeed)
- [Adding OptiSigns Player to a Google Admin Account](#AddingOptiSigns)
- [Adding the OptiSigns Player App as an Extension](#Extension)
- [Mass Provisioning ChromeOS Devices (OPTIONAL)](#MassProvisioning)
  - [Creating a Mass Provisioning Template on OptiSigns](#Creating)
  - [Adding to Extension Policy and Applying to OptiSigns Player](#ExtensionPolicy)
- [Adding OptiSigns Player to a Private Account](#PrivateAccount)

Chrome boxes are common for large-scale digital signage deployment as there are industrial-grade chrome boxes such as [AOpen Commercial Chromebox](https://amzn.to/33Zcu22) or [ASUS Chromebit](https://amzn.to/2FS8FDP).

Chrome devices are very stable, and provide excellent performance, they can also be managed by Google Chrome Device Management which will simplify your large-scale deployment, ensure enterprise security, and reduce device management overhead. You can learn more about Google's Chrome Device Management [here](https://support.google.com/chrome/a/answer/1289314?hl=en#:~:text=Enforce%20policies%20and%20manage%20apps&text=You%20can%20make%20Wi%2DFi,Manage%20policies%20for%20Chrome%20devices.).

Displaying OptiSigns on a ChromeOS device consists of these broad steps:

1. Adding OptiSigns Player to your Google Admin account
2. Adding the OptiSigns Player app as an extension
3. Mass Provisioning devices (optional)
4. Pushing Content to Your ChromeOS Device

---

## What You'll Need

- An OptiSigns [**Standard plan or higher**](https://www.optisigns.com/pricing)**\***
- [Chrome Enterprise Single App](https://chromeos.google/products/device-management/) licenses per device
- A Google Administrator account with administrator access
- ChromeOS devices, [**enrolled in Google Admin Console**](https://support.google.com/chrome/a/answer/1360534?hl=en)

\* In order to use touch screen functions, you will need an Engage Plan.

---

## Adding OptiSigns Player to a Google Admin Account

To begin, go to [**Google Admin**](http://admin.google.com).

Now go to **Device** → **Chrome** → **Apps & Extensions** → **Kiosks**.

![chrome os setup part one](https://support.optisigns.com/hc/article_attachments/49039295530643)

On the bottom left, click the **+ symbol**. Then, choose **Add by URL**.

![chromeos setup add by url](https://support.optisigns.com/hc/article_attachments/49039295533587)

Now copy and paste our OptiSigns PWA URL ([webapp.optisigns.com](https://webapp.optisigns.com)) into the open window. Click **Save**.

![chromeos add by url window](https://support.optisigns.com/hc/article_attachments/50218174250259)

The OptiSigns app will appear as a Kiosk app:

![chromeos setup optisigns app in window](https://support.optisigns.com/hc/article_attachments/50218174254355)

---

## Adding the OptiSigns Player App as an Extension

Now that OptiSigns is registered, we need to add it as an extension. Click on the **OptiSigns App** and scroll down the list on the right until you see **Add Extension**.

![chromeos app adding extension](https://support.optisigns.com/hc/article_attachments/50218184677139)

Click this button and choose **Add from Chrome Web Store:**

![add extension from chrome web store](https://support.optisigns.com/hc/article_attachments/50218174257043)

Now, find the **OptiSigns Digital Signage** app in the Chrome Web Store. Input **foendllmjcjfmcpfkkeinenelpnoinoc** in the **"Search by ID"** field. Then hit **Select.**

![optisigns chrome web store search for id](https://support.optisigns.com/hc/article_attachments/50218174262931)

Now, you should see that the OptiSigns Digital Signage app has been added to your extensions

![optisigns as chromeos extension](https://support.optisigns.com/hc/article_attachments/50218174266003)

Technically, your ChromeOS devices are now configured, and can be treated like any other screen in OptiSigns. Follow our [**Getting Started**](https://support.optisigns.com/hc/en-us/articles/18823504383891-OptiSigns-Getting-Started-Guide)guide to pair the device in OptiSigns, upload content, then get your displays working!

---

## Mass Provisioning on ChromeOS Devices (optional)

Mass provisioning requires two steps:

1. Creating a mass provisioning template on the OptiSigns Portal
2. Adding the JSON of that template into your Policy for Extensions area in Google Admin

Let's do it.

### Creating a Mass Provisioning Template on OptiSigns

To create a provisioning template, go to the OptiSigns portal and go to the **Username** → **More** → **Provisioning Templates**.

![provisioning templates](https://support.optisigns.com/hc/article_attachments/50218184695315)

Hit **Create New Provisioning Template:**

![optisigns create provisioning template](https://support.optisigns.com/hc/article_attachments/49041868805267)

You'll be asked to set up the template.

![provisioning template creation window](https://support.optisigns.com/hc/article_attachments/49039280054419)

- **Template Name**: Name of your template, this is for you to distinguish it when you have multiple provisioning templates.
- **Device Name Prefix**: This is used to generate the device name during provisioning.
- **Device Name Suffix**: This is used to generate the device name during provisioning, the default setting will add timestamps as a suffix.
- **Folder**: The folder you want to have the provisioned devices to be created.
- **WIFI**: Select from the stored WIFI, need to be created first. Only required if you want to setup WIFI during provisioning. WIFI setup is normally not needed for ChromeOS deployment. Because the deployment will be managed through Chrome Device Management.
- **Time Zone**: Specify the time zone of the device.
- **Tags**: Specify the tags you want to associate to the devices.
- **Initial Default Content Type**: Used to set the initial content on the device after provisioning.
- **Orientation**: Set the orientation, landscape is the default.
- **Sync Play**: Used to set the turn on/off of the sync play feature. For more details of Sync Play feature, please click [here](https://support.optisigns.com/hc/en-us/articles/4412065189267-Synchronized-playback-Sync-Play-feature).
- **Location**: Set the location of the device.

#### Advanced

![advanced creation window](https://support.optisigns.com/hc/article_attachments/49039280055571)

- **If device already paired**: Provides options for devices which have already been paired in OptiSigns and how to handle that:

![wifi options](https://support.optisigns.com/hc/article_attachments/49039295547411)

Once the template is created, it will be available under the list of provisioning templates. You can download the config file and it will be available for deployment. Click **Download**, then **ChromeOS**.

![adding chromeos to provisioning template](https://support.optisigns.com/hc/article_attachments/49039295552531)

Your configuration file will be "provisionting-template-<Your Template Name>.txt".

This file contains a JSON object. This is what you will need to set up auto-provisioning in the next step.

![](https://support.optisigns.com/hc/article_attachments/49039295553299)

---

### Adding to Extension Policy and Applying to OptiSigns Player

Now, go back to [**Google Admin**](http://admin.google.com) and navigate back to the **Apps & Extensions** menu.

Click the **OptiSigns extension** then

![optisigns provisioning id](https://support.optisigns.com/hc/article_attachments/49039295555347)

Your JSON value will now appear in the field:

![optisigns provisioning json](https://support.optisigns.com/hc/article_attachments/49039280067219)

Save it!

Now your ChromeOS devices are provisioned. Follow our [**Getting Started**](https://support.optisigns.com/hc/en-us/articles/18823504383891-OptiSigns-Getting-Started-Guide)guide to pair the device in OptiSigns, upload content, then get your displays working!

---

## Adding OptiSigns Player to a Private Account

If you don't have a Google Admin account, you can still get the OptiSigns PWA to work on ChromeOS devices. Just follow these steps.

First, go to the Chrome Web Store and **Search extensions and themes:**

![](https://support.optisigns.com/hc/article_attachments/50288483048467)

Search **OptiSigns Digital Signage** and select it.

![](https://support.optisigns.com/hc/article_attachments/50288515530899)

Click **Add to Chrome** and wait for it to install.

![](https://support.optisigns.com/hc/article_attachments/50288483061523)

You can go to **My Extensions** to see if it successfully downloaded:

![](https://support.optisigns.com/hc/article_attachments/50288515539091)

Now you can launch OptiSigns from the ChromeOS launcher on any ChromeOS device (TV, etc.):

![](https://support.optisigns.com/hc/article_attachments/50288483065875)

This will allow OptiSigns to run!

### That's all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
