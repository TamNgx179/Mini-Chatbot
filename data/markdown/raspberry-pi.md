# Raspberry Pi

Article URL: https://support.optisigns.com/hc/en-us/articles/360034379693-Raspberry-Pi
Article ID: 360034379693
Last Updated: 2025-10-07T15:03:02Z

### In this article, we'll break down how to get OptiSigns running on a Rapsberry Pi device.

- [Two Methods to Get OptiSigns Running on a Raspberry Pi](#Methods)
- [Method 1: Download & Use Prebuilt SD Card Image](#Method1)
- [Method 2: Install OptiSigns on Existing Raspberry Pi OS by Downloading and Running an AppImage File](#Method2)
- [Summary](#Summary)
- [Limitations of OptiSigns on Raspberry Pi](#Limitations)

OptiSigns is compatible with and works well on Raspberry Pi. We recommend Raspberry Pi 3B+ and above. Which type of Raspberry Pi you have will determine what type of software you'll want to download.

|  |
| --- |
| **Download** |
| Download our prebuilt SD Card image for [Raspberry Pi 4 or older](https://links.optisigns.com/rpi-image) or [Raspberry Pi 5.](https://links.optisigns.com/rpi5-image) |

## **Two Methods to Get OptiSigns Running on a Raspberry Pi**

1) Download our prebuilt SD Card image for [Raspberry Pi 4](https://links.optisigns.com/rpi-image) or [Raspberry Pi 5](https://links.optisigns.com/rpi5-image) and flash to your SD Card.

2) Install OptiSigns on your existing Raspberry Pi OS by downloading and running [AppImage file](https://links.optisigns.com/rpi)

Here's a step-by-step guide for each method.

---

## **Method 1: Download & Use Prebuilt SD Card Image**

Download the latest SD Card image for [Raspberry Pi 4](https://links.optisigns.com/rpi-image) ([MD5](https://download.optisignsapp.com/RPi/player-2435240-rpi4.zip.md5)) or [Raspberry Pi 5](https://links.optisigns.com/rpi5-image) ([MD5](https://download.optisignsapp.com/RPi/player-2435240-rpi5.zip.md5)) here.

Unzip and Flash the SD Card image to your SD Card (minimum 16GB card is required).

Note: If using [Raspberry Pi Imager](https://www.raspberrypi.com/software/)  instead of Etcher below, WIFI settings can be configured.

**Download and Install Etcher.**

Please click [**here to download Etcher**](https://www.balena.io/etcher/)**.**

![](https://support.optisigns.com/hc/article_attachments/34728529852307)

Open **Etcher software** and select the **OptiSigns .img file** that you just unzipped.

![](https://support.optisigns.com/hc/article_attachments/34728545802259)

Select the **SD card drive.**

**![](https://support.optisigns.com/hc/article_attachments/34728529863699)**

Click **"Flash".**

**![](https://support.optisigns.com/hc/article_attachments/34728545814547)**

After flashing the SD card and booting up, **connect to your network.**

OptiSigns is preinstalled and will auto-start on start-up.

Next you can skip to **step 2) iv)** to pair the screens and start assigning content.

![optisigns app with arrow pointing to hamburger menu](https://support.optisigns.com/hc/article_attachments/360087500074)

---

## **Method 2: Install OptiSigns on Your Existing Raspberry Pi OS by Downloading and Running** [**AppImage file**](https://links.optisigns.com/rpi)

**Here are the high-level steps:**

i) Get a fresh image of [Raspberry Pi OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/) boot it up and configure your network*. If you already have Raspberry Pi OS running, you can skip this.*

ii) Download FUSE using your Raspberry Pi's Terminal.

iii) [Download OptiSigns](https://links.optisigns.com/rpi) to your Raspberry Pi OS, and run it.

iv) Pair your screen with [OptiSign portal.](https://app.optisigns.com/)

v) Using OptiSigns's web portal to assign content and manage your screens.

### **Step 1: Get a fresh image of Raspberry Pi OS and configure the network**

If you already have Raspberry Pi OS running, skip this step.  
Download a fresh image of Raspberry Pi OS. We recommend:

- [Raspberry Pi 64-bit for Raspberry Pi 5 with desktop and recommended software](https://downloads.raspberrypi.com/raspios_full_arm64/images/raspios_full_arm64-2024-07-04/2024-07-04-raspios-bookworm-arm64-full.img.xz)
- [Raspberry Pi 32-bit for Raspberry Pi 4 or below with desktop and recommended software](https://downloads.raspberrypi.com/raspios_full_armhf/images/raspios_full_armhf-2024-07-04/2024-07-04-raspios-bookworm-armhf-full.img.xz)

|  |
| --- |
| **IMPORTANT:** |
| For Raspberry Pi 5, we recommend a 64-bit OS for best performance. For Raspberry Pi 4 or below, we recommend 32-bit. However, 64-bit systems will work in any case. |

Next, use a tool like [Etcher](https://www.balena.io/etcher/) to flash the image to your SD Card.

**![](https://support.optisigns.com/hc/article_attachments/34728545820691)**

After flashing the SD card and booting up, you can connect to your network by exiting OptiSigns, mousing up to the top of the Desktop, then clicking the **Network** button.

![raspberry pi os with arrow pointing at network option](https://support.optisigns.com/hc/article_attachments/34726239980563)

### **Step 2: Run/update FUSE**

Raspberry Pi AppImages require FUSE to run. If your existing Raspberry Pi already has the latest version of FUSE, you can skip this step.

|  |
| --- |
| **NOTE:** You'll need a functioning network connection for this. |

First, open the **Terminal** menu on your Raspberry Pi.

![terminal menu raspberry pi](https://support.optisigns.com/hc/article_attachments/34726239983635)

You'll see this screen:

![raspberry pi open terminal](https://support.optisigns.com/hc/article_attachments/34726272219027)

Now input the following command:

```auto
sudo apt install -y fuse
```

As long as you have a valid internet connection, this will install the latest version of FUSE.

### **Step 3: Download OptiSigns AppImage to your Raspberry Pi OS an run it**

Download OptiSigns AppImage file for [Raspberry Pi 5 here](https://links.optisigns.com/arm64), and [Raspberry 4 or below here](https://optisigns.page.link/rpi).

If you are unfamiliar with AppImage, it is a way for a Linux package app to run just like you would run a .app file on Mac or a .exe file on Windows.

Once Downloaded, open **File Explorer**, right-click on the downloaded file and select **Properties**.

![](https://support.optisigns.com/hc/article_attachments/34728529873043)

In the Properties box. Click the Permissions tab in the **Access Control** **→** **Execute** drop-down. Select **Anyone** on all three options. Then Click OK.

![](https://support.optisigns.com/hc/article_attachments/34728529875987)

After that, double-click on the AppImage file to execute it. In the pop-up, select **Execute**.

Raspberry Pi is not very fast, so it may take a few seconds to load. The app will run in full-screen mode, and generate a pairing code for you to pair with the [app.optisigns.com](http://app.optisigns.com/) portal. You can also move the mouse around, and you will see the top 3 buttons to resize, open side bar menu, or close the app.

![optisigns app with arrow pointing to hamburger menu](https://support.optisigns.com/hc/article_attachments/360087500074)

On the side menu, you can set Orientation, etc. The app has Autostart and Fullscreen on Startup checked as default. So now, the next time the Raspberry Pi starts up, it will run OptiSigns app automatically.

![optisigns app menu open](https://support.optisigns.com/hc/article_attachments/360087500094)

### **Step 4: Pair your screen with the OptiSigns portal.**

You can now go to our portal at: <https://app.optisigns.com/> to pair the screen.

If you don't have an account already, create one, or you can also log in with Google or Facebook account.

![optisigns URL being entered in browser](https://support.optisigns.com/hc/article_attachments/360086552573)

Once you log in Click the "Add screen" button

![optisigns app with arrow pointing to add screen button](https://support.optisigns.com/hc/article_attachments/360086552593)

In this pop-up, type in the Pair Code on your player's screen. Then click Pair

![add screen pair code](https://support.optisigns.com/hc/article_attachments/360086552633)

The screen will change to:

![optisigns app showing paired screen](https://support.optisigns.com/hc/article_attachments/360086552673)

### Step 5: Use Optisigns Web portal to assign content and manage your screens.

Once you go to our portal at: <https://app.optisigns.com/>to pair the screen and start assigning content to it, you can follow these guides for more detailed steps:

- [Set up & add a screen](https://support.optisigns.com/hc/en-us/articles/360016374813)
- [How to Upload & Manage Your Files/ Assets](https://support.optisigns.com/hc/en-us/articles/360016247974)
- [How to Create & Use Playlists](https://support.optisigns.com/hc/en-us/articles/28295104605843)
- [Create and Using Schedules with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360016981853)

---

## Summary

Now your Raspberry Pi image already has Digital Signage player features configured:

- Autostart up and launch OptiSigns.
- It will resume, and play what's assigned to it, even after hard power is lost.
- It will not go to sleep.
- It can play downloadable content (images, video, documents) even when internet connection is lost.

---

## Limitations of OptiSigns on Raspberry Pi

While Raspberry Pi do run OptiSigns well under most circumstances, there are a few limitations to be aware of.

- **Video Playback and Encoding** - Raspberry Pi 5's only support hardware decoding for HEVC. Certain apps like Youtube, Vimeo, etc. will display in low-quality due to using software decoding.
- **Video Quality Limitations** - Raspberry Pi is not designed for video playback, and we don't recommend videos in quality over 1080p. This is due to chipset performance limitations.

### That's all!

If you have any questions or issues that need support, please feel free to reach out to us at [support@optisigns.com](mailto:support@optisigns.com).
