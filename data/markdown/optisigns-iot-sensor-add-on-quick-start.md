# OptiSigns IoT Sensor Add-on - Quick Start

Article URL: https://support.optisigns.com/hc/en-us/articles/13097501958291-OptiSigns-IoT-Sensor-Add-on-Quick-Start
Article ID: 13097501958291
Last Updated: 2025-09-02T18:16:29Z

### How to quickly get your IoT sensors up and running on any screens you wish.

In this article:

- [Set Up Serial Communication Channel](#Serial)
- [Set Up IoT Sensor via Lift and Learn](#Lift)
- [Assign the IoT Sensor to a Screen](#assign)
  - [Option 1: Through Lift and Learn](#1)
  - [Option 2: Through Edit Screen Menu](#2)
- [Advanced Settings](#Advanced)

|  |
| --- |
| **NOTE:** This feature requires the **Engage plan** or higher. |

---

The OptiSigns IoT Sensor Add-on allows you to use any IoT sensors that work with serial communication to interact with your screens. You'll be able to:

1. Detect and monitor sensor data about the surroundings, such as motion, temperature and humidity, object liftup/placedown.
2. Responsively display different content based on the sensor event that was received by the player connected to the screen.
3. Send command to other IoT devices to control its behavior, e.g. turn on the atmosphere light, turn on/off the screen monitor.

Our YouTube video shows how it supports the lift and learn use cases using a Nexmosphere brand sensor.

*This feature supports Windows, Linux , MacOS, BrightSigns Player, and our pre-configured Android Stick.*

---

## **Quick Start Guide for OptiSigns IoT Sensor Add-on**

For the following example, we will use a temperature sensor with an **Arduino** board to demonstrate how it works. ***Your board may have slightly different connection options - we will note instances where this may be the case.***

The temperature sensor will send data in its own format to the OptiSigns player through serial communication. The temperature data can be displayed on the screen in realtime, and when the defined condition met, the screen content will change to show overheat status.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/13110301584531)

Setting up the IoT sensor add-on will take three steps:

1. Set up the serial communication channel.
2. Set up IoT sensor via Lift and Learn
3. Activate the IoT sensor on the screen and assign the IoT sensor addon app to it.

From there you can modify the set up to fit your need.

---

## **1. Set Up Serial Communication Channel**

In the top right corner, click on the account name.

Then, click **Personal Profile →** Look to the left hand column.

Expand **"Advanced" →** **"External Communications (RS232)"**.

![firefox_kDKZkQZT6x.png](https://support.optisigns.com/hc/article_attachments/32208926824211)

*You can also go the the page using this link: **<https://app.optisigns.com/app/s/external-coms>***

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/13110350933139)

Click **"Add New"** in the **Connections** tab to bring up the **Create New Connection** page, where you can define the parameters for the serial communication.![firefox_KBKtcrjYw5.png](https://support.optisigns.com/hc/article_attachments/32208926832787)

|  |
| --- |
| **NOTE:** Most of the required settings will depend on your device. Please see your device's documentation for specific information. |

We are only going to cover three main settings off this screen: **Name, COM Port,** and **Baud Rate.**

- **Name:** A quick name for your sensor. Enter whatever you'd like.
- **COM port:** Designates which serial port the serial communication channel will enter from.  
  Please note, different systems will organize the serial port differently.
  - **Windows:** Normally represented as "COM#". This will depend on the port you've plugged the sensor into.
  - **Linux:** Normally represented as something like "/dev/ttyUSB0" or "/dev/ttyACM0".
  - **Brightsigns:** Normally represented as "1" or "2"
  - **OptiSigns Preconfigured Android Sticks:** Usually is "USB0"

|  |
| --- |
| **NOTE** |
| You can find your COM Port by navigating to the **Trigger Event Viewer**page on your screen and clicking on "Show": |

- **Baud Rate:** This is a device specific number. For this example, we're using a Baud rate of 9600 for the communication with Arduino board. When using Nexmosphere sensors, the baud rate is always 115200.

Also note, both Arduino board and Nexmosphere controller are using USB port, please make sure the media player you use comes with USB port.

The other options (Data Bits, Stop Bits, Parity, Flow Controls, Receive Line Ending (EOL), Receive Encoding) are highly advanced and **are best left at default** unless your device specifies otherwise.

**Save** the connection once the configuration is complete and then it is ready for use.

|  |
| --- |
| **NOTE:** If you wish to set up custom commands to send to your sensor now, see the ***Set Up Custom Sensor Commands*** section of this guide. |

---

## **2. Set Up IoT sensor via Lift and Learn**

The IoT sensor is configured through our **"Lift and Learn"** builder, found under the **Engage** tab.

![firefox_h7cyVMoyaT.png](https://support.optisigns.com/hc/article_attachments/32208926838675)

Once you've selected Lift and Learn, click **Build.**

![ZgbrWWmul3.png](https://support.optisigns.com/hc/article_attachments/32208910745747)

![S0kR2qEg9y.png](https://support.optisigns.com/hc/article_attachments/32208910750355)

|  |
| --- |
| **NOTE:** In the case of custom commands, these are often device specific. Your user manual may have several basic commands. More commands can be determined through OptiSigns; however, the rest of the setup process will need to be completed first. |

- **Name:** This is an internally facing name that will help you organize your IoT devices. Type whatever you wish.
- **Change Content:** Switch between "Immediately" and a "Delay" of your choice in milliseconds.
- **Play for at least:** When triggered, the app will play the content corresponding to the play rule for as many seconds as you select here. We recommend keeping this at 3 seconds to give a smoother experience, just in case the triggering events are met frequently.
- **Rest for:** When the triggering condition is not met, the device will resume playing the content assigned to it for this number of seconds. We recommend keeping this at 3 seconds to give a smoother experience, just in case the triggering events are met frequently.
- **Play Rules:** Set content you want to play when the corresponding trigger event fires.  
  - **Effective Time:** Determines the time at which the IoT sensor is active. You can select times and days of the week, or a customized schedule.
  - **If Detected:** Sets the command trigger for the rule. This can be one of two preset options, or a custom command. This is a command *received* from the sensor.  
    - **Tag picked up:** If something is placed on the sensor and then picked up, this will trigger the rule. This gives a Default value specifically for Nexmosphere sensors. Please see the below sectionto get the exact command for your sensor.
    - **Tag put down:** If something is put down on the sensor, this will trigger the rule. This gives a Default value made for Nexmosphere sensors. Please see the below section to get the exact command for your sensor.
    - **Full Command:** A custom command can be input below.
  - **"</>":** A Javascript-based function where you can apply the needed logic to process the incoming command and derive the needed result. In the below example, the Ardunio board will send the temperature data from the sensor in a string, the processing rule extracts the temperature value and determine when the "TOOHOT30" custom command triggers the event.

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/13110786060691)

- - **Play Content:** Determines what content plays (or stops) when trigger conditions are met. Options are "Asset," "Playlist," or "Stop Playing."
  - **Commands:** Allows you to send out commands to sensors instead of just receiving them. If you're using a typical IoT sensor, **you most likely won't need to use this**. These are typically used for other types of devices, such as atmospheric lighting or speakers. These commands are created in the "Commands" section of the "External Communications (RS232)" section from before. We will be returning to this later in the article.
  - **Action:** Allows you to move a Rule's place in the list, or delete them.
- **Add Rule:** Allows the creation of more rules, with no maximum. These can be deleted or organized via the Action setting.

We ***strongly recommend*** obtaining a string command and inputting it into the **Play Rules**section. This will reduce or eliminate any potential issues.

To do this, boot up your screen and navigate to the OptiSigns main menu. Scroll down until you see **Trigger Event Viewer**.

![firefox_VujXdIW6kJ(1).jpg](https://support.optisigns.com/hc/article_attachments/42985157371027)

When your sensor is properly configured, you will be able to see it mapped to a COM port. This information can be  By placing pressure on the sensor, a **string** will appear on the right side of your screen. By typing this **case-sensitive** string into your **If Detected** area, your issues will likely resolve.

![firefox_ISUylb5Aq5.png](https://support.optisigns.com/hc/article_attachments/32208926880915)

This is the easiest way to get these command strings for non-Nexmosphere brand sensors. You can also find these command strings by looking at your manufacturer's website.

Once you've got everything set up to your liking, hit **Assign** to move to the next step.

---

## **3. Assign the IoT Sensor Add-on app to a Screen**

There are two options for assigning your Sensor Add-On to a screen.

### Option 1: Through Lift and Learn

![firefox_vDbwOLdUam.png](https://support.optisigns.com/hc/article_attachments/32208926865683)

Once you've created the parameters for your IoT sensor, you can assign it directly to one of your screens. There are two options:

- **Target -** Select between Screens and Tags. Selecting one or the other will change the next option to either Screens or Tags, depending on which you select here.
- **Screens / Tags** - Select which screen or tag will be associated with the sensor. This determines where your content will appear.

### Option 2: Through the Edit Screen Menu

You can also assign your completed Sensor app to a screen through the [Edit Screen Menu.](https://support.optisigns.com/hc/en-us/articles/360048914673-Edit-Screen-What-does-each-option-do)

To get there, go to Screen Management and click Edit the screen you want to add this Add-on to.

Click **Advanced** **→** **More** **→** **Sensor Add-on → Activate** to open up more options.

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/13110881710611)

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/13110883397907)

- **Sensor Add-on -** This is the IoT Sensor Add-on we created earlier. You can cycle through your created apps here.
- **Sensor COM Connection** - This is the serial communication channel we created in the first step. Select it here!
- **Sensor Commands Template -** This sets an external command template. If you're using an IoT sensor, you **should not need to use this device**.
- **External COM -** This for when you need to send a command out. Most users will want to leave this unchecked.

On the screen, you should also select the standard content that should be played on the screen in the normal, in this case we use the "Heat Sensor - Normal" asset that display the standard content and also data from temperature sensor in real time.

Once IoT Sensor Addon is activated, you can assign the IoT sensor Add-on app that was created earlier, in this case it is called "Sensor". And also select the sensor connection that was created in the first step, in this case it is "Arduino - Win". Since we are only receiving commands from sensors, we will leave the sensor commands template as "None"

---

## **Advanced Settings**

|  |
| --- |
| **Use Case** |
| In special cases when you need to send commands back to external devices, such as a light source or speaker, these options are for you. These options are not needed for those using ordinary IoT sensor devices. |

First, navigate to **External Communications (RS232) →****Add New**

![firefox_Ormk62EJMc.png](https://support.optisigns.com/hc/article_attachments/32208910780051)

This screen will come up:

![firefox_tdPfmJaP56.png](https://support.optisigns.com/hc/article_attachments/32208910797715)

Here you'll see four options:

- **Name -** What you'll call this command. This comes out in the form of a Tag.
- **Encoding** - The type of coding being sent to your device. Choose between "ascii" and "hex."
- **Value** - The actual command string being input. These will vary depending on use case and device.
- **Line Ending (EOL)** - The code for your line ending. Options are "None," "CR," "LF," and "CR + LF." We recommend leaving it at "None."

Once you've configured your Command, press **Save**.

Next, navigate back to **Lift and Learn** and click on your IoT app to edit it. Click the empty box under **"Commands"** and you should be able to select your tag:

![firefox_SASdQOLURh.png](https://support.optisigns.com/hc/article_attachments/32208926902675)

As long as everything is configured correctly, this will allow you to send commands to external devices.

---

**That's all!**

Now you have completed all the needed configurations to use the IoT sensors add-on, just connect the sensors and controller to your screen(media player), then you are ready to go. In this case, the screen will play the standard content like the one on the left with real time data from the temperature sensor, and when the temperature surpasses 30 degrees in Celsius, it will trigger the overheat content on the screen like the one on the right.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/13110301584531)

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
