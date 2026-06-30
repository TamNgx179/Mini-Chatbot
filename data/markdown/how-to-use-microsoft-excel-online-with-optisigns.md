# How to use Microsoft Excel Online with OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/4529298306963-How-to-use-Microsoft-Excel-Online-with-OptiSigns
Article ID: 4529298306963
Last Updated: 2025-08-29T19:58:56Z

Microsoft Excel is a very popular ways to create and share your spreadsheet. You can also use it on your Digital Signage screen.

There are 2 ways to use Excel with OptiSigns:

1) Upload the XLSX file, and OptiSigns will convert and display on your screen (pros: can play offline, just upload files, cons: when there are changes, you need to upload the files again)

![](https://support.optisigns.com/hc/article_attachments/43351529194259)

2) Use Excel for Web (online) (pros: **you can make changes to the Excel file and screens will update automatically**, cons: need internet connection to display)

This article will walk you through how to set up option 2:

Upload your Excel to OneDrive and changes to your Excel can be automatically updated on your screens.

![excel spreadsheet example](https://support.optisigns.com/hc/article_attachments/4542287976595)

If this is your first time using OptiSigns, you can [read here](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv) to get set up.

Otherwise, let's dive in.

## **1) Create and prepare your Excel**

First, we need to make sure your spreadsheet will fit on a single page. To do this, go to the **Page Layout**tab, then locate the **Scale to Fit**area. Here, for the **Width**, keep it to **1 page**, then set **Height**to **however large your spreadsheet is**.

![image (33).jpg](https://support.optisigns.com/hc/article_attachments/42892845437075)

Then upload your Excel file to your Microsoft OneDrive. If you're using the Web version of Excel, you can skip this step.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4542330886931)

Then on the **File** tab of the Ribbon, click **Share.**Make sure the Link Settings are set to **Anyone**:

![](https://support.optisigns.com/hc/article_attachments/38674935152787) Now click **Share** again, then click **Embed**.

![blobid3.png](https://support.optisigns.com/hc/article_attachments/4542332041363)

To create the HTML code to embed your file in the web page, click **Generate.**

Under **Embed Code**, right-click the code, click **Copy**, and then click **Close**.

![blobid4.png](https://support.optisigns.com/hc/article_attachments/4542332693139)

## **2) Add Excel Online App on OptiSigns**

Go to our portal: <https://app.optisigns.com>

Click File/Assets, then click Apps, search and select Excel Online app.  
![blobid0.png](https://support.optisigns.com/hc/article_attachments/4542218518675)

There are two options to enter your Microsoft Excel.

- Copy and paste your Microsoft Excel embed code directly.
- Sign in with your Microsoft account, and select your Excel file.

**Option 1: Copy and paste your Microsoft Excel embed code directly.**

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/11412898232211)

Name: for you to remember, you can use the same Excel file name.  
Embed: Paste in your Embed Code.  
Update Interval: default is 600 seconds (10 minutes). This means the app will refresh the link every 10 mins for any changes in your spreadsheet.

Click Save

**Option 2: Sign in with Microsoft Account**

|  |
| --- |
| **NOTE** |
| As of July 2025, Microsoft has created a limitation which only allows Excel sheets under **1 MB**to be uploaded in this manner. If you have an Excel sheet you'd like to display that is larger than 1 megabyte, we suggest **Option 1**. |

**![](https://support.optisigns.com/hc/article_attachments/21661672438547)**

- Name: This is the name to organize assets, it will not be shown on the screen.
- URL: This is the Excel link that is auto-generated.
- Customize Display Region: Select a specific region in your file to be displayed on your screens. The asset must be saved first before the feature is enabled.
  - If enabled, click on 'Select Display Region' and then click on the sheet page to select display region.

![](https://support.optisigns.com/hc/article_attachments/21661758082707)

- Speed: Select how fast you want the slide to switch between slides. You can also customize your speed if you select Custom.

**(Important Note: Please allow “popup” on your browser. You will able to log in and open the folder/file picker.)**

**Advanced option:**

With logging in with a Microsoft account, you have the option to set up Force it refreshes.

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/11412902362771)

Force Sync Interval: By default, the system will force sync every 12 hours. The minimum is 1 hour.

Click Save.

**That's it,** you have created an Excel Online.  
Anytime changes are made to the Excel Online workbook, the screens will be updated by the update intervals.

|  |
| --- |
| **IMPORTANT** |
| The total file size for an OptiSigns Excel app **cannot exceed 105 MB** and still display onscreen. This is due to a limitation by Microsoft. |

### Why does using Excel require giving OptiSigns Admin permission to use?

OptiSigns uses Microsoft APIs for integration. In order for our integrations to work, the integration has to be approved by an administrator. This is the same across all integrations using Microsoft APIs.

This administrator access is only needed for first time access. Once the OptiSigns app is approved for use, other users can use OptiSigns directly.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
