# How to Set Up Dynamic Data Mapping with OptiSync

Article URL: https://support.optisigns.com/hc/en-us/articles/29217646663187-How-to-Set-Up-Dynamic-Data-Mapping-with-OptiSync
Article ID: 29217646663187
Last Updated: 2025-09-04T17:54:40Z

### In today's fast-paced digital environment, manually updating digital displays can be both tedious and error-prone. This guide will show you how to integrate live data into your digital screens, allowing for seamless automatic updates across your displays.

**In this article:**

- [What is OptiSync?](#What)
- [Adding Your Data Source](#Adding)
- [Inputting Your Data Source in Designer](#Inputting)
- [Editing and Designing Your Repeater in Designer](#Editing)
  - [How to use the Property Mapping Feature](#Property)
  - [How to use Display Format Options](#Display)
- [Push to Screens](#Push)

|  |
| --- |
| Note: OptiSync is only available on Pro Plus and above plans. |

## What is OptiSync?

OptiSync is an integrated solution designed to seamlessly connect with various data sources, including spreadsheets, APIs, and tables.

**Key Features:**

- **Easy Setup:** Setting up your data source requires low code or no code, ensuring a quick and straightforward process.
- **Automatic Updates:** You can link your data source directly to our Designer app, which will automatically update your content.
- **Real-Time Data:** This ensures your digital display always reflects the latest data, eliminating the need for manual entry, reducing errors, and saving time.

**Use Cases:**

OptiSync is ideal for a wide range of use cases, such as:

- Displaying employee birthdays
- Restaurant menus
- Work anniversaries
- Product catalogs
- Team introductions
- And, many more!

With OptiSync, your digital displays remain accurate and up-to-date, enhancing communication and engagement in various settings.

## Adding Your Data Source

You can add your data source through **Account Settings** or through **Designer app**.

**Account Settings**

- Click on your account name in the top right corner
- Select **More**
- Select **DataSources**
- Select **Add DataSource**
- Choose your data source from the list of options and follow the instructions on how to import it
  - *If you fully open your account settings, it will be under "Advanced" in the column on the left*

**Designer App:**

- Open the Designer App
- Select **DataSources** from the column on the left
- Select **Add DataSource**
- Choose your data source from the list of options and follow the instructions on how to import it

You can add any data source, such as an Excel sheet, Google Sheet, POS system, inventory management system, HRIS, or other systems. You can also create a table directly in OptiSigns.

![](https://support.optisigns.com/hc/article_attachments/29687726573203)

**Please follow these guides to upload different kinds of DataSources:**

- [How to add Google Sheets as a DataSource for OptiSync](https://support.optisigns.com/hc/en-us/articles/29838866920211)
- [How to add a Microsoft 365 Excel Spreadsheet as a DataSource for OptiSync](https://support.optisigns.com/hc/en-us/articles/29863080711059)

In addition, you can integrate and test API requests, and execute any necessary pre- or post-request coding.

![](https://support.optisigns.com/hc/article_attachments/29217646654099)

Once your data source is set up, you can see **Where Used,** **Edit** the data source, and/or **Duplicate** it.

![](https://support.optisigns.com/hc/article_attachments/29689445946003)

- **Where Used:** This will show you which of your designs are using this Data Source. This is useful to track the use of this data source across different assets.
- **Edit Data:**Go into your data source and make any updates/changes.
- **Duplicate:**This will create a copy of your data source.

![](https://support.optisigns.com/hc/article_attachments/29689413996947)

## Inputting Your Data Source in Designer

Once your Data Source is set up, you can connect it to the Designer app.

Go to **DataSource** on the left side of the Side Menu.

![datasource location designer](https://support.optisigns.com/hc/article_attachments/42703178733715)

As previously mentioned, you can add your DataSource here. Or, if you have already created it in the Data Source section of **Advanced**, then it should show up under **Other DataSources**.

**Select** your data source.

**Drag and drop** the data source elements onto the Designer canvas.

- You can either drag and drop an entire Row or the individual aspects within the rows.

A pop-up message will appear, asking "**Would you like to use this data in a Repeater or on its Own?**"

![on its own vs repeater gif](https://support.optisigns.com/hc/article_attachments/42703178736787)

- **Use on its own:** It will be an element on its own and will update automatically based on the data source.
- **Use in a Repeater:** This will include the data source element in a Repeater component.
  - **Repeater** is a tool that can be used on the Designer application to display and repeat a list of items dynamically.

|  |
| --- |
| **IMPORTANT** |
| OptiSync does not support special characters (i.e. anything outside the scope of an English-language keyboard). This will cause the system data to read as blank, and it will not show. |

## Editing and Designing Your Repeater in Designer

You can edit both the template and the Repeater in Designer!

**The Repeater can be found on the side menu of the Designer application.**

![](https://support.optisigns.com/hc/article_attachments/42705270085523)

Within the Repeaters section, it will contain several ready to use "**Repeater components**" and "**Repeater Templates.**"

|  |
| --- |
| What is the Difference Between the two? |
| **Repeater Component:** designed to manage and display repeating elements along with some design elements. You can incorporate this Repeater component into any template design of your choice—it doesn't need to be a Repeater template. Once added, you simply connect it to your data source. Think of it as a widget that can be easily implemented and customized across different designs to dynamically display data. |
| **Repeater Template:** specifically designed to display repeating elements within a predefined template or design layout. Like other templates, it will replace any existed design when applied. You can still make edits and changes as desired. Again, users will only need to download it and connect to your desired data source. |

Any of these elements can have a DataSource mapped to them, then be edited in the same manner as any other Designer component.

For more information on this, see our guides:

- [**Getting Started with Designer**](https://support.optisigns.com/hc/en-us/articles/42087942047379-Getting-Started-with-Designer)
- [**Photos, GIFs, and QR Codes**](https://support.optisigns.com/hc/en-us/articles/42526907045651-Photos-GIFs-and-QR-Codes-in-Designer)
- [**Customizing Text**](https://support.optisigns.com/hc/en-us/articles/42157810188179-Customize-Text)
- [**Shapes and Elements**](https://support.optisigns.com/hc/en-us/articles/42307234534547-Shapes-and-Elements)

You can also adjust the formatting of a Repeater by selecting it, then selecting **Settings**.

![](https://support.optisigns.com/hc/article_attachments/42705270087059)

This will open up the **Data Mapping**section for the Repeater on the Side Menu:

![](https://support.optisigns.com/hc/article_attachments/42705284276243)

Then, these options will be presented:

- **Replace DataSource:** Change your DataSource
- **Manage:** Make changes to your DataSource's information.
- **Filter:** Apply condition based filters on the DataSource. Filter conditions can be applied using fixed value or device attributes.
- **Disconnect:** Disconnect your DataSource from the Repeater
- **Empty Data Handling:** When there is no DataSource element, the default behavior is to use a blank value. You can adjust this with the following options:
  - **Skip:** Skip it, or get rid of additional repeater items if there isn't enough data to reach the set "Total Items displayed per Page".
  - **Use Default Value:** Show default content, which is what your Repeater element looks like by itself.
  - **Use Blank:** The Repeater will show nothing.
- **Spacing Betwee****n** **Items:**Increase or decrease the space between the Repeater items.
- **Item Display Direction:** Change the positioning of the rows from your DataSource within the Repeater items.   
  - **Left To Right**: It will display the rows going from left to right.
  - **Top To Bottom**: It will display the rows going top to bottom.
- **Item Display Alignment:** Change the alignment of the remaining element items (less than the configured items) to be aligned left/center/right or top/center/bottom.
- **Total Items Displayed per Page:** Increase or decrease how many Repeater items you'd like to be shown.
- **Maximum Items in Each Row/Column:** Increase or decrease how many Repeater items you'd like shown in each row/column.
- **Additional Row/Column Spacing:** Increase or decrease the spacing between rows/columns.
- **Duration (seconds):** Adjust the duration of time for how long each Repeater item is shown before.
- **Shuffle:** Randomly shuffle the items in your DataSource to be displayed on the Repeater.

If you edit a Repeater, it will replicate your updates for each instance of data in the dataset.

- This allows for a consistent look across similar elements without the need to design each one individually.

If you want to use a specific Repeater Template or Component, and would like to update the sample DataSource to one of your DataSources, please follow the steps shown below:

### How to use the Property Mapping Feature

This advanced feature allows you to change the appearance of specific data in your repeater based on conditions set by the user. These conditions, defined in the data source, are mapped to the corresponding values or elements in the repeater, and the specified formatting is then applied.

![](https://support.optisigns.com/hc/article_attachments/42705284279187)

1. In Designer, double click on the Repeater that you'd like to change. (This will open the Repeater Editor.)
2. Select the element in the Repeater you want to edit, then click **Settings** at the top
3. Click **Advanced** **Options** in the Side Menu
4. Click **+ Property Mapping** (You'll press this for every new instance of mapping you'd like)
5. Clicking on the Property menu, select one of the options from the drop down shown above from the drop down menu or manually type in one of the available options listed below.
6. Clicking on the Value menu, selecting the correlating column name (This information is pulled from your DataSource).
7. Repeat this as many instances as you'd like for multiple elements within your Repeater.
8. Click **Update** to ensure this information is saved and applied to your Repeater.

#### Here are the listed property mapping options in the advanced settings:

|  |  |  |
| --- | --- | --- |
| Property | What it does | Value |
| Fill Color | Change the color of a selected shape or text in your Repeater | Accepts a valid **Hex** **color** **value** or **color** name (e.g., #CE657E or Red) |
| Font Size | Change the size of a text font and how it appears on screens | Accepts numerical value (e.g., 20) |
| Font Family | Change the font of a selected text, such as Arial, Times New Roman, or custom fonts. | Accepts a string values representing the font family. (e.g., Times New Roman) |
| Background Color | Change the background color of a selected shape or text in your Repeater. | Accepts a valid **Hex** **color** **value** or **color** name (e.g., #CE657E or Red) |
| Font Weight | Change the weight or thickness of the text font, making it appear lighter or bolder. | Accepts specific values: normal, bold, lighter, bolder, unset, or 100, 200, 300, 400, 500, 600, 700, 800, 900 |
| Underline | Specify whether you want the text underlined for emphasis. | Boolean value; accepts true/false or 0/1 |
| Linethrough | Specify whether you want a line striking through the text. | Boolean value; accepts true/false or 0/1 |
| Overline | Specify whether the text has an overline. | Boolean value; accepts true/false or 0/1 |
| Text Align | Change the horizontal alignment of the text. | Accepts specific values: left, center, right, justify, justify-left, justify-center, justify-right |
| Stroke Color | Change the stroke/outline color | Accepts a valid Hex color value or color name (e.g., #CE657E or Red) |
| Stroke Width | Specify the width of the stroke. which determines how thick or thin the outline is. | Accepts a number value. |
| Direction | Set the text direction: left-to-right or right-to-left | Accepts specific values: ltr or rtl |
| Visible | Determine whether the element is visible or not. | Boolean value; accepts true/false or 0/1 |
| Opacity | Change the transparency level of a selected shape, text, or photo in your Repeater | Accepts a numerical value from **0-1** (e.g., 0.2 is 20%) |

Here is an example of a sample DataSource set up with Fill Color, Background Color, Opacity, Font Weight, and Text Align:

![](https://support.optisigns.com/hc/article_attachments/30789450971539)

### How to Use Display Format Options

![](https://support.optisigns.com/hc/article_attachments/42702979620883)

If you'd like to change how the formatting of certain data from your DataSource looks on your repeater, you can do so with the Display Format option available in the Repeater Editor. This saves you time from editing your original DataSource, and will apply to the formatting to all the repeated elements in the Repeater.

**Follow the steps in the previous section regarding Property Mapping to access the Display Format options.**

|  |  |
| --- | --- |
| Display Format Option | What It Does |
| Text | This will show raw value without formatting. |
| Date Time | You can change the time zone, date format, and time format with available options. |
| Number | You can format numbers to display as percentages, decimals, currency, and more. |

## Push to Screens

Once your design is completed, it is ready to push to screen.

*(Here's **[a guide](https://support.optisigns.com/hc/en-us/articles/18988049363859)** if you need further assistance with this.)*

![](https://support.optisigns.com/hc/article_attachments/42702980943507)

Your screen will automatically update based on your connected data source.

You no longer need to manually update your data, which is time consuming and prone to errors.

## That's it! Now, you can set and forget it with OptiSync, an automated data mapping feature!
