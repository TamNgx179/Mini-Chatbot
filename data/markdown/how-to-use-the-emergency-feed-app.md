# How to Use the Emergency Feed App

Article URL: https://support.optisigns.com/hc/en-us/articles/4409673381011-How-to-Use-the-Emergency-Feed-App
Article ID: 4409673381011
Last Updated: 2025-12-29T21:30:40Z

### In this article, we'll explain how to set up and use the Emergency Feed app for displaying emergency messages on your digital signs.

- [What You'll Need](#WhatYouNeed)
- [Creating an Emergency Feed App Asset](#Creating)
  - [Theme Settings](#ThemeSettings)
  - [Advanced](#Advanced)

Some Emergency Alert Systems or Emergency Mass Notification Systems push out RSS feeds.

Using OptiSigns Emergency Feed app, you can have OptiSigns listen to an RSS feed, filter for certain types of messages, and target locations, and if there's matching content, it will take over screens to display emergency messages.

When the emergency is over, the feed returns blank, or no more matching content. OptiSigns will return to playing signage content as usual.

![emergency feed example image](https://signagecloud-prd.s3.amazonaws.com/editor/5f1595d6020cce00136d5164/f37643a3bef24cb59f514684aa518c3d_5f1595d6020cce00136d5164.jpg)

---

## What You'll Need

- An [**OptiSigns-capable device**](https://support.optisigns.com/hc/en-us/articles/360021855653-What-hardware-and-devices-are-supported)
- An OptiSigns [**Pro Plus plan or higher**](https://www.optisigns.com/pricing)
- A screen, [**set up and paired**](https://support.optisigns.com/hc/en-us/articles/18823504383891-OptiSigns-Getting-Started-Guide)

---

## Creating an Emergency Feed App Asset

On the OptiSigns portal, go to **Assets → Add Asset → Apps**.

![open apps tab optisigns](https://support.optisigns.com/hc/article_attachments/47770620403731)

Select **Emergency Feed:**

![select emergency feed app](https://support.optisigns.com/hc/article_attachments/29815767093395)

You'll see the following screen:

![emergency feed app setup](https://support.optisigns.com/hc/article_attachments/47770635827731)

These are the options, and what they do. Any edits made to these options should be automatically reflected in the **Preview** pane on the right. The **Preview** can be displayed in either **Landscape** or **Portrait** format.

![emergency feed app base options](https://support.optisigns.com/hc/article_attachments/47770620405907)

- **Name**: Name of your assets. This is for organizational purposes and will not be displayed on your screens.
- **RSS URL:** The URL of the Emergency RSS feed you wish to display.
- **Target:** Select Screens or Tags, then choose the proper one.
- **Status:** Choose between Active and
- **Check RSS feed every (seconds):** Set the amount of time in seconds for the app to update the Emergency Feed.
- **Preview Window:** This shows how your Emergency Feed asset will look when pushed to a screen.
- **Orientation Options:** Change between Landscape and Portrait orientation for the Preview.

### Theme Settings

Click **Theme Settings** to expand the field and provide a slate of new options:

![emergency feed app theme settings](https://support.optisigns.com/hc/article_attachments/47770620407699)

- **Background Color:** Determines the background color. Can be chosen with Hex Code or via color picker:  
  ![color picker optisigns](https://support.optisigns.com/hc/article_attachments/47770620408211)
- **Text Color:** Determines the text color. Can be chosen with Hex Code or via color picker.
- **Background Image:** Lets you choose a Background image for your RSS feed. When **Custom** is selected, it will give you the opportunity to **Choose Photo:**

  ![background image option expanded](https://support.optisigns.com/hc/article_attachments/47770620411539)

  This photo must already exist as an asset within OptiSigns.
- **Font Size:** Choose between Default Font Size, or Custom. When Custom is selected, will provide a new option: **Custom Font Size**.  
  **![font size option expanded](https://support.optisigns.com/hc/article_attachments/47770635844371)**
  - **Custom Font Size:** Choose your font size.
- **Text Alignment/Position:** Choose the alignment and position of the RSS text.
- **Max Number of Rows:** Choose the maximum number of rows to dedicate to the Emergency Feed.

### Advanced

Click **Advanced** to expand the field and provide a slate of additional options:

![emergency feed app advanced options](https://support.optisigns.com/hc/article_attachments/47770635845523)

- **Duration (seconds):** How long to display each feed item before moving on to the next.
- **Title Tag:** Message title from the RSS XML feed. The default is <title> - you can change it if your feed is different
- **Description Tag**: Message content from the RSS XML feed. The default is <description> - you can change it if your feed is different
- **Location (Screen Tags):** Some RSS can pass locations tag (i.e. emergency in a certain location only). The default tag is <location> - you can change it if your feed is different
- **Filter content containing:** Filter content based on specific words in the title or description (i.e. "fire"). If any title or description contains the word "fire" (non-case insensitive), the app will trigger the screen takeover.
- **Exclude title containing:** this filter will only apply to the title. You can hide all the old feeds by filtering with specific words in the title. I.E: “All Clear”, so after the emergency is gone, all the feeds before this title will be hidden, then the screen will revert to the original content or just display the new content after that.

Click **Save**.

After Saving, the app will start listening to the RSS feed. If the conditions match based on your settings, they will take over the screens you targeted and display the emergency messages from the RSS feed.

### That's all!

If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
