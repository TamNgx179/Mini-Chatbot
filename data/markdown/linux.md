# Linux

Article URL: https://support.optisigns.com/hc/en-us/articles/360034379573-Linux
Article ID: 360034379573
Last Updated: 2025-09-04T19:26:34Z

### In this article, we'll cover how to get OptiSigns running on devices running Linux.

- [Download the OptiSigns AppImage](#Download)
- [Installing OptiSigns on Linux Distributions](#AnyLinux)
- [Additional Instructions for Ubuntu 24.04 or Later](#24.04)  
  - [Install libfuse2 Library to Support AppImage](#libfuse2)
  - [Enabling AutoStart](#AutoStart)
  - [Enabling Video Hardware Acceleration Using MPV Player](#Acceleration)

The OptiSigns Player app can be installed on any Linux machine and used as a player for your digital signs.

OptiSigns app is packaged as AppImage and will run on all major Linux Distribution: Ubuntu, Debian, CentOS, Red Hat, Arch Linux, etc.

---

## Download the OptiSigns AppImage

To install OptiSigns on Linux, you'll need:

- The AppImage for Linux PCs: [**32 bit (x86)**](https://links.optisigns.com/linux-32) | **[64 bit (x64)](https://links.optisigns.com/linux-64)**
- For ARM Processors: [**32 bit**](https://links.optisigns.com/rpi) | [**64 bit**](https://links.optisigns.com/arm64)

---

## Installing OptiSigns on any Linux Machine

Once you've got the latest AppImage downloaded on your system, locate it wherever it's been downloaded.

![optisigns appimage linux](https://support.optisigns.com/hc/article_attachments/37230635291283)

Right click on the AppImage and select **Properties**.

![appimage properties](https://support.optisigns.com/hc/article_attachments/37230646236179)

In the Properties box, ensure the Permissions are set to **Read & Write** and the "Executable as Program" slider is **On**.

![optisigns appimage properties menu](https://support.optisigns.com/hc/article_attachments/37230646238995)

We're not done. Before we can launch the application, we'll need to configure the proper libraries.

Now return to where your AppImage is stored and double click it. If you are running certain distributions that does not come with libfuse2, you will need [an additional step](#24.04).

You'll be asked to confirm Install, hit **Yes**.

![install linux appimage window](https://support.optisigns.com/hc/article_attachments/37230646240915)

The app will run in full screen mode and generate a pairing code for you to pair with the [app.optisigns.com](http://app.optisigns.com/) portal. If you move the mouse around, you will see the top 3 buttons to **resize**, **open** **side bar menu,** or **close** the app.

![optisigns player pair code](https://static.wixstatic.com/media/e48f7f_3ee0de008d8b4f038c0de10250e80749~mv2.png/v1/fill/w_925,h_522,al_c,q_90,usm_0.66_1.00_0.01/e48f7f_3ee0de008d8b4f038c0de10250e80749~mv2.webp)

On the side menu, you can set Orientation, etc. The app will have the AutoStart and Fullscreen on Startup features checked as default. However, more setup is needed if you'd like the app to AutoStart.

![optisigns player side menu](https://static.wixstatic.com/media/e48f7f_2fc697a5f1224304b2a6b23835a38355~mv2.png/v1/fill/w_925,h_518,al_c,q_90,usm_0.66_1.00_0.01/e48f7f_2fc697a5f1224304b2a6b23835a38355~mv2.webp)

---



## Installing OptiSigns on Ubuntu v. 24.04 or Later

Ubuntu v. 24.04 introduced some changes which will require some additional steps to get OptiSigns working properly.

First, follow [all the instructions above](https://support.optisigns.com/hc/en-us/articles/37162616928659#24.04). Next, you'll need to download the libfuse2 driver.

### Install libfuse2 Library to Support AppImage

To do this, open your **Terminal** and type:

```
sudo apt install libfuse2
```

![linux terminal libfuse2 install command](https://support.optisigns.com/hc/article_attachments/37230646245011)

The necessary libraries will automatically install, and now the OptiSigns AppImage can be launched.

Now, there are a few optional things you can do to further optimize OptiSigns on Ubuntu 24.04 or later, including:

- Enabling AutoStart
- Enabling Video Hardware Acceleration via MPV Player

These are completely optional, but helpful for your experience.

### Enabling AutoStart

To enable AutoStart, we will need to alter the startup configuration on Ubuntu. To do this, we'll be setting up a shell script to run independently. This can be easily accomplished in around two minutes via Startup Applications Preferences.

Open up **Startup Application Preferences** and you should see something like this:

![linux startup programs](https://support.optisigns.com/hc/article_attachments/37230635312147)

The issue here is that the OptiSigns Digital Signage will not work after repeated startups. To get it working, hit **Add.**

![linux startup add program](https://support.optisigns.com/hc/article_attachments/37230635315091)

Name the file whatever you please and input any Comment you want. The **Command:** line is what's important here: put the same path as the basic OptiSigns autostart program, but add:

```
--no-sandbox
```

To the end of the command.

Once this is done, your player will continually autostart with each boot. You can delete the old OptiSigns startup script if you wish.

### Enabling Video Hardware Acceleration via MPV Player

In certain situations, Linux running Ubuntu 24.04 or later can struggle to play multiple or very high quality videos using the OptiSigns player.

In these situations, we recommend a very simple set of commands that should fix the issue.

First, if you're **using an Intel processor,** you'll need to download the proper drivers. Type this into the Terminal:

```
sudo apt install intel-media-va-driver-non-free
```

Next, you'll need to install MPV Player with this command:

```
sudo apt install mpv
```

Last, you'll want to hide the taskbar and top bar in the player. You'll need to input this command in order to get started:

```
sudo apt install gnome-shell-extension-manager
```

From here, head to **Settings.** Go to **Ubuntu Desktop**, and make sure **Auto-hide the Dock** is switched to ON.

![linux settings auto hide dock](https://support.optisigns.com/hc/article_attachments/37230646253459)

Next, open up the Extension Manager. Here, click **Browse**, then search for the "Hide Top Bar" extension. Click **Install**.

![linux extension manager hide top bar](https://support.optisigns.com/hc/article_attachments/37230893391763)

Now your video hardware acceleration should be enabled.

### **That's all!**

You now can go to our portal at: <https://app.optisigns.com/>to pair the screen and start assigning content to it. For detail steps to get your screens started, please follow these guides:

- [Set up & add a screen](https://support.optisigns.com/hc/en-us/articles/360016374813)
- [How to Upload & Manage Your Files/ Assets](https://support.optisigns.com/hc/en-us/articles/360016247974)
- [How to Create & Use Playlists](https://support.optisigns.com/hc/en-us/articles/28295104605843)
- [Create and Using Schedules with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360016981853)

If you have feedback on how to make the how-to guides better, please let us know at: [support@optisigns.com](mailto:support@optisigns.com)
