# LG WebOS Signage (Commercial Grade)

Article URL: https://support.optisigns.com/hc/en-us/articles/4414496579475-LG-WebOS-Signage-Commercial-Grade
Article ID: 4414496579475
Last Updated: 2025-09-04T18:03:17Z

LG is one of the world leader in manufacturing commercial grade TV screens that are used in hotels, restaurants, retails and other environment.

OptiSigns does support LG WebOS Signage, all apps, features are supported, include offline playback and auto update of OptiSigns app on LG WebOS Signage devices.

Please note that this article is for installing OptiSigns on LG WebOS Signage devices only, the screens should be marked as "LG Digital Signage". For the normal consumer TV with LG WebOS, please use the [normal webplayer](https://www.optisigns.com/post/how-to-use-optisigns-with-browser).

#### **The installation process is easy, you have 2 options:**

1) Installation from a USB drive: this is the easiest as you don't need to use remote to type in a URL, and it's useful if you have a lot of TVs to set up, you can use the same USB to set them up quickly.  
2) Installation from server: if you don't have or don't want to use USB drive, just need to punch in the URL: <https://links.optisigns.com/lg> in your SI server TV settings (see detail below)

#### **Before you begin:**

- Ensure your TV is factory reset with basic settings

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4414497081107)

- Connect to internet (WiFi or Ethernet)

- Set up date, time this is to ensure schedule will play correctly with your time zone

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4414489377299)

#### **1) Installation from a USB Drive:**

Download the this file [com.lg.app.signage.ipk](https://links.optisigns.com/lg) to your computer.

Format your USB Drive to FAT32 if you not already have it.  
Create a folder named **‘application’** in the root of your USB drive   
Copy the .ipk file into this folder   
![mceclip3.png](https://support.optisigns.com/hc/article_attachments/4414485674899)  
Insert the USB drive to the LG TV's USB port.

On the TV, enter the settings menu (press the config wheel icon on the remote controller)  
Navigate to: EZ Setting -> SI Server Setting

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/4414497608211)

Select SI Server Setting

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/4414490220051)

In this page, set the ‘Application Launch Mode’ to ‘Local’   
Set the ‘Application Type’ to ‘IPK’  
Then finally click ‘Local Application Upgrade’ -> ‘USB’

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/4414497878419)   
Confirm your intent to install the application

![mceclip8.png](https://support.optisigns.com/hc/article_attachments/4414498104851)

If your USB thumbdrive prepared correctly, you will see message confirm that the upgrade is completed

![mceclip9.png](https://support.optisigns.com/hc/article_attachments/4414490483859)  
After that power off, and power on the TV.

When the TV come back up, you will see it's updating:

![mceclip10.png](https://support.optisigns.com/hc/article_attachments/4414498126355)

After update completed, it will show this message:

![mceclip11.png](https://support.optisigns.com/hc/article_attachments/4414490508179)

And OptiSigns app will automatically be started, you will see the pairing code, you can start pairing it on app.optisigns.com and assign content to it there.  
The installation process is completed, you now can remove the USB drive.  
From now on, OptiSigns app will be automatically started with the TV, and it will also automatically check for updates itself.

![mceclip12.png](https://support.optisigns.com/hc/article_attachments/4414487042195)

#### **2) Installation from server:**

On the TV, enter the settings menu (press the config wheel icon on the remote controller)  
Navigate to: EZ Setting -> SI Server Setting

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/4414497608211)

Select SI Server Setting

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/4414490220051)

Set ‘Fully Qualified Domain Name’ to ‘On’   
Then enter ‘https://links.optisigns.com/lg’ into the input field  
Set the ‘Application Launch Mode’ to ‘Local’   
Set the ‘Application Type’ to ‘IPK’   
Finally click ‘Local Application Upgrade’ -> ‘REMOTE’

![mceclip13.png](https://support.optisigns.com/hc/article_attachments/4414487226771)

Confirm your intent to install the application

![mceclip14.png](https://support.optisigns.com/hc/article_attachments/4414487260307)   
If the FQDN URL is misspelled you will see an error message and have to modify the URL.  
If the FQDN URL is correct, you will see this message confirm upgrade completed.

![mceclip15.png](https://support.optisigns.com/hc/article_attachments/4414487276947)

After that power off, and power on the TV.

When the TV come back up, you will see it's updating:

![mceclip10.png](https://support.optisigns.com/hc/article_attachments/4414498126355)

After update completed, it will show this message:

![mceclip11.png](https://support.optisigns.com/hc/article_attachments/4414490508179)

And OptiSigns app will automatically be started, you will see the pairing code, you can start pairing it on app.optisigns.com and assign content to it there.  
From now on, OptiSigns app will be automatically started with the TV, and it will also automatically check for updates itself.

![mceclip12.png](https://support.optisigns.com/hc/article_attachments/4414487042195)

#### **Batch installation from the server URL with settings from a USB drive:**

Instead of typing in the URL and change settings for reach device, you can create USB drive to re-use it on many screens.  
1) Create a file named ‘scap\_installation.json’ on your computer with this content:

```
{  
“serverIp” : “0.0.0.0”,  
“serverPort” : 0,  
“secureConnection” : false,  
“fqdnMode” : true,  
“fqdnAddr” : “https://links.optisigns.com/lg”,  
“appLaunchMode” : “local”,  
“appType” : “ipk”  
}
```

2) Copy this file into the root of the USB drive   
3) Insert the USB drive into the device and start/reboot it  
4) Once the installation finish, restart the TV and OptiSigns app will AutoStart.

**To check which LG WebOS Signage firmware version is installed on the device:**   
Enter the settings menu (the config wheel icon on the remote)   
Navigate to ‘General’ -> ‘System Information’

#### **To upgrade the** **LG WebOS Signage firmware** **on the device:**

If you are running WebOs 4.1 or older, you may need to upgrade your Firmware to for the device to be able to play OptiSigns apps like Weather, Social Medias, etc.  
Get the latest firmware file (.epk) from [LG website](https://partner.lge.com/global/portal/main/main/fowardMenuUrl.lge?_MenuId=210099&_MenuLevel=3&_MenuParentId=210021&_SuperCategoryCode=&_searchKeyWord=&pageName=&gdprChk=&pwConfirmYn=&popupYn=&menuType=C&_SuperCategoryCode=&needReload=&siteCountryCode=global&corporationCode=LGEHQ&obuCode=) (please see [this article on LG's website](https://www.lg.com/us/support/help-library/lg-tv-how-to-manually-update-software--20154165668198), contact us, or LG if you need help)  
Create a folder names ‘LG\_MONITOR’ in the root of your USB drive   
Copy the new firmware .epk file into it   
Insert the USB drive into the TV's USB port  
The update menu will automatically appear   
Click on ‘Update’ and wait till the process finishes

#### **Copy config from 1 device to another:**

You can create USB drive config to replicate settings from 1 device to another (include WiFi, OptiSigns app, time zone, etc.) this will save you time if you have many devices to set up.

Enter the settings menu (the config wheel icon on the remote)  
Insert a USB drive into your device   
Navigate to ‘Ez Setting’ -> ‘Setting Data Cloning’   
On the first device push ‘Export Setting Data’   
On the other devices push ‘Import Setting Data’

If you have questions or need additional help, please contact us at [support@optisigns.com.](mailto:support@optisigns.com)
