# How To Create and Use Operational Schedules (HDMI-CEC, RS-232)

Article URL: https://support.optisigns.com/hc/en-us/articles/28598173096723-How-To-Create-and-Use-Operational-Schedules-HDMI-CEC-RS-232
Article ID: 28598173096723
Last Updated: 2026-06-02T22:08:42Z

### Do you want your screen to automatically turn on and off according to a schedule to save time and energy? Operational Schedule, an all-in-one feature, makes this easier than ever before!

|  |
| --- |
| Use Case |
| In a corporate office setting, this feature can be employed to control the power, volume, and brightness settings of digital displays across multiple conference rooms and common areas, ensuring they operate only during designated business hours or specific events. |

**In this article:**

1. [Introduction to Operational Scheduling](#Introduction)
   - [Schedules vs. Operational Schedules](#VS)
2. [Assigning Operational Schedules to Screens](#Assigning)
3. [Create Your Own Advanced Schedule](#Create)

## **Introduction to Operational Scheduling**

Operational Schedule allows you to schedule when your TV powers on/off and to control the volume and brightness through the device level, HDMI-CEC, or RS-232 connections. HDMI-CEC is a popular feature available on most consumer TVs right now, while RS-232 is useful for commercial-grade displays.

|  |
| --- |
| Limitations |
| - You will need the **Pro+ Plan** or above to have access to this HDMI-CEC and RS-232 feature. The HDMI-CEC or RS-232 capabilities allow you to Power On/Off your TV using the Operational Schedule, and change the volume or mute the screen. |
| - If you have the **Free** or **Standard** plan and create an Operational Schedule, the player will display black to save power and device life. Free and Standard plan users will not have access to the "Advanced Scheduling" option: |
| - To access Operational Schedule with an HDMI-CEC port, you will need our [**OptiSigns Android Player**](https://shop.optisigns.com/products/optisigns-android-stick-player-2), [**Pro Signage Player**](https://shop.optisigns.com/products/optisigns-digital-signage-player), [**ProMax Player**](https://support.optisigns.com/hc/en-us/articles/38680194603155-OptiSigns-ProMax-Player), Windows, or Linux devices. The player will need to be plugged in to an HDMI-CEC port to function. RS-232 functionality can be used with any device which supports it.   - Please ensure your Android Player device is ***powered from an outlet, not the screen's USB port.***If plugged into the USB port, the act of turning off the screen will also power off the device - meaning, it will not be able to turn the screen back on.   - Operational Scheduling is not supported on Roku nor Samsung Tizen devices. The option will not be visible. |

**One last important note:**

HDMI-CEC is referred to by numerous names. Depending on the brand of your TV or device, it might be called something else, and may need to be enabled in the device software.

Here is a complete list of [**TV Manufacturer CEC Names**](https://support.klipsch.com/hc/en-us/articles/360045728971-TV-Manufacturer-CEC-Names). Simply find your device on the list and enable HDMI-CEC, if necessary.

### Schedules vs. Operational Schedules

**Operational Schedules** are distinct from **Schedules**, which allow you to schedule the actual content which appears on a digital sign.

- **Operational Schedules** are for turning *on and off the actual display*.
- **Schedules** are for displaying *what content or playlists will display on the display*.

For more on Schedules, see our article on [**Creating and Using Schedules**](https://support.optisigns.com/hc/en-us/articles/360016981853-Creating-and-Using-Schedules-with-OptiSigns).

---

## **Assigning Operational Schedules to Screens**

**1. Navigate** to [**Screens Management**](https://app.optisigns.com/app/screenManagement), then select **Edit** on your desired screen.

![](https://support.optisigns.com/hc/article_attachments/28598173050899)

**2.**Select **Operational Schedule**, then select your schedule from the dropdown menu:

1. **Default Schedule**: Screen is on, 4:00AM - 11:59PM, every day
2. **New:** Create your own schedule

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/39032325151379)

**3.**If **Default Schedule** is selected, the time and days can adjusted by clicking **Edit**.

|  |
| --- |
| **Note:** ***Advanced Scheduling** will allow you to create your own schedule.* |

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/39032349012883)

**4.**Select your **Operational Schedule**, assign your desired content, then click **Save.**

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/39032349013267)

**5.** Once saved, your TV power will be on during the operational schedule and will be turned off or display black outside of the operational schedule.

|  |
| --- |
| Note: If there is nothing scheduled, your screen will automatically turn off or display a black screen during that time. You don't need to set a specific schedule for this function to activate. |

---

## **Create Your Own Advanced Schedule**

**1.**Navigate to your [**Screens Management**](https://app.optisigns.com/app/screenManagement), select your desired screen, click **Operational Schedule**, select **+ New** from the Operational Schedule dropdown menu.

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/39032349024531)

**2.** Select your desired event time by clicking on a time, then drag-and-dropping to create an event.

On the side menu, you can customize your schedule with the following options:

![](https://support.optisigns.com/hc/article_attachments/40739915922835)

1. 1. **Name:** Create a name for your schedule. We ***highly recommend*** doing this so as to differentiate it from other Operational Schedules you may wish to make.
   2. **Time:**This is the time of your event, click on it to edit the day and time.![](https://support.optisigns.com/hc/article_attachments/28598178564627)
   3. **Repeat:**Choose whether you'd like your event to repeat from the available options, or create your own custom repeat.![](https://support.optisigns.com/hc/article_attachments/28598178568211)
   4. **Power:** Choose from On, Off, HDMI-CEC On or Off, or RS-232 On or Off.
      - **On:** Sends a signal to turn the screen **ON** during the designated hours. This will be through RS-232 first if available, then through HDMI-CEC. This is our ***recommended option.***
      - **Off:**Sends a signal to turn the screen **OFF**during the designated hours. This will be through RS-232 first if available then through HDMI-CEC.
      - **HDMI-CEC - On:**Sends a command to turn the screen **ON**using HDMI-CEC during the designated hours.
      - **HDMI-CEC - Off:**Sends a command to turn the screen **OFF**using HDMI-CECduring the designated hours.
      - **RS-232 - On:**Sends a command to turn the screen **ON**using RS-232 during the designated hours.
      - **RS-232 - Off:**Sends a command to turn the screen **OFF** through RS-232 during the designated hours.

        |  |
        | --- |
        | **Note:** *Your device will try RS-232 first if available, then HDMI-CEC command to turn off TV/Monitor. Your TV/Monitor model and player needs to support this feature for it to work. Players sold by OptiSigns support HDMI-CEC and RS-232.* |

        ![](https://support.optisigns.com/hc/article_attachments/28598178570771)
   5. **Mute:**Choose if you'd like your screen to be mute or not if sound is available.
   6. **Volume:**Adjust the volume of the screen.
   7. **Brightness:** Adjust the brightness of the screen, with 100% being your screen's current brightness.
   8. **RS-232 Commands:** If you have already configured [**RS-232 commands**](https://support.optisigns.com/hc/en-us/articles/9061950942995-Using-RS-232-to-Schedule-TV-Power-On-Off-or-other-commands), you can select them from this dropdown.
   9. **HDMI Lock:**If checked, the system will periodically check which HDMI input the TV is using. If it detects that the TV has been switched away from the OptiSigns HDMI-CEC input, it will automatically switch back. This check runs approximately once every hour.

**3.**Make sure to **Save** your event at the bottom so that it will assign the event to the schedule. Then, click "**Apply**" to assign it to your screen.

![](https://support.optisigns.com/hc/article_attachments/28598178573587)

**4.**Once applied, click **Save** to apply and activate all changes to your screens.

![](https://support.optisigns.com/hc/article_attachments/28598173087891)

With that, you've created your Operational Schedule. This schedule can be ***reused as often as you like***, and can be applied to numerous screens. Simply select it from your Edit Screen tab for each screen you'd like to apply it to.

### That's all!

If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
