# How to Display Microsoft Power BI Dashboards & Reports with OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/360024859713-How-to-Display-Microsoft-Power-BI-Dashboards-Reports-with-OptiSigns
Article ID: 360024859713
Last Updated: 2026-03-25T21:24:00Z

### In this article, we will show how to display Microsoft Power BI dashboards and reports on TVs and screens using OptiSigns.

- [What You'll Need](#WhatYouNeed)
- [Prepare Dashboard or Report for Sharing](#PrepareDashboard)
  - [Dashboard Hosted on Microsoft 365](#Microsoft365)
  - [Dashboard from Power BI Desktop App](#DesktopApp)
- [Add Power BI App on OptiSigns](#AddPowerBI)
- [Filtering a Report](#Filtering)
  - [Creating a Basic Filter](#BasicFilter)
  - [Creating a Filter to Automatically Target Certain Screens (Optional)](#AutomaticFilter)
  - [Saving and Loading Filters (Optional)](#SavingandLoading)
- [Frequently Asked Questions](#FAQs)
  - [How does security work with OptiSigns Power BI integration?](#PowerBIintegration)
  - [How do I set up a Power BI service principal with OptiSigns?](#ServicePrincipal)
  - [How can I edit the size of the screen on my display?](#SizeofScreen)
  - [I'm having trouble displaying my Power BI report off MS Fabric.](#Fabric)
  - [My embedded Power BI report shows on my portal, but won't display on my screen. Help?](#WontDisplayOnscreen)
  - [My Power BI report lags and crashes frequently. Why?](#LagsandCrashes)
  - [Power BI Display for US Government Customers](#USGovernment)

|  |
| --- |
| **NOTE** |
| The **Power BI app** is available to customers with a **Pro Plus plan or above**. |

OptiSigns boasts integration with Microsoft Power BI, allowing secure sharing of PowerBI Dashboards and Reports to large TVs and screens. This improves communication and information sharing across office spaces.

---

## What You'll Need

- An OptiSigns [Pro Plus plan](https://www.optisigns.com/pricing) subscription or above
- A screen, [set up and paired](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv) with OptiSigns
- A valid Microsoft username and password
- Appropriate Power BI Administrative permissions
- A Power BI URL

---

## Prepare Dashboard or Report for Sharing

We'll assume you already have a Power BI dashboard or report built out and ready to showcase to your team members or audience on a large screen.

### Dashboard Hosted on Microsoft 365

If your report or dashboard is hosted on **Microsoft 365**, simply copy the URL link in your Power BI dashboard.

![power bi desktop url](https://support.optisigns.com/hc/article_attachments/37495309620627)

|  |
| --- |
| **NOTE** |
| Make sure to use the URL from the browser address bar. The link from Report Share is a dynamic link, and is not a valid identifier for the dashboard. |

This URL is what you'll need to set up the Power BI app [in the next step.](#AddPowerBI)

### Dashboard from Power BI Desktop App

If your report or dashboard was created using the **Power BI Desktop app**, you need to click **Publish** from the top menu.

![publish button from power bi desktop app](https://support.optisigns.com/hc/article_attachments/37495325626515)

Select the Workspace where you want to publish it.

|  |
| --- |
| **IMPORTANT** |
| Your report must be in a group different from "My workspace" |

![workspace publish power bi](https://support.optisigns.com/hc/article_attachments/37495309627795)

Once it has successfully published, click on Open in Power BI and will be redirected to your report or dashboard.

![publishing to power bi](https://support.optisigns.com/hc/article_attachments/37495309647123)

Copy the URL in your Power BI dashboard.

![copy url power bi dashboard](https://support.optisigns.com/hc/article_attachments/37495309653267)

This URL is what you'll need to set up the Power BI app [in the next step.](#AddPowerBI)

---

## Add Power BI App on OptiSigns

Now, it's time to add an instance of the Power BI app to your OptiSigns account.

Navigate to the [**OptiSigns Portal**](https://app.optisigns.com/)**,**then click **Files/Assets** → **Apps**.

![optisigns files assets apps](https://support.optisigns.com/hc/article_attachments/37495309686163)

Navigate to the **Power BI app**.

![optisigns power bi app location](https://support.optisigns.com/hc/article_attachments/37495309693203)

Enter your Power BI app details.

![](https://support.optisigns.com/hc/article_attachments/44002355209107)

- **Name -** Name of your Power BI app instance. This is the name of the app in your asset list. It will **not** be displayed on your screens.
- **URL -**  Paste in the Dashboard URL you copied in Step 1 here.
- **Update Interval -** Select how often you want the app to check for an update to the Dashboard. The Default is 600 seconds (10 minutes).
- **Use Service Principal -** When selected, uses a Microsoft Entra ID Service Principal to log in to Power BI. This requires additional setup. For more information, see [How to Set Up a Power BI Service Principal for Use with OptiSigns](https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-PowerBI-Service-Principal-for-Use-in-OptiSigns).
  - **Select the "User Service Principal" Integration** - Where you choose the service principal integration for your Power BI reports.
- **Direct Login -** In order to view your dashboard on any screen, OptiSigns requires you to authenticate via the pass-through to Microsoft's Power BI service. Simply input your Microsoft ID and password.

Once you've integrated a Service Principal or directly logged in, you're ready to display. On the right is the **Preview** pane. If you've set up your report correctly, you should see it display here. You can change its orientation by switching between **Landscape** and **Portrait**.

|  |
| --- |
| **NOTE** |
| A successful Preview will prove that your Power BI report has properly integrated with OptiSigns. However, it **DOES NOT** mean that it will display on your screen the same way. A variety of additional factors can affect how your Power BI displays, including (but not limited to):   - Type of device being used to display - Device memory - Reliability of network connection - Company firewalls and other network restrictions   If you're still having trouble getting your Power BI reports to display after all these have been accounted for, please contact us at [support@optisigns.com](mailto:support@optisigns.com). |

If it appears to your satisfaction, you can choose to assign your Power BI app instance either directly to a screen or as part of a [Playlist](https://support.optisigns.com/hc/en-us/articles/28295104605843-How-to-Create-Use-Playlists) and/or [Schedule](https://support.optisigns.com/hc/en-us/articles/360016981853-Create-and-Using-Schedules-with-OptiSigns).

This instance will display a single page of a report. You will need to create multiple instances to show multiple pages of a report. These can be placed into a Playlist to have a constantly rotating series of slides showing entire reports or dashboards, or sprinkled in with other Assets - however you like.

---

## Filtering a Report

If you only wish to display certain pieces of data on your report, you can create Filters within the Power BI app.

### Creating a Basic Filter

For a basic filter, create a Power BI app or open an existing one and open the **Advanced Settings** at the bottom.

![](https://support.optisigns.com/hc/article_attachments/44002355213715)

To create a filter, we’ll need three key pieces of information from your report: a **Table**, a **Column**, and a **Value**.

![](https://support.optisigns.com/hc/article_attachments/44002377534611)

To find these, go to the report you wish to use. Click **Edit**.

![](https://support.optisigns.com/hc/article_attachments/44002377537299)

A number of options will appear on the right side. Under the **Data** tab, you should see a number of folders and subfolders. The folders correspond to the **Table**, the subfolder the **Column**. When selected, there will be a number of names in a properly configured report in the **Filters** column. These are your **Values**. See the image below for a better visual reference.

![](https://support.optisigns.com/hc/article_attachments/44018968307347)

In this example, we’ll use **Account** as our Table, **Region** as our Column, and **Central** as our filter Value. Simply fill that in to the Filter.

![](https://support.optisigns.com/hc/article_attachments/44002377545747)

There is one last step. We need to set our variable, which corresponds to the field between the Column and the Value. This is clickable, and there are many options:

![](https://support.optisigns.com/hc/article_attachments/44002377551635)

This gives you a great degree of customizability on how you wish to set up your Filter. For our example, we’ll keep the value as **Is**. This means that it will only show data corresponding to that Table, Column, and Value.

If this is all you need, great. You’re done! Simply hit **Save** and your filter will apply. However, it’s also possible to add additional conditions to a filter, or to create more than one per report.

To add additional conditions to a basic filter, hit the **+** button next to it.

![](https://support.optisigns.com/hc/article_attachments/44002377555603)

You can change the condition logic between **AND** and **OR** to specify what type of filter to apply. Then, set the variable and value. You can continue adding additional conditions if you wish.

To add a completely new filter, hit **Add New Filter**.

![](https://support.optisigns.com/hc/article_attachments/44002355238035)

This will (shockingly) create a new filter. Fill this out as you did your first one, with the information you wish to show.

![](https://support.optisigns.com/hc/article_attachments/44002377558675)

### Creating a Filter to Automatically Target Certain Screens (Optional)

By pairing these filters with OptiSigns [**Device Additional Attributes**](https://support.optisigns.com/hc/en-us/articles/360048914673-Edit-Screen-What-does-each-option-do#attributes), it is possible to apply them only to certain screens. This is useful if you have multiple screen locations, for example, and only wish to show Power BI data which is relevant to them.

To set this up, navigate to the **Device Additional Attributes** by editing your screen. This can be found through the **Screens tab,** then finding the screen you wish to Edit. Click **Edit Screen → Advanced → More → Device Additional Attributes**.  
![](https://support.optisigns.com/hc/article_attachments/44002355241875)

Here’s where it gets fun. On the Device Additional Attributes screen, you’ll see two fields: **Key**, and **Value**.

![](https://support.optisigns.com/hc/article_attachments/44002377564179)

- **Key** - A parameter that will be used by the filter. This will replace either the Table, Column, or Value, as you’ll see in a moment. You’ll want to keep your Key consistent across ALL screens where you plan to display a filtered Power BI report.
- **Value** - Dictates which part of the report to share with this screen. You’ll want this to vary depending on the screen.

For this example, we will fill in the Key as **Location** and the Value as **Central**:

![](https://support.optisigns.com/hc/article_attachments/44002355249939)

For practical purposes, what we’re saying here is that this screen’s Location is in the Central region, which corresponds to the Values which exist on our Power BI report. You can add as many attributes to an individual screen as you wish.

|  |
| --- |
| **IMPORTANT** |
| The Value here MUST match up with an element of your report if you wish to apply the filter properly. In our example report, we have Central, East, and West, so one of these must be the value for the report to display properly. Your report will be different. |

Now that we’ve set this up, we can return to our Power BI report. Now, we’ll substitute the **Value** for **{{Location}}**:

![](https://support.optisigns.com/hc/article_attachments/44002377569939)

By inputting this and assigning this to a screen, it will find the Device Additional Attribute and substitute the Value here. In this case, that value is Central, so it will filter out all data that does not fall under the Account Table, Region Column, and Central Value.

For a different screen, you might set the Device Additional Attribute value to East. By pairing this same report to that screen, it will filter out all data that does not fall under the Account Table, Region Column, and East value.

Let’s see how this works with a practical example:

- Say we have 3 screens in 3 locations:
  - Screen A is in Location 1, Screen B is in Location 2, and Screen C is in Location 3
- We only want these screens to show the appropriate data off this report
  - On each screen, we go to Device Additional Attributes. We set Key as Location and the Value as Location 1 for Screen A; Location 2 for B; and Location 3 for C
  - We set the Value in our Power BI report to {{Location}}
- It will automatically filter the report based on the device’s set location, and this app can be used across all 3 screens and will show different data depending on where the screen is located

Pretty cool, huh? This can also be used to replace the Table or Column values depending on your use case or need.

### Saving and Loading Filters (Optional)

It’s also possible to Save your filters for use when creating another Power BI app.

To do this, simply create your filter, then hit the **Save Filter** button:

![](https://support.optisigns.com/hc/article_attachments/44002355256339)

This will bring up the **Save Your Filter Settings** menu.

![](https://support.optisigns.com/hc/article_attachments/44002355262611)

Give your filters a name and a description, then hit **Save My Filters**. This will save this filter on the Account Level. It can then be loaded by hitting the **Load Filter** button:

![](https://support.optisigns.com/hc/article_attachments/44002377583251)

These filters can be edited directly from this menu:

![](https://support.optisigns.com/hc/article_attachments/44002355268755)

Any edits made will apply everywhere this filter is applied.

---

## Frequently Asked Questions

#### **How does security work with OptiSigns Power BI integration?**

OptiSigns integrates with and displays Power BI dashboards via an official Microsoft API, securely integrated through your Power BI or MS Azure portal. No usernames or passwords are stored in OptiSigns.

Your devices (screens) will display your Power BI report on the screens directly. Power BI data does not pass through our servers. There is no data-farming on our end of any kind.

OptiSigns uses Microsoft APIs for integration. In order for our integrations to work, the integration has to be approved by an administrator. This is the same across all integrations using Microsoft APIs.

This administrator access is only needed for first time access. Once the OptiSigns app is approved for use, other users can use OptiSigns directly.

Customers with MS Azure Enterprise Apps management can also [manage OptiSigns in your Enterprise App](https://support.optisigns.com/hc/en-us/articles/4403616315539) for even more control over security options.

#### **How do I set up a Power BI service principal with OptiSigns?**

We have an entire article dedicated to this process! Please see:

- [Set Up a Power BI Service Principal for Use in OptiSigns](https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-PowerBI-Service-Principal-for-Use-in-OptiSigns)

Please note that the service principal option is only available to customers with an **Enterprise** plan.

#### **How can I edit the size of the screen on my display?**

To make sure your Power BI app displays properly, go to **View** within the Power BI application you want to display. Then hit **Fit to Page**.

![power bi fit to page](https://support.optisigns.com/hc/article_attachments/37192704471315)

Certain display devices may have additional requirements for displaying the report at the proper resolution. For example, mobile devices display at a different resolution than typical HD devices, and so some display issues may arise when setting reports to display on a mobile device.

In addition, certain hardware is not optimized for displaying Power BI. In these cases, we recommend our [OptiSigns Android Player](https://www.optisigns.com/product/hardware/android-player), which guarantees the best support for our software and Power BI in particular.

If issues persist, we recommend contacting our support team at [support@optisigns.com](mailto:support@optisigns.com).

#### **I'm having trouble displaying my Power BI report off MS Fabric.**

If you have a Power BI report created off MS Fabric, you'll need to make a slight tweak to the URL to get it to display using OptiSigns.

If created on Fabric, your Power BI URL should begin: **app.fabric.microsoft.com**

Simply change this to: **app.powerbi.com** while keeping all other parameters the same. This should fix any display issues.

#### **My Power BI report displays on my portal, but won't display on my screen. Help?**

This issue is usually caused by network connectivity issues at the device. We recommend checking and validating your device/screen's network connection.

If you have a Samsung SSSP or LG WebOS TV, there might be a different issue. Microsoft requires a minimum Chromium version of 95 for their apps to display. These TVs typically don't update very often. This is a Microsoft issue, and there is little we can do on our end.

If you have one of these TVs and wish to display SharePoint, we recommend our [Android Player](https://www.optisigns.com/product/hardware/android-player).

If you're still having issues, feel free to contact our support team at [support@optisigns.com](mailto:support@optisigns.com).

#### **My Power BI report lags and crashes frequently. Why?**

Lagging and crashing Power BI reports usually have to do with two factors:

- The device being used to run the OptiSigns app and display the report
- The size of the report

Simply put, the larger the size of the report, the more powerful device you'll need to display it without issue. Small reports can use weaker hardware, while large and sprawling reports will need more powerful or dedicated hardware.

This means, if you're having this issue, you'll need to either:

1. Reduce the size of the report you want to display
2. Improve the hardware you're using

We recommend using an [**OptiSigns Pro Player**](https://www.optisigns.com/product/hardware/pro-digital-signage-player)or [**OptiSigns ProMax Player**](https://www.optisigns.com/product/hardware/promax-digital-signage-player)for displaying large, heavy Power BI reports.

#### **Power BI Display for US Government Customers**

If you are a US government entity (federal, state, or local), you may be using Power BI for government. If so, your Power BI reports will use one of these URLs:

- **GCC**: `https://app.powerbigov.us`
- **GCC High**: [`https://app.high.powerbigov.us`](https://app.high.powerbigov.us)

If that is the case, your display won't work with the Power BI app. However, it is possible to create your Power BI as a Sharepoint application, then display it with our [**SharePoint app**](https://support.optisigns.com/hc/en-us/articles/4414539282067-Displaying-SharePoint-Sites-on-OptiSigns)**.**

### That's all!

OptiSigns is the leader in [digital signage software.](https://www.optisigns.com/) If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)

**For additional assistance with Power BI usage**  
Check out this guide here:  
[Publish and share in Power BI](https://docs.microsoft.com/en-us/power-bi/guided-learning/publishingandsharing?tutorial-step=11)
