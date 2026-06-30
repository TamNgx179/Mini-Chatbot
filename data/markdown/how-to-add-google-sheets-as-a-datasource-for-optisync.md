# How to add Google Sheets as a DataSource for OptiSync

Article URL: https://support.optisigns.com/hc/en-us/articles/29838866920211-How-to-add-Google-Sheets-as-a-DataSource-for-OptiSync
Article ID: 29838866920211
Last Updated: 2025-09-04T14:07:29Z

#### Using our new OptiSync feature in Designer, you can add your Google Sheets to your DataSources and apply to your designs or our prebuilt Repeater Templates or Components. For a breakdown on OptiSync, please visit our guide **[here](https://support.optisigns.com/hc/en-us/articles/29217646663187)**.

|  |
| --- |
| Note: OptiSync is only available on Pro Plus and above plans. |

## Adding Your Google Sheets as a DataSource

There are two different methods to adding Google Sheets to your DataSources:

#### **Method 1: Through Designer**

- On the Files/Assets page, select **Designer** from the Apps
- Select **DataSource** on the side menu, then **Add DataSource**
- Click **Google Sheets**
- Copy and Paste your Google Sheets URL into the provided text box, then **Import Data**
  - Note: You will be prompted to sign into your Google
- Once your Google Sheets is imported into a table in our portal, click **Save**
- **Name** your DataSource something easily recognizable
- Select your Synchronization and Update Interval
- Click **Done**

**Method 2: Through Account Settings**

- In our portal, select your account name, then **More**, then **DataSources**
- Select **Google Sheets**from the list of options
- Copy and Paste your Google Sheets URL into the provided text box, then **Import Data**
  - Note: You will be prompted to sign into your Google
- Once your Google Sheets is imported into a table in our portal, click **Update**
- **Name** your DataSource something easily recognizable
- Select your Synchronization and Update Interval
- Click **Done**
- Your **DataSource** will now be listed within your Advanced Account Settings

**Synchronization**

- **Only import once:** This option imports the data only once when you add the DataSource. After the initial import, the data will not be updated automatically.
- **Periodic direct access:** This option regularly fetches the latest data directly from the device through your gateway, providing "live access" to the data and ensuring you have the most up-to-date information available directly from the device.
  - *This is better for more consistent update intervals, but could cause performance issues.*
- **Periodic background sync:** This option periodically syncs data to your server in the background at regular intervals, reducing the need for direct queries to the device.

|  |
| --- |
| **IMPORTANT** |
| OptiSync does not support special characters (i.e. anything outside the scope of an English-language keyboard). This will cause the system data to read as blank, and it will not show. |

**Update Interval**

*The duration of time between updates if you chose "Periodic direct access" or "Periodic background sync"*

- None *(Your Datasource will import with the newest data available, but will not continuously update afterward. You will have to force refresh data for new updates.)*
- 30 minutes
- 1 hour
- 8 hours

|  |
| --- |
| If you'd like to learn more about OptiSync and how to use this DataSource for Data Mapping, please visit the following guide: |
| **[How to Set Up Dynamic Data Mapping with OptiSync](https://support.optisigns.com/hc/en-us/articles/29217646663187)** |

## That's it!

Now you've successfully added your Excel spreadsheet as a DataSource to be used for data mapping with OptiSync!
