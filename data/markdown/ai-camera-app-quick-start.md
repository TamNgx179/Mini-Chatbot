# AI Camera App - Quick Start

Article URL: https://support.optisigns.com/hc/en-us/articles/27690296225555-AI-Camera-App-Quick-Start
Article ID: 27690296225555
Last Updated: 2026-06-29T19:26:02Z

OptiSigns AI Camera app that allows you to use any camera, plug into the device playing OptiSigns Digital Signage player to:

1. Detect and collect data about passing by foot traffic to analyze impressions and exposure of your Digital Sign.

2. Responsively display different content based on demographic of viewers standing in front of your screens.

This feature is supported on [Linux](https://support.optisigns.com/hc/en-us/articles/360034379573-Linux), [Windows](https://support.optisigns.com/hc/en-us/articles/360034379293-Windows), and [Android Device](https://support.optisigns.com/hc/en-us/articles/1500004585601-OptiSigns-Pre-Configured-Android-Device).

**Quick start guide to use OptiSigns AI Camera:**

In this guide, we will:

1. Set up the AI Camera to display suit sales when a male person is detected and yoga wear sales when a female person is detected.

[![](https://support.optisigns.com/hc/article_attachments/27855243843091)](https://support.optisigns.com/hc/article_attachments/27855243843091)

2. Review the data collected by the app on the portal's reporting page.

Ex:

![Screenshot 2024-03-22 141025.png](https://support.optisigns.com/hc/article_attachments/27696211826835)

From there, you can modify the set-up to fit your needs.

**1.) Preparation:**

If you haven't paired a device yet, follow this guide [for Windows](https://support.optisigns.com/hc/en-us/articles/360034379293-Windows), or this guide [for Linux](https://support.optisigns.com/hc/en-us/articles/360034379573) or [Raspberry Pi](https://support.optisigns.com/hc/en-us/articles/360034379693) to install and run OptiSigns Digital Signage Player first.

**You must have the OptiSigns' Engage Subscription or Trial to access the AI Camera feature.**

Each account is entitled to use the AI Camera feature on **ONE FREE** screen. If you would like to add the AI Camera feature to more than 1 screen, you will need to purchase the Engage subscription.

This screen is the only one that will ever have Engage enabled, and it is a one-time assignment. If you remove the Engage feature from that screen, you will not be able to add it to another.

Here is a link to the [subscription page](https://www.optisigns.com/pricing?utm_source=google&utm_medium=cpc&utm_campaign=**LP%20-%20TM%20-%20General&gad_source=1&tm=tt&gclid=CjwKCAjw17qvBhBrEiwA1rU9wzdWIAakpk0mIXEg3OpcP4QnrL-GRU2ZyQ5wF16D9CNUBDIXeQfZJxoCfXkQAvD_BwE&aaid=adaoPCrtgEgFw).

Get a USB Camera and plug into your device:

We recommend the Logitech Webcams like the [C270](https://www.amazon.com/Logitech-Desktop-Widescreen-Calling-Recording/dp/B004FHO5Y6/ref=sr_1_2?dib=eyJ2IjoiMSJ9.xTkSg8MY4kb9MLTupXquWb1yd2NRogWqCSAv6prNcI09Cg4SXj4qfME1YR36PDpBODSThuLo3EPLSG2yFWB3XffZZAefDL1sF5SHE2hY8oVDBSRNaM-sD9zqv9mMWAHCyTa7yVAFVfZvgmQ06ucgCGUFPAEBnYIKWiSAtQKJDbnOYpCm58MiC9xf8Sw311vn8Ns-9hGhLuZbLzO8yevcrXLnTT91vEDnl9iUrtalnys.28BMi6sOrg5Zhk6RL9Gc29RtyarJ66gj09SE4fi13eQ&dib_tag=se&keywords=Logitech+Webcams+like+the+C270.%5C&qid=1711118707&sr=8-2).

If you are running on your Windows Laptop, you can use the built-in camera; no additional camera is needed.

**2.) Review & configure AI Camera:**

Go to the **Engage** Tab at the top of the screen.

**![annotely_image (19).jpeg](https://support.optisigns.com/hc/article_attachments/27690296203923)**

Click New App on the top right corner:

**![annotely_image (20).jpeg](https://support.optisigns.com/hc/article_attachments/27690263765011)**

First, click the "**AI Camera**" tab on the left side. Then, click the "**Build**" button in the bottom right corner.

**![annotely_image (21).jpeg](https://support.optisigns.com/hc/article_attachments/27690263766035)**

You will then be directed to the AI Camera Build page.

![Screenshot 2024-03-22 101159.png](https://support.optisigns.com/hc/article_attachments/27690263767315)

![Screenshot 2024-03-22 101449.png](https://support.optisigns.com/hc/article_attachments/27690296216979)

You can view how the asset is configured

**Play Settings:**

- Play for at least: when detected, the app will play the content corresponding to detection rule for at least X seconds. (Default is 3s)
- Rest for: the device will wait for at least X seconds (Default: 3s) before triggering additional content if multiple rules are detected.

We recommend to keep Play for at least and Rest for at 3s, to give smooth feeling experience when in crowded place like mall, or an airport with many people walking by very quickly.

**Play Rules:**

- Effective Time: This refers to the time frame during which the feature is active and the specific days it applies to.
- If Detected: This describes how the AI camera determines when to trigger a change.
- Play Content: This pertains to the asset assigned to play when a specific gender is detected.

After completing the previous steps, you will be directed to the "Assign to Screen" page. Here, you will assign the AI camera to the specific screen on which you want the camera to trigger.

![Screenshot 2024-03-28 112724.png](https://support.optisigns.com/hc/article_attachments/27882861309971)

**3.) Assign the AI Camera app to your Screen:**

1. Go to the **Screen** tab and click **Edit**.

2. Click **Advanced**.

![annotely_image (22).jpeg](https://support.optisigns.com/hc/article_attachments/27696211732627)

3. Click **More**.

![](https://support.optisigns.com/hc/article_attachments/27974903303571)

4.  **Activate** the AI Add-on.

![](https://support.optisigns.com/hc/article_attachments/27974903309715)

If you want the device to send data for Analytics purposes, please leave the Send AI Data box checked as well. You can learn more about what data we collect [here](https://support.optisigns.com/hc/en-us/articles/360058259834-OptiSigns-AI-Camera-FAQs).

![](https://support.optisigns.com/hc/article_attachments/27974888673171)

5. Change the **AI Add-on** and it will bring you to the select Asset Page.

6. Click **Engage**

![annotely_image (25).jpeg](https://support.optisigns.com/hc/article_attachments/27696232098195)

7. Choose your **AI App** and then save.

![annotely_image (26).jpeg](https://support.optisigns.com/hc/article_attachments/27696211793555)

**4**.) **Set up camera & app on your device**

If you are using Linux or Raspberry Pi, the AI Camera will be automatically install when you click AI Camera Activate in the step above. You may need to restart your device. If you need instruction on how to manually activate, run AI Camera for Linux, you can follow [this guide](https://support.optisigns.com/hc/en-us/articles/360060676993-How-to-manually-install-activate-OptiSigns-AI-Add-on-on-Linux-or-Raspberry-Pi).

For Android, you'll need to go to the app permission settings and grant camera access.

If you are using Windows just download & run [optisigns-ai-detection.exe.](https://links.optisigns.com/ai-add-on-win) If you want OptiSigns AI Detection to run on system start up just follow these [steps here](https://support.optisigns.com/hc/en-us/articles/360058345334-How-to-run-OptiSigns-AI-Add-on-on-start-up-in-Windows).

The app will log events it detected like below.

[![](https://support.optisigns.com/hc/article_attachments/27805047501843)](https://support.optisigns.com/hc/article_attachments/27805047501843)

**That's all!**

Once OptiSigns AI detection is running, you'll notice it's using the camera to detect and send events to the OptiSigns Player to change content as appropriate. In this case, if a male person is in front of the camera, the Suit Sales ad will be displayed. If a female person is in front of the camera, the Yoga ad will be displayed.

If you leave "Send AI data" on, you can view the analytics report here:

![Screenshot 2024-03-22 141025.png](https://support.optisigns.com/hc/article_attachments/27696211826835)

Please let us know if you have any questions or feedback.
