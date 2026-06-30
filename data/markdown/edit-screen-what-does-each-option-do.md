# Edit Screen: What does each option do?

Article URL: https://support.optisigns.com/hc/en-us/articles/360048914673-Edit-Screen-What-does-each-option-do
Article ID: 360048914673
Last Updated: 2026-05-21T13:09:58Z

### OptiSigns gives you unparalleled customization options for your digital signs with its Edit Screen feature. Each setting will be thoroughly explained to ensure you can effectively manage and customize your digital signage.

In this article:

- [Navigating to Edit Screen](#Navigating)
- [Edit Screen Options](#Edit)
  - [Advanced](#advanced)
  - [More](#more)
  - [Device Additional Attributes](#attributes)
  - [Device Info](#info)
  - [OptiSigns Player Specific Settings](#android)
  - [More Remote Command Options](#remote)
  - [Final Options](#final)

|  |
| --- |
| **NOTE** |
| If you're new to OptiSigns, you'll be using one of two interfaces: the **1.0** interface, or the **Updated** interface. For your convenience, we've provided screenshots of each. |

---

## Navigating to Edit Screen

Navigate to the [**Screens page**](https://app.optisigns.com/app/screenManagement)in OptiSigns portal → Find your desired screen → Click '**Edit**' or click the screen name:

|  |  |
| --- | --- |
| **OptiSigns 1.0** | **Updated** |
|  |  |

The Edit Screen window, shown below, will appear.

---

## Edit Screen Options

|  |  |
| --- | --- |
| **OptiSigns 1.0** | **Updated** |
|  |  |

- **Device Name -** Name of your screen
  - This will **not** be displayed on your screens. It is best used as a way for you to know which screen is being accessed.
- **Tags -** These are free-form text fields that you can use to organize using a nomenclature that makes sense to your team.
  - These help with organizing, searching, and managing screens efficiently. Tags are particularly useful when pushing content to multiple screens simultaneously.
- **Type -** Select what will be bound to the screen
  - **Asset**: This is a specific content type such as images, videos, or app instances i.e. Weather app or Designer app
    - You can click on '**Change**' to change the Selected Asset
    - When the '**Asset**' option is selected, you have the ability to choose from different scaling options - None, Fit, Stretch, or Zoom.
  - **Playlist**:  Selecting this allows you to [Select a Playlist](https://support.optisigns.com/hc/en-us/articles/28295104605843) from the drop-down which will bind the screen to that playlist.
    - A playlist is a grouping of assets and or nested playlists in a specific order.
    - You can click on 'Go To' to go to the selected playlist. It will open a new window and display the playlist and its contents.
  - **Schedule**: Selecting this allows you to [Select a Schedule](https://support.optisigns.com/hc/en-us/articles/360016981853) from the drop-down and designate a schedule you want the screen to follow.
- **Scale** - Adjust how your selected content displays and fits to your screen with None, Fit, Stretch, or Zoom.
- **Orientation**- Adjust the positioning of the content on your screen.
  - **Landscape**: Default layout for most screens
  - **Rotate 90 degrees**:  Rotates screen 90 degrees clockwise from landscape.
  - **Rotate 180 degrees**: Rotates screen180 degrees clockwise from landscape.
  - **Rotate 270 degrees**: Rotates 270 degrees clockwise from landscape.

---

## Advanced

Clicking the **"Advanced"** option at the bottom of the Edit Screen window provides the options below.

|  |
| --- |
| **NOTE** |
| The available settings and their ordering in your Edit Screen options may vary depending on your hardware, pricing plan, and version of OptiSigns (1.0 or the Updated UI). |

|  |  |
| --- | --- |
| **OptiSigns 1.0** | **Updated** |
|  |  |

- **Device Locations**
  - **Location** - Set the device's location. This is tied to a city or address.
  - **Functional Location** - Denotes where in your screen is placed, i.e. "Conference Room" or "Hallway"
- **Connection Status**
  - [**Show Downloading Status**](https://support.optisigns.com/hc/en-us/articles/12947300131731) - Set to show or hide downloading status on your screen
  - [**Show Offline Indicator**](https://support.optisigns.com/hc/en-us/articles/12498801963027) - Show an icon on the screen when there's no network connection, this is useful if your screen have live content that need internet connection all the time.
- **Background Type** - You can select a background for a consistent backdrop in situations where content may not fill the screen or if the content is not Scaled. You can choose from the following:
  - Default
  - Color
  - Image
  - Transparent
- **Advanced Playlist Settings**
  - [**Sync Play**](https://support.optisigns.com/hc/en-us/articles/4412065189267) - Synchronize playback timing across your screens.
  - **Preload Assets in Playlist** - If checked, this will preload the assets in your playlist in the background. This is good for user experience, but if you have animation or dynamic content on your web page, you may want to disable this.
  - [**Content Tag Rule**](https://support.optisigns.com/hc/en-us/articles/20879903340947-How-to-Use-Content-Tags-in-The-Playlist) **-** Enables you to mix and match content for different screens within the same playlist, greatly simplifying screen management.
  - **Preload Playlist** - Preloads a specific playlist in the background, allowing for instant playback when that playlist is selected to display on the screen.
- **Mute** - Check to mute your screen

---

## More

Clicking the **"More"** option under Advanced leads you to the options below.

|  |  |
| --- | --- |
| **OptiSigns 1.0** | **Updated** |
|  |  |

- [**Lock Down**](https://support.optisigns.com/hc/en-us/articles/4416681544211) - Hide OptiSigns controls and menu to prevent viewers from making changes to the app. If running Kiosk, viewers still can interact with Kiosk, but cannot use the menu or close app.
- [**Playback Control**](https://support.optisigns.com/hc/en-us/articles/4416704273811)- Enable the viewer to navigate forward, backward, and pause the playlist.
- [**Proof of Play**](https://support.optisigns.com/hc/en-us/articles/360058936513) - Send playback data to enable proof of play reporting.
- **Brightness** - Controls the brightness of your screen.
- **Volume** - Controls the volume of your screen.
- [**Schedule Power, Volume, Brightness, mute**](https://support.optisigns.com/hc/en-us/articles/4416681142675) - Schedule Device, TV power on/off, Volume, Brightness or when device should download new contents. This will largely depend on your devices and TV/Monitor selection.
- **Polling Interval**
  - **Polling Interval -** Controls how frequently the system checks for content updates, ensuring that the displayed content is always current and reflects any changes made to the source.
  - **Heartbeat Interval -** Controls how frequently the system checks in to OptiSigns server. This determines whether your device will appear Online or Offline in the OptiSigns portal.
- [**Remote Control**](https://support.optisigns.com/hc/en-us/articles/360055486554-Advanced-How-to-Remote-Troubleshooting-Control-Your-Device) - Remotely view what's on your screen or troubleshoot any issues.
- [**AI Add-On**](https://support.optisigns.com/hc/en-us/articles/360058259834) - Enable OptiSigns AI camera to detect and collect data around passing foot traffic, or responsively display different content depending on the demographic of the viewers in front of your screen.
- [**Sensor Add-On**](https://support.optisigns.com/hc/en-us/articles/13097501958291) - Activate OptiSigns IoT Sensor to measure the impact of your signs.
- [**External COM**](https://support.optisigns.com/hc/en-us/articles/17342932920211-Event-logging-and-analytics-for-External-Communication-RS-232)- Enables communication with External Devices.

---

## Device Additional Attributes

To open the Device Additional Attributes window, click the **Wrench** icon at the bottom right of the window.

|  |  |
| --- | --- |
| **OptiSigns 1.0** | **Updated** |
|  |  |

This feature ties in to Power BI app filters and API gateways, allowing substitution of your merchantID and the API or filter's value. Click [here](https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-consume-API-and-publish-the-API-data-on-the-screen) to learn more about how to use this much-requested feature.

---

## Device Info

To view the **Device Info** tab, click the small **'i'** at the bottom right of your screen.

|  |  |
| --- | --- |
| **OptiSigns 1.0** | **Updated** |
| firefox_7oQsrmiEmn.png |  |

This will open the **Device Info** window.

|  |  |
| --- | --- |
| **OptiSigns 1.0** | **Updated** |
| firefox_AwP9mWDRsw.png |  |

This window provides information about your system in the form of Python lists and dictionaries, which you can utilize for your own purposes.

---

## OptiSigns Player Specific Settings

|  |  |
| --- | --- |
| **OptiSigns 1.0** | **Updated** |
|  |  |

|  |
| --- |
| **Note:** If you are not using an OptiSigns Player (OptiStick, Pro, or ProMax) these features will not be shown in your options. |

[**Operational Schedule**](https://support.optisigns.com/hc/en-us/articles/28598173096723)- Schedule TV power on/off times and control volume and brightness.

[**Background Music**](https://support.optisigns.com/hc/en-us/articles/360050726634-Playing-background-music-radio-with-OptiSigns) - Setup your screen to play Background Music through the OptiSound add-on.

[**Remote Commands**](https://support.optisigns.com/hc/en-us/articles/30010338528659) **-** Executes remote commands like rebooting, taking screenshots, adding Wi-Fi, and more.

[**Video Wall**](https://support.optisigns.com/hc/en-us/articles/33382537925267-Making-a-Video-Wall-with-OptiSigns-Video-Wall-App)- Only available on OptiSigns Pro or ProMax player under the Advanced section, the Video Wall option enables the Video Wall app for creating multi-screen video walls.

---

## More Remote Command Options

|  |  |
| --- | --- |
| **OptiSigns 1.0** | **Updated** |
|  |  |

Explore more about executing remote commands on Android by [clicking here](https://support.optisigns.com/hc/en-us/articles/30010338528659), and for Windows, [click here.](https://support.optisigns.com/hc/en-us/articles/4408658251027)

---

## Final Options

At the bottom of the window, you will see several options, including **Help, Preview, Close, Schedule, Save,** and an arrow leading to **Identify Screen**.

|  |  |
| --- | --- |
| **OptiSigns 1.0** | **Updated** |
| firefox_K67dpVQIPS.png |  |

- **Help -** This leads you here, to this article. Hello!
- **Preview** - Lets you check out the settings you've selected on the chosen screen, without saving it. See our article on [**How to Preview a Screen**](https://support.optisigns.com/hc/en-us/articles/360035739414-How-to-Preview-a-Screen) for more information about this feature.
- **Close -** Leaves the Edit Screen window without saving your work.
- **Schedule** - This lets you see the schedule you have the screen on quickly. *Only clickable when a schedule is selected above.*
- **Identify Screen** - Displays information on the screen for 30 seconds, displaying the Device name and other specific data for identification or troubleshooting purposes.

## **That's It!**

Click **Save** when you are completed; otherwise, you will lose all changes.
