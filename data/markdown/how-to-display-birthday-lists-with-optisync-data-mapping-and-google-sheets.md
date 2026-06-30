# How to Display Birthday Lists with OptiSync Data Mapping and Google Sheets

Article URL: https://support.optisigns.com/hc/en-us/articles/29979283289235-How-to-Display-Birthday-Lists-with-OptiSync-Data-Mapping-and-Google-Sheets
Article ID: 29979283289235
Last Updated: 2026-01-09T02:22:54Z

**With OptiSync, you can dynamically map data from various sources such as Google Sheets, Microsoft Excel, HR systems, and more to display employee birthday celebrations on your screens. This article explains how to connect your data source to the Designer app and automatically update birthday celebrants on your screens.**

To set up your birthday list with OptiSync, follow these steps:

1. [Setting up a Birthday List with OptiSync](#Setting)
   - [Option 1: Create a Repeater from Scratch](#Create)
   - [Option 2: Full Repeater Template](#Full)
   - [Option 3: Repeater Component](#Component)
2. [How to Auto-Update Values](#Auto)
3. [How to Handle Empty Data Values in a Repeater](#Empty)
4. [Set Up Auto Sorting in Your Sheet](#AutoSort)
5. [Push Designs to Screen](#Push)

|  |
| --- |
| Note: OptiSync, a dynamic data mapping feature, is exclusive to Pro Plus and above plans. |

---

## **Setting up a Birthday List with OptiSync**

For an in-depth instructional video on how to dynamically map a birthday list to your screens using OptiSigns, please watch the below guide:

1. Access your account by navigating to [OptiSigns](https://app.optisigns.com/) and log in
2. Proceed by adding your DataSource either through designer or your account settings under **DataSource**.
   - Learn how to add data sources [here](https://support.optisigns.com/hc/en-us/articles/29217646663187).
3. Click on 'Add DataSource' and select Google Sheets.

![](https://i.imgur.com/x3utMb2.png)

|  |
| --- |
| Note: While this functionality is **not exclusive** to Google Sheets, it will be the primary data source used for demonstration purposes in our examples. |

### Option 1: Create a Repeater from Scratch

If none of the Repeater designs resonate with the design you are trying to accomplish, you can create your own design within the repeater itself from scratch. Here's how:

1. Open the **Designer app**
2. Go to **DataSource** →
   Select your custom DataSource → Expand "**Row 1**".
3. **Drag** **and** **drop** the
   information you want displayed on the Repeater.
4. Double Click the Repeater to open the editor
5. Customize your Repeater's design.
6. Once the customization is complete press "**Update to Save**".

After creating it, feel free to add the repeater to any template design,  create your own design or upload one of your choosing.

### Option 2: Full Repeater Template

Once your data source is added, it's time to create your design using the Designer app. To quickly get started, you can utilize our prebuilt repeater templates.

1. 1. Open the Designer app from the Files/Assets page → Apps → Designer
   2. Go to **Repeaters** → Repeater Templates Section → Birthday
   3. Choose a template you'd like to use
   4. Click the **repeater** **item** *(i.e., the element with the names)*→ **Settings** → then "**Replace Data Source**".
   5. Click the "**Other Data Source**" arrow → choose your uploaded data source.
   6. Click **Continue**.
   7. Double-click the Repeater item to open it → open the **Data Source** on the left.
   8. Drag the employee name over the text box to populate it.

### Option 3: Repeater Component

Repeater components let you keep the repeater design you like while using a different template background. Choose any component template from our library or upload your own design, then add the repeater component on top. This lets you combine your preferred repeater with the template background you want.

Here's how to set up a repeater component:

1. Go to **Templates** → Select a **Template design** *(e.g., Birthday)*
2. Remove unwanted designs from template.
3. Go to **Repeaters** → Repeater Component Section → Birthday.
4. Click the **Repeater** once → select the "**Settings**" button → **Replace DataSource**.
5. Click the arrow off to the left side of "**Other DataSources**" → select **custom DataSource** → click **Continue**.
6. Double-click the **Repeater** to open it → **open the Data Source** on the left.
7. Drag your desired row *(i.e., **employee name**)* over the text box to populate it → Click **Update** to save.

---

## How to Auto-Update Values

To update the cell value mapped on the template, create another sheet for your employee birthday lists and use formulas to match today's date or the month, depending on your preference.

![](https://support.optisigns.com/hc/article_attachments/31245544060179)

|  |
| --- |
| Here is a sample [**link**](https://docs.google.com/spreadsheets/d/1A0apt1hrrz3XNujVj6gWjd0tDz_H2XUf4LFFx6Dqg6Q/edit?usp=sharing) to a Birthday list in Google Sheets. To use: Make a copy of it so that you can modify and adapt according to your specific requirements and preferences. |

Within the settings of your Google Sheet, please ensure Recalculation is on (e.g., On change and every hour/minute), otherwise the formula won't recalculate.

![chrome_vVrfIwHVno.png](https://support.optisigns.com/hc/article_attachments/30697329605779)

You can access this in your Google Sheet by selecting **File** > **Settings** > **Calculation.**

---

## How to Handle Empty Data Values in a Repeater

Let's say you're playing this design as a single asset or running it like a slideshow, but it is nobody's birthday. You can set how you would like your Repeater to handle empty data values.

1. In Designer, **select your Repeater** so it is highlighted.
2. Select **Settings** from the top bar.
3. In the far-right menu, use the drop-down menu for **Empty Data Handling** to select:
   - **Skip:** Skip it, or get rid of additional repeater items if there isn't enough data to reach the set "Total Items displayed per Page".
   - **Use Default Value:** Show default content, which is what your Repeater element looks like by itself.
   - **Use Blank:** The Repeater will show nothing.
4. Make sure to **save** your design.

![](https://support.optisigns.com/hc/article_attachments/43015697573523)

---

## Set Up Auto Sorting in Your Sheet

#### When handling large quantities of data in your spreadsheet, the ability to auto sort is incredibly useful and at times, essential. Instead of manually rearranging your data every time you add or update entries, the SORT function does it for you automatically.

|  |
| --- |
| **Note:** If you're using the example spreadsheet we provided above, there are specific instructions in that Google Sheet on how to set up auto-sorting for that data set-up. Please read the "**Tips**" section. If you're not using that spreadsheet, you can follow the example below to help you understand sorting. |

#### **Example: Auto-Sorting a Birthday List**

Imagine you have a list of employees and their birthdates. You want to keep this list sorted by the upcoming birthdays, and if two employees share the same birthdate, you want to sort their names alphabetically.

Let’s go over the **Step-by-Step Instructions:**

**Step 1**: Open Your Google Sheet. For simplicity, here’s how your data might look:

|  |  |
| --- | --- |
| **Celebrant Name** | **Birthdate** |
| Alice | 12/05/1990 |
| Bob | 12/15/2001 |
| Carol | 12/05/1990 |
| David | 12/01/1988 |

**Step 2:** Select an Empty Cell

Click on an empty cell where you want the sorted list to appear. For this example, we’ll use cell A1 in a new tab.

**Step 3**: Enter the SORT Formula

In the selected cell A1, enter the following formula and press Enter.

```auto
={"Celebrant Name", "Birthdate"; SORT(A2:B, B2:B, true, A2:A, true)}
```

The formula will immediately sort the data and display the results starting from Cell A1.

### How the Formula Works:

1. **={"Celebrant Name", "Birthdate";**
   - **Purpose**: This creates the headers for your sorted data.
   - **Explanation**: It sets up the column titles "**Celebrant Name**" and "**Birthdate**" at the top of the sorted list. The **semicolon** **;** tells Google Sheets to display the sorted data below these headers.
2. **SORT(A2:B, B2:B, true, A2:A, true)**
   - **A2:B**: This is the range of data you want to sort (including both columns: Celebrant Name and Birthdate).
   - **B2:B**: This specifies the first column to sort by, which is Birthdate.
     1. **true**: This indicates that the sorting should be in ***ascending*** order.
     2. **false**: This indicates that the sorting should be in ***descending*** order.
   - **A2:A**: This specifies the second column to sort by, which is Celebrant Name.
     1. **true**: This indicates that names should also be sorted in ***ascending*** order.
     2. **false**: This indicates that names should also be sorted in ***descending*** order.

### **Sorted Table:**

After applying the formula, your sorted list would look like this:

|  |  |
| --- | --- |
| **Celebrant Name** | **Birthdate** |
| David | 12/01/1988 |
| Alice | 12/05/1990 |
| Carol | 12/05/1990 |
| Bob | 12/15/2001 |

- David has the earliest birthday (12/01/1988) and appears first.
- Alice and Carol share the same birthdate (12/05/1990), so they are sorted alphabetically.
- Bob is listed last with the latest birthdate (12/15/2001).

Your list is now automatically sorted by birthdate and name.

Any updates or additions to the original data in your birthday columns will trigger the list in your new tab to auto-sort accordingly.

---

## Push Designs to Screen

To display your designs for your employees to see:

1. Add a **name** to your design.
2. Click the **Save** icon.
3. Then select "**Push to Screen**".

![](https://support.optisigns.com/hc/article_attachments/43015697575315)

You will now be brought to this page:

1. Select your screen.
2. **Push** to the screen.

![](https://support.optisigns.com/hc/article_attachments/43015684495891)

Here is what your design will look like when pushed to screens.

![](https://support.optisigns.com/hc/article_attachments/30118759886355)

## That's all!

Now you have a template that will show off any employee birthdays for your chosen month or day!
