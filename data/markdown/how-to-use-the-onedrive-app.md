# How to use the OneDrive App

Article URL: https://support.optisigns.com/hc/en-us/articles/360050665253-How-to-use-the-OneDrive-App
Article ID: 360050665253
Last Updated: 2026-01-29T15:45:29Z

With OptiSigns, you can quickly put images, videos from your Microsoft OneDrive on your Digital Signs screens  by using OneDrive App. The app will create a playlist for files in your OneDrive, any changes, updates, add, remove will automatically be synced. This allow you to quickly update, share contents within your team without needing to login to OptiSigns portal.

With the OptiSigns OneDrive app you can:

- Connect to OneDrive and choose a folders with images, videos
- Choose the timing, duration of your images/videos
- Choose transition effect between your files

## **Let's jump in and get started:**

First, you will need to have your screens set up and paired. For more information on how to do that, click [here](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv).

Then log on to our portal: <http://app.optisigns.com/>

Go to Files/Assets, Click on "App" and add the OneDrive app to your Account.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/26400546709779)

Click OneDrive app:

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/360076676833)

Sign in with Microsoft account.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/11413102757907)

Enter your Microsoft Credential and allow OptiSigns to access your OneDrive.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/360076676853)

Select the folder you want to use:

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/360076676873)

 Enter information for your OneDrive app

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/11413154341267)

- Name: Name of your OneDrive App, this is the name of the wall in your asset list. It will **not** be displayed on your screens.
- Folder: Your folder name from OneDrive.
- Transition Effect: Transition effect between your images, and videos in the folder.
- Transition Speed: How fast you want your transitions to animate.
- Duration for Image: How long each image should show on your screen, default is 10 seconds.
- Max Video Duration: Default is 0, which means the app will play each video till the end. You can set it to some other values to prevent too long videos. For example, if you set this value to 60 seconds. If a video is longer than 60s, it will get cut off at 60s to play next item. If a video is less than 60s, it will play the duration of the video.

**Advanced option:**

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/26400515453075)

- Force Sync Interval: By default, the system will force sync every 12 hours. The minimum is 1 hour.

Click Save.  
Depend on how many files you have in the folders, **it may take a moment** to sync to OptiSigns, as all the files will be synced, copied to our servers.

Files will be sorted and played by name. You can control the order of playback by changing the name of the files in your OneDrive.

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/360076676913)

### Switching Between Microsoft Accounts

If you create another OneDrive asset, you will notice you're automatically logged in to the same Microsoft account you signed into to create your first one. But what if you want to change Microsoft accounts?

Unfortunately, Microsoft authentication tokens are tied to the browser used, making this difficult.

However, there is a workaround. To do it, you'll need to switch browsers (i.e. if you added the first Microsoft account on Chrome, use Edge or Firefox), or create a new Chrome profile:

![](https://support.optisigns.com/hc/article_attachments/46697859996051)

Another option is to switch devices.

## **That's all! Congratulations!**

You have created your OneDrive app.  
You can change the wall at any time by clicking on it in the Files/Assets tab.

You can assign the newly created wall to your screen by going to Screens, clicking Edit screens, and assigning the wall to screens that you want.

You can put the created social walls in a Playlist, Schedule too.

**Notes:**

When files change, add, or remove from your OneDrive Folder, OptiSigns will automatically sync the changes. You can check when the last time changes were made and what the last file synced by opening the app modal again.

You can also force refresh, and sync by clicking the Refresh Data button.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/11413157953299)

**Release Notes & Limitations:**

- Only image and video files are supported. If there are other files in the folder, they will be ignored.
- Sub-folder is not supported, the app will not sync files in folders under the one you selected
- To ensure strong performance, limit file sizes to 100 MB or smaller.
- Max number of files supported in folder is 200. If you have big video files, it's better to upload directly to OptiSigns; and if you have more than 200 files, you can split them up in multiple OneDrive folders.
- Microsoft does not have published SLA for integration API, hence sometime it could take really long time before Microsoft send folder change notification. As a workaround, OptiSigns will check the OneDrive folder every 12h to ensure folders are synced up.
- You can only create 100 OneDrive app per 1 account, if you need more please contact [support@optisigns.com](mailto:support@optisigns.com) to discuss Enterprise Plan

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
