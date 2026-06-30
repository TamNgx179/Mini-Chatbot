# Advanced: How to Manually Install & Activate OptiSigns Remote Agent on Linux or Raspberry Pi

Article URL: https://support.optisigns.com/hc/en-us/articles/360057146573-Advanced-How-to-Manually-Install-Activate-OptiSigns-Remote-Agent-on-Linux-or-Raspberry-Pi
Article ID: 360057146573
Last Updated: 2025-09-02T20:02:58Z

### In this article, we will show you how to complete a manual installation of the OptiSigns Remote Agent on a Linux or Raspberry Pi device.

If you're running OptiSigns on a Windows, Linux or Raspberry Pi device, you can install optisigns-remote-agent add-on that will allow you to remotely control your device from the portal.

If you have not tried to automatically activate this feature, please try it first by following [this guide](https://support.optisigns.com/hc/en-us/articles/360055486554).

If automatic activation fails, follow these steps to manually install & activate the OptiSigns remote agent on your Linux or Raspberry Pi device.

**Before you start, please ensure that:**

- Your device has OptiSigns Digital Signage player installed. Download the latest version [here](https://www.optisigns.com/download).
- Your device has an active network connection.
- You have the authorization and privileges to install apps and background services on your device.

|  |
| --- |
| **NOTE** |
| The Remote Control feature is only available to subscribers with a **Pro Plus** **plan or above.** |

## **How to manually install optisigns-remote-agent**

Open Terminal.

On Raspberry Pi run:

```
curl -s https://release.optisigns.com/optisigns-remote-agent-setup-rpi.sh -L | sh
```

On Linux run:

```
curl -s https://release.optisigns.com/optisigns-remote-agent-setup-linux.sh -L | sh
```

This will download a script and run installation.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/360095986553)

After you see "Starting Remote Control Service ..." you are done!

You can go back to app.optisigns.com to use Remote Control feature now.

![](https://support.optisigns.com/hc/article_attachments/18614175492243)

## **More Technical Details for optisigns-remote-agent**

The binary executable is downloaded and installed to ~/bin/optisigns-remote-agent

It will be started as a background service and will automatically boot on system start up.

This ensures the remote agent is independent from OptiSigns Digital Signage Player and still running in case the Player encounters an issue, or you need to reinstall it.

You can manually execute the optisigns-remote-agent executable:

```
<path>/optisigns-remote-agent [arg]  
install : to install remote agent  
remove : to remove/uninstall remote agent  
start or restart : to start remote agent service  
stop : to stop remote agent service  
version or -V : to print remote agent version  
help : to print this instructions  
run : to run the remote agent in console or terminal or service
```

## **How to remove optisigns-remote-agent:**

Open Terminal and run:

```
~/bin/optisigns-remote-agent remove
```

### That's all!

OptiSigns is a leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
