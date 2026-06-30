# Operational Schedule Troubleshooting

Article URL: https://support.optisigns.com/hc/en-us/articles/48241081473043-Operational-Schedule-Troubleshooting
Article ID: 48241081473043
Last Updated: 2026-04-20T21:26:17Z

### In this article, we will troubleshoot common issues related to the Operational Schedule feature in OptiSigns.

- [Introduction to Operational Scheduling](#Introduction)
- [Changing Display Settings](#ChangingSettings)
- [How to Test HDMI-CEC / RS-232 Connections](#TestConnections)
- [OptiStick Improperly Powered](#ImproperlyPowered)
- [Operational Schedule Works at Different Times from How It Was Set](#DifferentTimes)
- [Screen Turns Off, But Not Back On](#TurnOff)

Operational Scheduling is a feature which allows you to turn off and on your digital signs on a set schedule, further automating your setup. If you’re looking to set up an Operational Schedule of your own, see our guide on [Creating and Using Operational Schedules](https://support.optisigns.com/hc/en-us/articles/28598173096723-How-To-Create-and-Use-Operational-Schedules-HDMI-CEC-RS-232).

However, many factors and settings may need adjustment in order to get this feature running properly. Here, we go through a few of the most common troubleshooting scenarios our teams face.

---

## **Introduction to Operational Scheduling**

Operational Schedule allows you to schedule when your TV powers on/off and to control the volume and brightness through the device level, HDMI-CEC, or RS-232 connections. HDMI-CEC is a popular feature available on most consumer TVs right now, while RS-232 is useful for commercial-grade displays.

|  |
| --- |
| Limitations |
| - You will need the **Pro+ Plan** or above to have access to this HDMI-CEC and RS-232 feature. The HDMI-CEC or RS-232 capabilities allow you to Power On/Off your TV using the Operational Schedule, and change the volume or mute the screen. |
| - If you have the **Free** or **Standard** plan and create an Operational Schedule, the player will display black to save power and device life. Free and Standard plan users will not have access to the "Advanced Scheduling" option: |
| - To access Operational Schedule with an HDMI-CEC port, you will need our [**OptiSigns OptiStick**](https://shop.optisigns.com/products/optisigns-android-stick-player-2), [**Pro Signage Player**](https://shop.optisigns.com/products/optisigns-digital-signage-player), or [**ProMax Player**](https://support.optisigns.com/hc/en-us/articles/38680194603155-OptiSigns-ProMax-Player). The player will need to be plugged in to an HDMI-CEC port to function. RS-232 functionality can be used with any device which supports it.   - Please ensure your OptiStick device is ***powered from an outlet, not the screen's USB port.***If plugged into the USB port, the act of turning off the screen will also power off the device - meaning, it will not be able to turn the screen back on.   - Operational Scheduling is not supported on Roku nor Samsung Tizen devices. The option will not be visible. |

**One last important note:**

HDMI-CEC is referred to by numerous names. Depending on the brand of your TV or device, it might be called something else, and may need to be enabled in the device software.

Here is a complete list of [**TV Manufacturer CEC Names**](https://support.klipsch.com/hc/en-us/articles/360045728971-TV-Manufacturer-CEC-Names). Simply find your device on the list and enable HDMI-CEC, if necessary. This will solve a lot of issues by itself.

---

## Changing Display Settings

In order for Operational Scheduling to work, your TV must actually support it. Operational Scheduling makes use of either:

- **HDMI-CEC** - This is the most common option, and supported by most TVs. See this guide on [HDMI-CEC settings](https://www.helpdesk.nakamichi-usa.com/hdmi-cec-settings) to find your display’s make and model for information on how to set this up to receive signal.
- **RS-232** - This option is most common on commercial displays, and is the most reliable option. ***If you can set up your player to use RS-232, you should, as it is far more reliable than HDMI-CEC***.

|  |
| --- |
| **NOTE** |
| Your device will try RS-232 first if available, then HDMI-CEC command to turn off TV/Monitor. Your TV/Monitor model and player needs to support this feature for it to work. Players sold by OptiSigns support HDMI-CEC and RS-232. |

On most displays, HDMI-CEC or RS-232 will need to be enabled before Operational Scheduling will work. How to do this will vary by TV and connection.

|  |  |
| --- | --- |
| **MORE ON RS-232** | |
| An RS-232 cable should have come with your display. We recommend using this if possible, as there are reportedly issues with certain displays (generally LG) when other RS-232 cables are used.  Your RS-232 ports may look different depending on the age of your display: | |
| **OLDER DISPLAYS:** | **NEWER DISPLAYS:** |
|  |  |
| A typical RS-232 cable which comes with most new commercial displays: | |
| [**Buy USB-A to RS-232 cable for older displays**](https://www.amazon.com/Sabrent-Converter-Prolific-Chipset-CB-DB9P/dp/B00IDSM6BW?dib=eyJ2IjoiMSJ9.eDpH7mZ-MxF1rW_bLcNPOgxDhwo8eCgqihSClktQT86m8ERQwz21Q9euBmQ3zNtrIG2huqPq1a_Yupg_0lAfJD7XCkjpxXR7vDb_WG-28D3-SuPxCy1MVPvoKFbVWg92YGOfKork7n_l1CNOzUJ-R9gMzzuw9iQpODbta2oRWS1vbcaQF9XyY0RrYG6443FJHjRAL09KvJaZCY_6khThywKVe_gaB5qpCHxZzBMbRFk.gkxWaA_HDwYQYoAZKJYArVgEQjxmvGUftl17_EdW9Z0&dib_tag=se&keywords=db9%2Bto%2Busb&qid=1768493612&sr=8-3&th=1) | - [**Buy USB-A to RS-232 cable for newer displays**](https://www.amazon.com/CIQILY-Adapter-Braided-Compurter-Headphones/dp/B0F244GXYD?crid=3F7PMHINSSJV5&dib=eyJ2IjoiMSJ9.9yl--ztyPtBcoMUVrl88mn4TF0qc4F00jdNaYWJiOkE8spJ9Tr2MI7CXTqlfHWzIoXaPXCumrSVQtH7x9o0zmSJMkTSXgb7d9mOjKpugOIQQBLdfDIb2TPzZ9zU2oxpFtYpIMZaY-DShM2y_QlmnFq9lXAXvnJPjKvQ4FXiDiT7u9MGwf_pljN57vDs6JJ4gwbGmz8kDIb78Vd_Oe0mNMbwEvAttq2kKcYdx2RZesSU.g8ca63B6VuAlFGeaF48NG8KONf0XIybCT6T9B9f3DoU&dib_tag=se&keywords=3.5%2Bmm%2Bto%2BUSB-A&qid=1768493667&sprefix=3.5%2Bmm%2Bto%2Busb-a%2Caps%2C159&sr=8-4&th=1) - [**Buy USB-A to RS232 Female Adapter**](https://www.amazon.com/Adapter-Chipset-CableCreation-Converter-Register/dp/B0769DVQM1?crid=3V1RSDNOXKRRK&dib=eyJ2IjoiMSJ9.u5CpMrocxXKM1T6QqugwN6WZNjAMgpYeQrLD7PG2XhgbuJuHAoZSFqwOLpQcJjp2UUQmyVf6LdB5aXazNkDOZ6g10xmHbzhz__e0Z2Z9thclyXehquOcdC5N0EEfTS09SabOOCtNIxDqETc5DteqsJhzczZAt4tP_QSaTk71xOwNNIRDLk0ftLA5LlX8iQHLswNI7w9CZrNJismJ8iYQcedr5vr12ucsj_F0LfXU8mo.g_V1c7cnRq5RTvKb5Ec-8xPvkWdFXYcN05nDOUMC8lk&dib_tag=se&keywords=usb-a%2Bto%2Brs-232%2Bfemale&qid=1768494731&sprefix=usb-a%2Bto%2Brs-232%2Bfemal%2Caps%2C137&sr=8-3&th=1) |

---

## How to Test HDMI-CEC / RS-232 Connections

Here is how to test your HDMI-CEC or RS-232 connection to make sure it works as it should.

Go to **Edit Screen → Advanced → More**:

Click the **Arrow** in the right hand corner of the popup, next to the **Save** option. This will bring up several options. Hit **Send HDMI CEC** or **Send RS232**:

![](https://support.optisigns.com/hc/article_attachments/48241081464467)

This should either turn on or turn off the TV depending on whether the TV is currently on or off. If it does not, keep troubleshooting.

---

## OptiStick Improperly Powered

It is possible to power the OptiStick via a USB port on your display. However, in addition to [the other problems this causes](https://support.optisigns.com/hc/en-us/articles/40147900639891-OptiStick-Troubleshooting-Guide#Power), powering an OptiStick via USB will cause significant problems with the Operational Schedule feature.

Think about it this way: your OptiStick is tasked with powering down and powering off your display, but it is relying on that display to pull power from. Once the display is off, how is the OptiStick supposed to turn it back on? There is no power reaching it. That’s why it needs its own dedicated power source (i.e. outlet) to use Operational Scheduling properly.

For this reason, if you want to make use of Operational Scheduling with an OptiStick, ***be sure to plug it into a dedicated outlet, not the USB port.***

---

## Operational Schedule Works at Different Times from How It Was Set

This is very common and almost always goes back to the device Time Zone. Your first troubleshooting step for this issue should be to set the time zone.

This can be done either with the device itself, or remotely (if the device is online). To update it remotely, edit the screen, then hit **Advanced**. You should see the below bar, click the **Time Zone** button:

![](https://support.optisigns.com/hc/article_attachments/48241081465107)

This will open up the **Update Time Zone** screen:

![](https://support.optisigns.com/hc/article_attachments/48241081468307)

Here, simply select the appropriate Time Zone for your device. This should match the Operational Schedule you’ve set to it. Now, they should be aligned.

---

## Screen Turns Off, But Not Back On

One of the main reasons for this is that the [OptiStick is improperly powered](#ImproperlyPowered). However, another possible reason (regardless of the device being used) is that Operational Scheduling might not be supported on your individual TV, regardless of settings. This is a limitation of the device.

Assuming the OptiStick is plugged into a wall socket and this issue persists, here is what you can try:

- Replace the HDMI-CEC connection with RS232. This issue usually occurs because, for whatever reason, your TV is not able to make use of this feature. Plugging in a [USB-to-RS232 cable](https://www.amazon.com/Adapter-Chipset%EF%BC%8CDB9-Serial-Converter-Windows/dp/B0759HSLP1?crid=DJRK1PMU1XP8&dib=eyJ2IjoiMSJ9.xWQsG3VO7IqOId9P7LqGZq38EEH2QvMypF3SndBiNDHIJy8eXhJM5OWgnvi9cefD87NcVoHJfzIkkhm2fj93LMSdKLrVOwYtWWretyo9_0FcYXKCIxmNeWMwVU9X3Z3vrYr-W6kVTPsxwJfIz75S02drmPkfed8r3lXBbfeClyFQGjAnhrk1T1vW6iTvz8ihzawazD_PKzN4x49gEZM9oRjwOCH8_JAn-_n9xyI2p5RzYrPYxL_7EFAlBzAt4zlFuchQub82kkAddhtogG2jdNx92nxsfT-ocOsD2PEZq7U.uLskW3KPqzSxswulRF9kaQzYhjBL8nVFvpU3GjB1wMQ&dib_tag=se&keywords=USB%2Bto%2BRS232&qid=1768418871&s=electronics&sprefix=usb%2Bto%2Brs232%2Celectronics%2C180&sr=1-3&th=1) usually fixes these issues. For Pro/ProMax users, this [3.5mm-to-RS232 cable](https://www.amazon.com/Wpeng-Female-3-5mm-Serial-Conversion/dp/B06WLP4LTP?crid=2TJVY9W17FGXA&dib=eyJ2IjoiMSJ9.Y6_VGAouYwBNLtnwPYqjn-7cydyPVjGKK0bAEUGUF8eIUkzSYL1ZP9NZRBcu05_r1XxGY3Z1QvyptSulXNnCQH125i4Jjfgx2Qt0uSAmgg2Wgdm3XwCtixWVVfdMD_n8r0nKRjLWXHtwauI8uI6MUHKhfuv7g4U1CM6IpPvwo4wo5eG0AUrFo4h52R25zD1XtpLffAo54EJDoy2rHtJuiQwlKBtci_9Wl5_6seGMHLk.EMlyYI-DF9Ak6MFx4QxzmJVovu79dk4VaYEdXmMZXs8&dib_tag=se&keywords=rs232+cable+jack&qid=1768421592&sprefix=rs232+cable+jac%2Caps%2C169&sr=8-3) will also work.

If you've tried the above, feel free to [reach out to our support team](https://support.optisigns.com/hc/en-us/articles/35626165056787-How-to-Contact-OptiSigns-Support).

### That’s all!

Still having problems with getting your Operational Schedule to work? Reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com) for additional help.
