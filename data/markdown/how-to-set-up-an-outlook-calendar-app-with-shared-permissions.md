# How to Set Up an Outlook Calendar App with Shared Permissions

Article URL: https://support.optisigns.com/hc/en-us/articles/45619214182803-How-to-Set-Up-an-Outlook-Calendar-App-with-Shared-Permissions
Article ID: 45619214182803
Last Updated: 2025-10-17T16:01:18Z

### In this article, we'll go over how to set up Shared Permissions to show Room or Equipment Resources on an Outlook Calendar with OptiSigns.

- [What You'll Need](#WhatYouNeed)
- [Step 1: Granting the Proper Resource Permissions to a User Account](#Step1)
- [Step 2: Displaying the Resource in the User's Outlook Calendar](#Step2)

When using Outlook calendar in an organization, you are often granted access to various calendars. These may be for other individuals, or they may show the availability of certain shared resources, such as Rooms or Equipment.

While OptiSigns currently does not support showing multiple user calendars at once (see our [**Calendar Mix**](https://support.optisigns.com/hc/en-us/articles/4408052949139-How-to-use-Calendar-Mix-app) app for doing that), it is possible to show those Resources. However, specific permissions will need to be granted via your Microsoft Admin account in order to do this.

Let's get started.

---

## What You'll Need

To set up Resource permissions and display them on OptiSigns, you'll need:

- Administrator Access to a Microsoft Business Account
- A Room or Equipment Resource to display
- An OptiSigns[**Standard Plan or higher**](https://www.optisigns.com/pricing)

---

## Step 1: Granting the Proper Resource Permissions to a User Account

To get started, we'll need to open up the [**Microsoft Exchange Admin center**](https://admin.exchange.microsoft.com/#/resources). This is where permissions of this type are handled.

Navigate through the sidebar to the **Resources** tab. Here, select either **Add a Room Resource, Add an Equipment Resource,** or an already made Resource.

![exchange admin center resource example](https://support.optisigns.com/hc/article_attachments/45619197975827)

You'll see that the **Type** displays what type of resource it is, whether Room or Equipment. These resources are distinct from Users, and have different permissions.

Click the Display Name of the resource you want to change the permissions of to continue:

![microsoft room 1](https://support.optisigns.com/hc/article_attachments/45619197976339)

Next, navigate to the **Delegation** tab, then hit **Edit** under the "Read and manage" section:

![microsoft room permissions delegation](https://support.optisigns.com/hc/article_attachments/45619197976723)

On the Manage delegates screen, click **Add Member:**

![](https://support.optisigns.com/hc/article_attachments/45619197981459)

This will open up the "Add read and manage permissions tab." Here, select the Display Name of the user you want to set up OptiSigns with.

![microsoft exchange admin read manage permissions](https://support.optisigns.com/hc/article_attachments/45619197986195)

Hit **Save**. Now we need to make sure the Resource calendar is set up in Outlook.

---

## Step 2: Displaying the Resource in the User's Outlook Calendar

Log in to Outlook with the user you wish to display OptiSigns on. Hit **Add Calendar**:

![microsoft outlook add calendar](https://support.optisigns.com/hc/article_attachments/45619197986323)

Next, click **Add from Directory**, then **Select an Account**.

![microsoft outlook add calendar directory](https://support.optisigns.com/hc/article_attachments/45619197986963)

You'll choose your User account here:

![add from directory choose email](https://support.optisigns.com/hc/article_attachments/45619214166163)

You'll be asked to Select a person, group, or resource from your organization's directory. Find the desired Resource's **email address**. This can be found on your Resources page in your Exchange Admin portal:

![use room email](https://support.optisigns.com/hc/article_attachments/45619197987987)![select room from email](https://support.optisigns.com/hc/article_attachments/45619197989011)

Once it has been found and entered, it will appear on the list:

![room resource on list](https://support.optisigns.com/hc/article_attachments/45619214169875)

When you try and exit, you'll be asked to Save changes. Do so.

![save changes to outlook calendar](https://support.optisigns.com/hc/article_attachments/45619214170515)

Now the Resource's calendar will populate on this User's calendar display.

From here, follow the normal instructions on [Setting Up a Microsoft Outlook Calendar with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360036250853-How-to-use-Microsoft-Outlook-Office-365-Calendar-with-OptiSigns) to get your Calendar up and running.

### That's all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
