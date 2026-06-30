# How to Perform Mass Provisioning with OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/4416542923667-How-to-Perform-Mass-Provisioning-with-OptiSigns
Article ID: 4416542923667
Last Updated: 2026-04-16T14:17:14Z

### In this article, we explain how to Mass Provision your devices for easy digital signage setup across numerous devices.

- [How to Set Up Mass Provisioning in the OptiSigns Portal](#Setup)
  - [Prerequisites](#Prerequisites)
  - [Step 1: Create a Provisioning Template](#Step1)
  - [Step 2: (Optional) Generate Device List](#Step2)
- [Deployment by Device](#Deployment)
  - [OptiSigns Digital Signage Players & Windows/Linux Devices](#OptiSigns)
  - [Raspberry Pi Devices](#Raspberry)
  - [Apple TV and ChromeOS](#AppleTV)

|  |
| --- |
| **NOTE:** Mass Provisioning is only available to **Enterprise** plan subscribers. |

Customers on the Enterprise Plan can now perform mass provisioning with OptiSigns. It is supported on OptiSigns Android Player, Android OS devices, Windows, Linux, Raspberry Pi, ChromeOS, or AppleTV.

If running a large deployment of digital signs, mass provisioning will save a lot of time and effort.

For example, when you use our RPI image or have MDM software to display the OptiSigns player on a device, the mass provisioning feature lets you set up the device and get it connected to your account without having to set up each device individually.

---

## How to Set Up Mass Provisioning in the OptiSigns Portal

The process of performing mass provisioning is simple and straightforward.

1. Create a provisioning template in your account.
2. (Optional) Generate a device list. Only needed if you wish to
3. Deploy and run.

### Prerequisites:

- The device needs to support using a USB drive or SD card. Or there is a way you can push the configuration file to a specific location in the OS.
- The user using the OS has the privilege to run the installation and access the USB drive or SD card.

First time using OptiSigns? [Learn how to set up your digital signs](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv) to get a better understanding before deployment.

### Step 1: Create provisioning template

To create a provisioning template, access it from the admin menu or use this [provisioning templates link](https://app.optisigns.com/app/s/provisioning-templates).

![provisioning templates dropdown in optisigns app](https://support.optisigns.com/hc/article_attachments/34385117085715)

|  |
| --- |
| **NOTE:** This option will not be visible without an **Enterprise** level plan. |

Create a new provisioning template by clicking the **Create templates** button.

![create templates button with arrow pointing at it in optisigns app](https://support.optisigns.com/hc/article_attachments/34385123847827)

 If you want to auto-step up WiFi at provisioning, you will need to create a stored WiFi first. These steps are covered later.

For now, set up the template in this popup:

![provisioning template options in optisigns](https://support.optisigns.com/hc/article_attachments/4416555482899)

- Template Name: Name of your template, this is for you to distinguish it when you have multiple provisioning templates.
- Device Name Prefix: This is used to generate the device name during provisioning.
- Device Name Suffix: This is used to generate the device name during provisioning, the default setting will add timestamps as a suffix.
- Folder: The folder you want to have the provisioned devices to be created.
- WiFi: Select from the stored WiFi, which needs to be created first. Only required if you want to set up WIFI during provisioning.
- Time Zone: Specify the time zone of the device.
- Tags: Specify the tags you want to associate with the devices.
- Initial Default Content Type: Used to set the initial content on the device after provisioning.
- Orientation: Set the orientation, landscape is the default.
- Sync Play: Used to set the turn on/off of the sync play feature. For more details on the Sync Play feature, please click [here](https://support.optisigns.com/hc/en-us/articles/4412065189267-Synchronized-playback-Sync-Play-feature).
- Location: Set the location of the device.

Once the template is created, it will be available under the list of provisioning templates. Download the config file for use during deployment. The configuration file's name is "provisioning-template-<Your Template Name>.cfg"

![provisioning templates screen with arrow pointing at file name button](https://support.optisigns.com/hc/article_attachments/4416548298259)

If you want to set up WiFi at the same time as provisioning, click the **Manage Stored WiFi** button.

In the popup, click "Add New WiFi", then enter the WiFi SSID and password. The WiFi will be stored and available to use in the provisioning template.

![manage stored wifi screen with arrow pointing at add new wifi button](https://support.optisigns.com/hc/article_attachments/4416570772627)

### Step 2: Generate Device List (Optional)

If you want the device name preassigned for each device, follow this step. Otherwise, proceed to the Deployment section below.

To preassign the device name, choose **Preconfigure Devices** feature on the **Screens**tab to create a device list with a pairing code:

![screens tab with arrows showing how to get to preconfigure devices option](https://support.optisigns.com/hc/article_attachments/4416556453779)

In the popup, specify how many screens you want to preconfigure.

![preconfigure devices options screen 1](https://support.optisigns.com/hc/article_attachments/4416556459923)

Enter a prefix  to give to your device and assign some initial content to display onscreen. The device name will be generated based on the prefix with a sequence number added. This name can be changed later before deployment.

![preconfigure devices options screen 2](https://support.optisigns.com/hc/article_attachments/4416556506003)

Once done, the page will list all the devices preconfigured with the pairing code. Click **Done**.  This generates a CSV file named "preconfigure-devices.csv". Download it to your computer.

![preconfigure devices screen with two screens added](https://support.optisigns.com/hc/article_attachments/4416556695571)

Open the CSV file. It will contain the list of the preconfigured devices and their corresponding pairing code. To change the device name, simply update the CSV file. Then the file can be used in deployment if you want to have your screens using the exact pre-assigned name.

![preconfigure devices downloaded csv file](https://support.optisigns.com/hc/article_attachments/4416571675923)

---

## Deployment

Once you have the provisioning template config file ready, you can proceed to the deployment. If you would like to pre-assign the exact name on the screen, you will need to get the preconfigured device list from step 2 as well.

### OptiSigns Digital Signage Players and Windows/Linux/Android Devices

For mass provisioning deployment on the [OptiSigns Android Player](https://shop.optisigns.com/products/optisigns-android-stick-player-2), the [OptiSigns Pro Player](https://shop.optisigns.com/products/optisigns-digital-signage-player), or any Windows, Linux, or Android device, get a MicroSD card or USB drive and create a folder named "autoconfig" under the root directory. Place one or both of the CSV and CFG files into this folder.

Next, attach the MicroSD card/USB drive to your player. Launch the player, and the player will automatically detect the config file and start the provisioning process. You will receive this message once the provisioning is complete (with your local timezone configured):

![mass provisioning success screen](https://support.optisigns.com/hc/article_attachments/4416680470163)

### Raspberry Pi Devices

Raspberry Pi devices have two options for mass deployment: the USB method detailed above, or via SSH.

For more on the SSH method, see [how to enable SSH for your Raspberry Pi](https://support.optisigns.com/hc/en-us/articles/1500008008981-How-to-enable-SSH-for-your-Raspberry-Pi) and [how to mass deploy OptiSigns on Raspberry Pi devices](https://support.optisigns.com/hc/en-us/articles/360063098753-How-to-mass-deploy-OptiSigns-on-Raspberry-Pi-devices).

### Apple TV and ChromeOS

Deployment on an Apple TV or a ChromeOS device has to be done through their respective platforms.

For more, see our articles on [configuring OptiSigns mass deployment on Apple devices](https://support.optisigns.com/hc/en-us/articles/31695220475283-Configuring-Mass-Deployment-with-Jamf-Pro-MDM-on-Apple-Devices) and [how to use OptiSigns Auto Provisioning Template on ChromeOS.](https://support.optisigns.com/hc/en-us/articles/17353256033811-How-to-use-OptiSigns-Auto-Provisioning-Template-on-ChromeOS)

### **That's all!**

Now you know how to perform mass provisioning with OptiSigns.

If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
