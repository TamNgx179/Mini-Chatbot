# How to Use Google Slides with OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/360050642833-How-to-Use-Google-Slides-with-OptiSigns
Article ID: 360050642833
Last Updated: 2026-01-31T15:45:41Z

### In this article, we'll show how to use Google Slides with OptiSigns.

- [What You'll Need](#WhatYouNeed)
- [Creating a Google Slide Asset on OptiSigns](#CreatingAsset)
  - [Public Slides](#Public)
  - [Private Slides](#Private)
    - [Advanced Settings](#Advanced)
- [Assigning a Google Slide Asset to Your Screens](#AssigningtoScreen)
  - [Using a Google Slide Asset in a Playlist](#UsinginPlaylist)

[Google Slides](https://www.google.com/slides/about/) is a very popular way to create and share your presentations. These presentations can then be used on your Digital Signs for meetings, photo slideshows, and more!

There are two types of Google Slide: Public, and Private. Each has a different method of setup to display within OptiSigns. Private slideshows require a Google Authorization to access, and have different features. Here, we'll go over both.

---

## What You'll Need

- An [**OptiSigns-capable device**](https://support.optisigns.com/hc/en-us/articles/360021855653-What-hardware-and-devices-are-supported)
- An OptiSigns [**Standard plan or higher**](https://www.optisigns.com/pricing)
- A screen, [**set up and paired**](https://support.optisigns.com/hc/en-us/articles/18823504383891-OptiSigns-Getting-Started-Guide)

---

## Creating a Google Slide Asset on OptiSigns

On the OptiSigns portal, go to **Assets → Add Asset → Apps**.

![open apps tab optisigns](https://support.optisigns.com/hc/article_attachments/48704526157331)

Select **Google Slides**:

![](https://support.optisigns.com/hc/article_attachments/48704526159123)

You'll see the following screen:

![](https://support.optisigns.com/hc/article_attachments/48704528568851)

These are the options and what they do:

**Name -** The name of the Google Slides asset as it will appear in OptiSigns. This is only for OptiSigns and will not affect your slideshow or anything in the asset itself.

**URL -** The link of the Google Slides presentation you want to display.

Additional options will appear once your URL is placed in the field and hit **Next**.

### Public Slides

A Public slide is one that reads **Anyone with the link**.

![](https://support.optisigns.com/hc/article_attachments/48704526167443)

When a URL to a Public slide is placed in the **URL** field in the Google Slides app and you hit **Next**, additional options will appear:

![](https://support.optisigns.com/hc/article_attachments/48704526169875)

**Update Interval -** Choose how often OptiSigns will check your Google Sheet for updates. Measured in seconds. Default is 600 seconds (10 minutes). If 0 is input, it will only refresh each time it loads - useful for using this asset in a Playlist.

**Auto-advance slides -** Choose how quickly your slides will advance. Measured in seconds. If your Google Slide asset is the only asset assigned to your screen, once it reaches the end of the slideshow it will loop from the beginning.

Hit **Save.** Your slideshow will be Previewed on the left hand side, and you can make adjustments as necessary. When it is set up to your liking, hit **Close**.

Congratulations! You've created a Google Slides app.

### Private Slides

A Private slideshow is one that reads **Restricted.** This also applies to slides which groups or individuals also have access to - anything which is not "Anyone with the link" is considered a Private Google Slide.

![](https://support.optisigns.com/hc/article_attachments/48704526172563)

![](https://support.optisigns.com/hc/article_attachments/48704526174483)

|  |
| --- |
| **NOTE** |
| Displaying a Private slideshow in OptiSigns requires OptiSigns to repeatedly ping your Google account to check for updates on your Google Slides document. This means we cannot set a definite "time" measured in seconds where we can guarantee your slides will advance due to network variability. However, you can still set the speed - see below. |

Placing a Private Google Slides link in the **URL** section of the Google Slides app and hitting **Next** will prompt you to provide Google authorization.

![](https://support.optisigns.com/hc/article_attachments/48704526178195)

Hitting **Sign In with Google** will prompt you to choose the Google account associated with the URL. This account must have access to the slide in question.

![](https://support.optisigns.com/hc/article_attachments/48704528589331)

You'll have to grant OptiSigns certain permissions in order to display your Private Google Slideshow:

![](https://support.optisigns.com/hc/article_attachments/48704526181651)

If this is acceptable, hit **Continue**. Now you'll be back in OptiSigns, with additional options:

![](https://support.optisigns.com/hc/article_attachments/48704526183571)

**Aspect Ratio** - Lets you choose the Aspect Ratio in which to display your slides. It's stuck at Landscape, but you can set it to display at either 16:9 or 4:3.

![](https://support.optisigns.com/hc/article_attachments/48704528595219)

**Speed -** Choose the speed at which the slideshow advances. Choose from **Slow**, **Medium**, **Fast**, or **Custom**. When Custom is chosen, you can adjust it via the below slider:

![](https://support.optisigns.com/hc/article_attachments/48704528597267)

#### Advanced Settings

Click **Advanced** to expand the field and provide an additional option:

![](https://support.optisigns.com/hc/article_attachments/48704526192403)

**Force Sync Interval (hours) -** Choose the interval rate at which the Google Slide will force synchronize. By default, this is 12 hours.

|  |
| --- |
| **IMPORTANT** |
| The way our app works with Private slideshows is that it uses a webhook to automatically fetch new instances of it when updates are made. Depending on how many updates are made, it will be either near real-time or lag a couple hours.  Force Sync Interval is more of a fallback system. The absolute minimum we are able to Force Sync is **1 hour**. Only do this if you really, really need constantly updated data from your slideshow. Otherwise, the 12 hour default Force Sync Interval will work for most use cases. |

---

## Assigning a Google Slides Asset to Your Screens

To get your new Google Slide asset to a screen, go to the **Screens** tab, then click the screen you want to assign it to.

![](https://support.optisigns.com/hc/article_attachments/48704526193427)

This brings up the **Edit Screen** tab:

![](https://support.optisigns.com/hc/article_attachments/48704526197779)

Here, select **Asset** under Content type, then hit **Change** next to Selected Asset.

![](https://support.optisigns.com/hc/article_attachments/48704528605203)

Now hit **Save**. Your Google Slides asset will play on

### Using a Google Slides Asset in a Playlist

Getting a Google Slides asset to play well in a Playlist requires a little bit of extra configuration.

First, create a Playlist by going to **Playlists → Create Playlist.**

![](https://support.optisigns.com/hc/article_attachments/48704526202643)

Add your Google Slides asset to the Playlist by finding it on the right hand column:

![](https://support.optisigns.com/hc/article_attachments/48704526205075)

Here, you'll want to adjust the time it plays for:

![](https://support.optisigns.com/hc/article_attachments/48704528614291)

This time applies to the ***entire slideshow***, not just a single slide.

To better illustrate what we mean, let's say you have a slideshow consisting of 10 slides. You've configured the Asset to advance its slides every 5 seconds for a Public slideshow, or a Medium rate for a Private slideshow. This means you'll want to make sure the time given to this asset in your playlist is at least 50 seconds in order to display the entire slideshow.

Basically, it's number of slides (s) times the advance rate of the slideshow (a) equals the total time for it to display on the playlist (t).

- s\*a=t

Whew!

### That's all!

If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
