# How to Create and Use the Split Screen App

Article URL: https://support.optisigns.com/hc/en-us/articles/360026559573-How-to-Create-and-Use-the-Split-Screen-App
Article ID: 360026559573
Last Updated: 2026-02-04T16:37:07Z

The Split Screen feature in OptiSigns allows you to divide your screen into different zones or regions, enabling a more dynamic display of content. This feature is supported on all platforms except Roku and Apple TV. Commonly referred to as Split Screens, Screen Zones, or Screen Layouts, this guide will walk you through the steps to create and use the split screen app.

![](https://support.optisigns.com/hc/article_attachments/360041995893)

## Steps to Create & Use the Split Screen App

### 1. Creating a Split Screen App

![](https://support.optisigns.com/hc/article_attachments/30984907809555)

1. **Navigate to Assets/Files**: Click on the `Files/Assets` tab in the OptiSigns portal.
2. **Select the App**: Click on the `App` option.
3. **Choose Split Screen**: Select `Split Screen` from the available options.

### 2. Selecting a Template

![chrome_fXoMvJjziP.png](https://support.optisigns.com/hc/article_attachments/30984941338003)

1. **Choose a Template**: Templates provide a starting point. You can modify the zone dimensions later or create your own Custom layout.
   - For this article, we will use `2 Mains + 1 Ticker` in examples.

### 3. Configuring Zones

![](https://support.optisigns.com/hc/article_attachments/30984941345555)

1. **Name Your Split Screen**: Enter a name for your Split Screen. This name will appear in the Asset list.
2. **Adjust Orientation:** Change the split screen to landscape or portrait orientation.
3. **Name the Zone:** Not required to change, but you can give each zone a name.
4. **Adjust Zone Dimensions**: Modify the position and dimensions of the zones if needed.
   1. The numbers are in percentages to ensure the layout scales appropriately regardless of screen resolution.
   2. Or, you can click on a zone, and drag and drop the edges to change the zone's size.
5. **Assign Content to Zones**: For each zone, select the type of content you want it to play (asset, playlist, or schedule).
6. **Add or Adjust the Zones:** Use the options on this bar to change the colored zones.
   - **Plus Icon:** Will add another zone.
   - **Undo and Redo:** Either reverse an action or reapply an action you undid.
   - **Adjust Layering of Zones:** Send zones backward, to the back, forward, or to the front. These are useful if your zones overlap each other.
   - **Delete:** Select a zone and delete it from the customization board.

|  |
| --- |
| Note: You cannot place a Split Screen within a Split Screen |

### 4. Adding a Scrolling Strip

![chrome_IrQqLbhNk0.gif](https://support.optisigns.com/hc/article_attachments/30984907828115)

- **Scrolling Strip Integration**: Split Screen can be accompanied by a Scrolling Strip. Apps like Weather, News, Social Media walls, and Stock automatically switch to a scrolling strip format when placed in a scrolling strip-like zone. Learn more about creating a Scrolling Strip [**here.**](https://support.optisigns.com/hc/en-us/articles/360026559613)

### 5. Making Adjustments (Optional)

After integrating your content, you can make adjustments by hitting the **Settings** wheel:

![](https://support.optisigns.com/hc/article_attachments/48817391393683)

This will open the **Split Screen Configs** menu:

![](https://support.optisigns.com/hc/article_attachments/48817391398163)

- **Unit Type** - Change between percentage (%) and pixels on the Zone configuration.
- **Resolution** - Choose the final display resolution. This should match the total resolution of the screen you plan to display the split screen on.
- **Background Music -** Lets you choose the Zone Playlist background music will be played.
- **Audio Zone** - Lets you select which zone audio will be played in. Zones not selected will be muted.
- **Primary Zone** - This settings lets you sync timing of all secondary zones to the zone selected. With None selected, all content will play at their own pace.

### 6. Preview and Save

![](https://support.optisigns.com/hc/article_attachments/30984907837459)

1. **Preview**: Click `Preview` to see how the Split Screen looks.
2. **Save**: Once satisfied with the layout, click `Save`. Your Split Screen will be added to your Asset list.

### 7. Assigning Split Screen to Your Screens

1. **Navigate to Screens Tab**: Go to the `Screens` tab.
2. **Edit Screen**: Click `Edit` on the screen you want to assign the Split Screen to.
3. **Assign Split Screen**: Set `Type` to `Asset` and select the newly created Split Screen asset.

|  |
| --- |
| Note |
| You can assign a Split Screen directly to a playlist, but it can create a loop (a Split Screen containing a playlist that contains a Split Screen). Instead, we recommend assigning a playlist to the zones within the Split Screen. |

## Frequently Asked Questions

#### **I can't get some of my split screens to display as full screen. What can I do?**

This issue occurs because the **Main Zone** in the Split Screen app does not have a 16:9 ratio. Here are a few ways to resolve this and ensure the content fits your Main Zone:

1. **Resize the Designer Asset:**

   - Ensure your asset size matches that of the **Main Zone,**
   - For example: in the below screenshot, the Main Zone is 1920x970. So you'll want to resize your Designer asset to match that number.

   ![](https://support.optisigns.com/hc/article_attachments/37700048880275)
2. **Adjust the Main Zone Ratio:**

   - Change the Main Zone size to **1920x1080**, and use other zones as an overlay.
   - This works best with scrolling strips

   ![](https://support.optisigns.com/hc/article_attachments/37700029022099)
3. **Use the Stretch Option:**

   - In the playlist settings, set the **Scale Image** option to **Stretch**.
   - This will stretch the content to fill the Main Zone.

   ![](https://support.optisigns.com/hc/article_attachments/37700048887059)

You can get an idea of what these settings will look like with this image:

![](https://support.optisigns.com/hc/article_attachments/37700048889875)

For more information on image ratios, see our article on [**Stretch, Zoom, and Fit**](https://support.optisigns.com/hc/en-us/articles/360026610194-Stretch-your-images-document-Stretch-vs-Fit-vs-Zoom-your-content).

Please note that these ratios apply to any app, not just images and videos.

#### **My documents (PowerPoint, PDFs) go through pages too fast! How can I fix this?**

When selecting a document, there is an additional setting, called **Duration**:

![](https://support.optisigns.com/hc/article_attachments/45708705963667)

This shows how long on your split screen your document will display. However, please note that this duration applies to ***the entire document**.*Meaning, if you have a slideshow with 10 slides, and set this duration for 10 seconds, each slide will only display for 1 second.

If you want to display each slide for 10 seconds, you will need to set your duration to 100 seconds: 10 slides divided by 10 seconds per slide.

## Additional Information

For any additional questions, concerns, or feedback about OptiSigns, feel free to reach out to our support team at support@optisigns.com.
