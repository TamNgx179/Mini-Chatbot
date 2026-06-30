# How to manually install & activate OptiSigns AI Add-on on Linux or Raspberry Pi

Article URL: https://support.optisigns.com/hc/en-us/articles/360060676993-How-to-manually-install-activate-OptiSigns-AI-Add-on-on-Linux-or-Raspberry-Pi
Article ID: 360060676993
Last Updated: 2025-09-02T20:15:47Z

OptiSigns AI Add-on is a background service running on your Linux, Raspberry Pi device to use a Camera to detect & count people passing by.

If you have not tried to automatically activate this feature, please try it first by following [this guide](https://support.optisigns.com/hc/en-us/articles/27690296225555).

The add-on is a ~200MB app, so it will take several minutes to download and activate on your device, so please be patient after auto-activation before you try manual activation.

If auto-activation fails, then you can follow these steps to manually install & activate AI detection add-on on your Linux or Raspberry Pi devices.

**Before you start, please ensure that you have:**

- Your device has OptiSigns Digital Signage player version 4.2.10 or newer installed. You can download the latest version [here](https://www.optisigns.com/download).
- There's a network connection to your device
- You have enough authorization, and privileges to install apps, and background services on your device
- optisigns-ai-detection runs on any Raspberry Pi OS, or any major Linux distro such as Ubuntu.

## **How to manually install optisigns-ai-detection**

Make sure you have a camera installed on your system.  
Open Terminal.

On Raspberry Pi run:

```
curl -s https://links.optisigns.com/ai-add-on-rpi-install -L | sh
```

On Linux run:

```
curl -s https://links.optisigns.com/ai-add-on-linux-install -L | sh
```

This will download a script and run the installation.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/360099273994)

After you see "Starting OptiSigns AI Detection Service ..." you are done!

You can go back to [app.optisigns.com](https://app.optisigns.com/app/screenManagement) to use the AI feature now

## **Further technical detail for optisigns-ai-detection**

The binary executable is downloaded and installed to ~/bin/optisigns-ai-detection

It will be started as a background service and will be automatically started on system start-up.

This will ensure the AI detection add-on is independent of OptiSigns Digital Signage Player and still running in case the Player has an issue or you need to reinstall it.

You can manually execute the optisigns-ai-detection executable:

```
<path>/optisigns-ai-detection [arg]  
install : to install ai detection agent  
remove : to remove/uninstall ai detection agent  
start or restart : to start ai detection agent service  
stop : to stop ai detection agent service  
version or -V : to print ai detection agent version  
help : to print this instructions  
run : to run the ai detection agent in console or terminal or service  
show or -s: show camera feed
```

## **How to remove optisigns-ai-detection:**

Open Terminal and run:

```
~/bin/optisigns-ai-detection remove
```

If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
