# How to Use the Local Folder App in OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/1500001985341-How-to-Use-the-Local-Folder-App-in-OptiSigns
Article ID: 1500001985341
Last Updated: 2025-09-04T19:36:02Z

### In this article, we'll explain how to use the Local Folder app in OptiSigns to let you access locally stored files on your device to display.

- [How to Set Up the Local Folder App](#Setup)
  - [For Windows](#Windows)
  - [For Mac/Linux/Ubuntu/Raspberry Pi](#Mac)
  - [For the OptiSigns Android Stick](#Stick)
  - [For the OptiSigns Pro Player](#ProPlayer)

Sometimes, due to network limitations or security reasons, you'll have content you'd rather keep locally at your device. The Local Folder app allows you to access content stored locally.

Major use cases for this app include:

- Sensitive information that should not be transferred via Internet
- Limited network availability locations
- You want to use or mix in contents from USB thumb drives

OptiSigns player is smart enough to scan for changes in these folders. When files are added or removed, it's handled automatically.

You can also use USB thumb drives. OptiSigns detects drives plugged in and scan the folder to play again as long as it's given the correct path.

|  |
| --- |
| **Note:**The Local folder application only currently supports video and image files. |

---

## **How to Set Up the Local Folder App**

First, you will need to have your screens set up and paired. For more information on how to do that, click [here](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv).

Then log on to our portal: <http://app.optisigns.com/>

Go to **Files/Assets** and click on **"Apps"**:

![optisigns portal with arrows pointing to Files/Assets tab and Apps button](https://support.optisigns.com/hc/article_attachments/21882432568595)

Find the **Local Folder** app:

![apps screen in optisigns portal with arrow pointing at local folder app](https://support.optisigns.com/hc/article_attachments/360102953613)

Enter the path to your local folder (explained in more detail below) and other settings:

![local folder app menu](https://support.optisigns.com/hc/article_attachments/360100790274)

- **Name** - Name of your Local Folder app. This will be displayed on your asset list, and will **not** be displayed on your screens.
- **Local Folder** - Path to the folder on your device. We will provide detailed instructions per platform later in this article.
- **Transition Effect** - Transition effect between your images and videos in the folder.
- **Transition Speed** - How fast you want your transitions to animate.
- **Duration for Image** - How long each images should show on your screen, default is 10 seconds.
- **Max Video Duration** - Default is 0, which means the app will play each video till the end. You can set it to some other values to prevent too long videos. For example if you set this value to 60 seconds. If a video is longer than 60s, it will get cut off at 60s to play next item. If a video is less than 60s, it will play the duration of the video.
- **Scale Image** - select how the player should handle if image's resolution is less than your screen's resolution
- **Scale Video** - select how the player should handle if the video's resolution is less than your screen's resolution
- **Shuffle** - select if you want to shuffle play the content in the folder (Default order is by filename alphabetically)

Click **Save**.

You now can assign the Local Folder app to your device. It can also be placed in a Playlist or Schedule.

### For Windows:

If using a Windows device to display your content, the path to your Local Folder will be similar to C:\ D:\Media Folder etc. Find the path by looking at the folder's Properties, like so:

![windows folder highlighting folder path](https://support.optisigns.com/hc/article_attachments/33807447378707)

You'll then use this path to fill in the Local Folder value within the Local Folder App:

![local folder app in optisigns with windows value](https://support.optisigns.com/hc/article_attachments/33807447390355)

This will vary depending on the location of the folder on your drive.

### For Mac/Linux/Ubuntu/Raspberry Pi:

If using a Mac, Linux, or Ubuntu device, the path to your folder will be similar to /media/path/folder.

For Mac users, find this using **Get Info**. It will look similar to this:

![mac folder highlighting folder path](https://support.optisigns.com/hc/article_attachments/33807447394067)

This comes out to /Users/{username}/Desktop as a path filename.

In Linux/Ubuntu, you can find this information in **Properties.**

![ubuntu folder highlighting folder path](https://support.optisigns.com/hc/article_attachments/33807672236819)

The path in this example would be /home/optisigns .

For Raspberry Pi, the path can also be found in **Properties**.

![raspberry pi folder highlighting folder path](https://support.optisigns.com/hc/article_attachments/33807431768339)

In this example, that's /home/pi.

You'll then use this path to fill in the Local Folder value within the Local Folder App:

![local folder app with mac/linux/ubuntu/pi value](https://support.optisigns.com/hc/article_attachments/33807431781907)

This will vary depending on the location of the folder on your drive. However, it's important to note that Mac, Linux, Ubuntu, and Raspberry Pi paths all have the same format.

### For OptiSigns Android Stick Digital Signage Player

|  |
| --- |
| **IMPORTANT:** To use the Local Folder App on your Android Stick player, make sure its firmware version is 5.17.23 or later. |

To use the Local Folder app on an [OptiSigns Android stick](https://shop.optisigns.com/products/optisigns-android-stick-player-2), first install whatever you'd like to display on a USB drive or MicroSD. Attach the device to your Android stick, then navigate using a [Remote Control](https://support.optisigns.com/hc/en-us/articles/30304278652563-How-to-Use-the-Mobile-App-for-Remote-Control) to **Device Storage** on the side menu:

![optisigns android stick player menu with arrow pointing toward device storage option](https://support.optisigns.com/hc/article_attachments/33807431790995)

Once there, you should be able to see your External storage device listed:

![device storage menu optisigns stick arrow pointing toward external storage path](https://support.optisigns.com/hc/article_attachments/33807431795347)

Simply copy this and place this in your Local Folder value within the Local Folder App:

![local folder app optisigns with android stick value](https://support.optisigns.com/hc/article_attachments/33807447423763)

This path will vary depending on the type of external storage device, and will always be different.

### For OptiSigns Pro Digital Signage Player

The OptiSigns Pro Player is an Ubuntu enabled device, so it runs the same way. You'll have a slightly different path depending on whether you're using a USB device or MicroSD card as your external storage, or if you have multiple USB drives plugged into the player.

The path for a single USB device when plugged into the OptiSigns Pro Player will be:

```
/home/optisigns/external/sdb1
```

If your device has a label, it will be:

```
/home/optisigns/external/{label}-sdb1
```

Where {label} is the name/label of the USB drive.

Should you plug in a second USB drive, the path will be:

```
/home/optisigns/external/sdc1
```

Similarly, a third USB drive will have a path of:

```
/home/optisigns/external/sdd1
```

Again, remember to add the label to the path if your drive has one.

Lastly, if you're using a MicroSD card, your path will be:

```
 /home/optisigns/external/{label}-mmcblk0p1
```

Where {label} is the name/label of the MicroSD card.

Then, use this path to fill in the Local Folder value within the Local Folder App:

![local folder app optisigns with pro player value](https://support.optisigns.com/hc/article_attachments/33807447426963)

### **That's all!**

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
