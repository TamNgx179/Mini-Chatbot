# How to add a Microsoft 365 Excel Spreadsheet as a DataSource for OptiSync

Article URL: https://support.optisigns.com/hc/en-us/articles/29863080711059-How-to-add-a-Microsoft-365-Excel-Spreadsheet-as-a-DataSource-for-OptiSync
Article ID: 29863080711059
Last Updated: 2026-01-29T16:01:49Z

#### Using our new OptiSync feature in Designer, you can add your Google Sheets to your DataSources and apply to your designs or our prebuilt Repeater Templates or Components. To learn more about OptiSync, please visit our guide [**here**](https://support.optisigns.com/hc/en-us/articles/29217646663187).

|  |
| --- |
| Note: OptiSync is only available on **Pro Plus and above** plans. |

## Adding Your Excel Spreadsheet as a DataSource

There are two different methods to adding Excel Spreadsheet to your DataSources:

|  |
| --- |
| **IMPORTANT NOTE** |
| OptiSync does not currently (as of 1/15/2025) support Excel's date formatting. In order for dates to properly display, they will need to be redone in TEXT format, or use a formula (like =TEXT(A1, "mm/dd/yy")) to convert them. |

#### **Method 1: Through Designer**

- On the Files/Assets page, select **Designer** from the Apps
- Select **DataSource** on the side menu, then **Add DataSource**
- Click **Microsoft 365 Excel**
- Grant access to your Microsoft 365 Excel by **signing in** when prompted
- Find and select your Excel spreadsheet from the Microsoft pop-up window
  - If your spreadsheet has multiple sheets, select the one you want to import from the drop-down menu
- Click **Import Data**
- Double check your table, select **Update**
- **Name** your DataSource something easily recognizable
- Select your Synchronization and Update Interval
- Click **Done**

**Method 2: Through Account Settings**

- In our portal, select your account name, then **More**, then **DataSources**
- Click **Microsoft 365 Excel**
- Grant access to your Microsoft 365 Excel by **signing in** when prompted
- Find and select your Excel spreadsheet from the Microsoft pop-up window
  - If your spreadsheet has multiple sheets, select the one you want to import from the drop-down menu
- Click **Import Data**
- Double check your table, select **Update**
- **Name** your DataSource something easily recognizable
- Select your Synchronization and Update Interval
- Click **Done**

**Synchronization**

- **Only once import:** This option imports the data only once when you add the DataSource. After the initial import, the data will not be updated automatically.
- **Periodic direct access:** This option regularly fetches the latest data directly from the device through your gateway, providing "live access" to the data and ensuring you have the most up-to-date information available directly from the device.
  - *This is better for more consistent update intervals, but could cause performance issues.*
- **Periodic background sync:** This option periodically syncs data to your server in the background at regular intervals, reducing the need for direct queries to the device.

**Update Interval**

The duration of time between updates if you chose "Periodic direct access" or "Periodic background sync"

- None *(Your Datasource will import with the newest data available, but will not continuously update afterward. You will have to force refresh data for new updates.)*
- 30 minutes
- 1 hour
- 8 hours

### Limitations

- OptiSync does not support special characters (i.e. anything outside the scope of an English-language keyboard). This will cause the system data to read as blank, and it will not show.
- Row 1 of your Spreadsheet will register as a Header, and must be regular text to support features like Excel Function outputs. A function cannot exist in Row 1 of a spreadsheet.

|  |
| --- |
| If you'd like to learn more about OptiSync and how to use this DataSource for Data Mapping, please visit the following guide: |
| [**How to Set Up Dynamic Data Mapping with OptiSync**](https://support.optisigns.com/hc/en-us/articles/29217646663187) |

## That's it!

Now you've successfully added your Excel spreadsheet as a DataSource to be used for data mapping with OptiSync!
