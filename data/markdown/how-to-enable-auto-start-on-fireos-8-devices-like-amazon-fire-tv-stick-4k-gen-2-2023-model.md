# How to enable auto-start on FireOS 8 devices like Amazon Fire TV Stick 4K Gen 2 (2023 model)

Article URL: https://support.optisigns.com/hc/en-us/articles/23274673797139-How-to-enable-auto-start-on-FireOS-8-devices-like-Amazon-Fire-TV-Stick-4K-Gen-2-2023-model
Article ID: 23274673797139
Last Updated: 2025-09-04T16:18:04Z

Amazon recently released their new Gen 2 Fire Sticks that come with many changes including to its hardware and OS. While OptiSigns will run great on these new devices, there is an issue where the auto-start feature will not function properly, likely due to the updated version of Fire OS.

In this guide, we will show you how you can properly enable OptiSigns to auto-start on these new Gen 2 Fire Sticks.

Before we begin, please be sure you have the following ready:

- A computer.
- Stable internet connection.
- Ensure that both your computer and your Fire Stick are on the same network.
- Android SDK Platform Tools installed on your computer.  
  <https://developer.android.com/tools/releases/platform-tools>

#### **Step 1:**

On your Fire Stick, navigate to the settings then select “My Fire TV” then click on “Developer Options” and ensure that ABD Debugging is enabled.

**Note, in order to enable the developer options, follow these steps:**

1. Go to “Settings” from the home screen of your Fire Stick.
2. Select the “My Fire TV” or “Device” option.
3. Click on “About”.
4. Click on the first option where it labels the model of your Fire TV stick, quickly 7 times. You will see a notification at the bottom saying, "No need, you are already a developer" when this is complete.
5. Press the back button once or go back to “Settings” > “My Fire TV” and you will now see "Developer Options".

![](https://support.optisigns.com/hc/article_attachments/23274690253587)

#### **Step 2:**

Exit out of developer options then select “About” then “Network”. You will see the Fire Stick’s network information. In this case, we will want to write down the IP address:

![](https://support.optisigns.com/hc/article_attachments/23274680489747)

#### **Step 3:**

On your computer, you will need to have the Android SDK Platform Tools installed. You can install this by clicking on the link earlier in this guide. Make sure to create a folder somewhere on your computer such as your desktop then extract the contents on the Android SDK Platform Tools into that folder:

![](https://support.optisigns.com/hc/article_attachments/23274673766803)

#### **Step 4:**

On your desktop, open the command prompt. On Windows you can do this by typing “cmd” in the search bar on your taskbar. On Mac, it will be called the Terminal.  
  
Once you have this opened, type “cd \”

![](https://support.optisigns.com/hc/article_attachments/23274665378451)

Then type “cd android”

![](https://support.optisigns.com/hc/article_attachments/23274680497299)

Then type “dir”:

![](https://support.optisigns.com/hc/article_attachments/23274643497875)

Type “adb connect <The Firestick IP Address from step 2>”

**NOTE: If you receive a message where it mentions “failed to authenticate to <ip address>” you will need to allow access from your Firestick. Check “always allow from this computer” and press “OK”. Then back on the command prompt, type “adb disconnect” and hit enter.**

**![](https://support.optisigns.com/hc/article_attachments/23274690270739)**

Type adb connect <Firestick’s IP address> once more. Once connected, it should look like this:

![](https://support.optisigns.com/hc/article_attachments/23274660262547)

After you’ve successfully connected, enter this command then hit enter:

```
adb shell pm grant com.optisigns.player android.permission.SYSTEM_ALERT_WINDOW
```

This command will now be sent to your Firestick in order to allow OptiSigns to have its auto-start function enabled.

And that’s it! You’re all set!

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
