# Using RS-232 to Schedule TV Power On/Off or other commands

Article URL: https://support.optisigns.com/hc/en-us/articles/9061950942995-Using-RS-232-to-Schedule-TV-Power-On-Off-or-other-commands
Article ID: 9061950942995
Last Updated: 2025-09-19T18:38:49Z

With OptiSigns, you can schedule TV Power On/Off using the advanced schedule feature. There are 2 ways you can do it with OptiSigns depending on what devices you are using.

- If you are using a consumer-grade TV and an OptiStick, the TV Power On/Off is achieved through HDMI-CEC. See our **[Operational Schedule](https://support.optisigns.com/hc/en-us/articles/28598173096723-How-To-Create-and-Use-Operational-Schedules-HDMI-CEC-RS-232)**article for more information.
- If you are using a commercial-grade display, RS232 will be the option for you.

In this article, we will walk through how to set up the external communication for RS-232 and use it to control your commercial display power on/off. It consists of 3 steps at a high level.

1. Set up RS-232 connection for serial communication.
2. Configure the RS-232 command for your display and set up the template
3. Create the Power On/Off Schedule

The same procedures can be used to send other RS 232 compliant commands as well.

Supported devices/platforms: Windows, Linux, Raspberry Pi, OptiStick, and OptiSigns Pro/ProMax players.

**1. Create RS-232 connection**

Go to the admin console and expand Advanced, click on the link for external communication. You can also use the link below.

<https://app.optisigns.com/app/s/external-coms>

Click "Add New" button, to create a new RS-232 connection.

![chrome_ThjlLpoiH0.png](https://support.optisigns.com/hc/article_attachments/32323154940819)

In the connection creation window, you can give a name to the connection and define the serial port to use, Baud Rate, Data bits, Stop bits, and Parity. This info is determined by the commercial display used, you should be able to get it from your TV user manual.  Flow control is normally not needed in this case, you can just leave it blank.

![chrome_972ixLupAY.png](https://support.optisigns.com/hc/article_attachments/32323154949651)

Click "Save", once the configuration is complete.

To know which serial port is used, you will need to check it on your device. Using Windows as an example, you can find it in the device manager, it will list out the COM port available. On Linux/Raspberry Pi, the serial port is normally "/dev/ttyS0" or "/dev/ttyUSB0" if a USB serial adapter is used. On OptiSigns pre-configured Android Stick, you can use "USB0" as the serial port.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/9062308259731)

**2. Configure RS-232 command and set up the template**

Go to the "Commands" tab, and click the "Add New" button.

![chrome_kVTicFpYv5.png](https://support.optisigns.com/hc/article_attachments/32323154954003)

Set the RS-232 command of your commercial display in the pop-up window. You can choose "asc ii" or "hex" encoding depending on your TV, and the end of line value can be set here accordingly as well.

You will need to create a command for Power On, and a command for Power Off.

![chrome_QGt8AmZbeI.png](https://support.optisigns.com/hc/article_attachments/32323291436947)

Once commands are created, go to the "Templates" tab, this is where you map the commands to the Power On/Off action. You only need to create a template if the commands are different. For example, if you are only using Samsung commercial TVs, which all have the same commands for power on/off, then you only need to create one template for it, it can be used on all the Samsung TVs you have deployed.

![chrome_0RqFJkgyu4.png](https://support.optisigns.com/hc/article_attachments/32323151390739)

Map the command to the actions. The actions will be used in the advanced schedule. Save it after the mapping is complete, then the template is ready for use.

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/9062485175059)

**3. Set up Power On/Off schedule**

Once the RS-232 configuration is complete, you will need to set up an Operational Schedule.

Go to the Edit Screens, then go to the **Operational Schedule**section. Hit **New**.

![](https://support.optisigns.com/hc/article_attachments/40414890419859)

You'll see the Operational Schedule screen. Here, click anywhere you'd like to schedule a Power On/Off.

![](https://support.optisigns.com/hc/article_attachments/40414890422803)

Once you've done this, you'll see this menu pop up on the side:

![](https://support.optisigns.com/hc/article_attachments/40414884380947)

Here, the relevant piece is **Power**. Clicking this will show a drop-down:

![](https://support.optisigns.com/hc/article_attachments/40414890424723)

To power your screen on or off using RS-232, there are two relevant options:

- **To Power Screen ON -** Choose either **On**or **RS-232 - On**. The first option will make use of RS-232 first, then HDMI-CEC as a fallback. The second will only utilize RS-232.
- **To Power Screen OFF -**Choose either **Off**or **RS-232 - Off**. The first option will make use of RS-232 first, then HDMI-CEC as a fallback. The second will only utilize RS-232.

That's all! Now you have learned how to schedule TV power on/off using RS-232.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
