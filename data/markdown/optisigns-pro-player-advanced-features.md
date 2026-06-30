# OptiSigns Pro Player Advanced Features

Article URL: https://support.optisigns.com/hc/en-us/articles/35577511423635-OptiSigns-Pro-Player-Advanced-Features
Article ID: 35577511423635
Last Updated: 2026-03-30T17:22:38Z

### In this article, we go over the Advanced Features of the new Gen 3 OptiSigns Pro Player.

|  |
| --- |
| **IMPORTANT** |
| This article applies strictly to the *OptiSigns Gen 3 Pro Player or ProMax Player* on version **5.6.33** or later. |

- [OTA Updates](#OTA)
  - [Forcing an OTA Update](#ForceOTA)
- [The "About" Option](#About)
  - [Device Log](#Log)
  - [Advanced Settings](#AdvancedSettings)
- [How to Bring Up the System Terminal](#name)
- [How to Use SSH to Remote into Device](#ssh)
- [How to Perform a Factory Reset](#FactoryReset)

The [**OptiSigns Pro Digital Signage Player**](https://shop.optisigns.com/collections/shop-page/products/optisigns-digital-signage-player) or [**OptiSigns ProMax Player**](https://shop.optisigns.com/products/optisigns-promax-signage-player) are mighty devices, able to leverage the full power of OptiSigns [**digital signage software**](https://www.optisigns.com/) to display your content on any screen with unparalleled visual clarity and customizability.

But there’s even more to the [**Pro Player than its standard features**](https://support.optisigns.com/hc/en-us/articles/32272215514131-Optisigns-Pro-Digital-Signage-Player), and here we’ll explain the device’s Advanced features.

|  |
| --- |
| **NOTE** |
| If you do not see all the options listed below, we recommend performing an **OTA Update** to ensure you have the latest version of the Pro Player software. This is covered later in the article. |

---

## OTA Updates

The OptiSigns Pro Player makes use of OTA updates to receive security patches, platform enhancements, additional feature support, and more.

![](https://support.optisigns.com/hc/article_attachments/35577511371795)

By default, the Pro Player can be set to check for updates once per week at a time you specify from the device itself. If an update is available, it will be automatically downloaded as long as the player has an internet connection. It’s also possible to force an OTA update if necessary.

### Setting the OTA Update Time

To change the OTA Update time from the portal or across multiple devices, read on.

|  |
| --- |
| **NOTE** |
| This has to be done on the original 1.0 OptiSigns portal. |

First, find your screen. Navigate to **Advanced** → **Down Arrow** → **OTA Update.**

![](https://support.optisigns.com/hc/article_attachments/49004214269459)

The below window will appear:

![](https://support.optisigns.com/hc/article_attachments/49004214271123)

Here, choose the day of the week and time of day for your OTA update. You can choose from various builds as well under the **Channel** option:

![](https://support.optisigns.com/hc/article_attachments/49004252034451)

You can also **Reset after OTA**, which will automatically restart the Pro or ProMax player after the OTA Update is complete.

Finally, you'll be able to check for an update and automatically apply it here, or receive instructions on how to manually reimage your Pro/ProMax Player.

### How to Force an OTA Update

If your device misses its update window, either due to being powered off, or lacking reliable network connection, it is possible to check for an OTA update to the OptiSigns Pro Player and apply it.

In order to do this, you’ll need access to the OptiSigns Portal. From the **Screens tab**, click the **3 Dots** **→ Execute Remote Commands**.

![](https://support.optisigns.com/hc/article_attachments/35577511373587)

You’ll be taken to the below screen:

![](https://support.optisigns.com/hc/article_attachments/35577555668755)

Target the screen you’ve paired with your OptiSigns Pro Player, then enter the **forceOTA** command in the highlighted field. After a few seconds, you should see the following:

![](https://support.optisigns.com/hc/article_attachments/35577511382803)

This means the OptiSigns Pro Player has received the command and executed it. It should now be receiving its update.

|  |
| --- |
| **NOTE:** In order for your OptiSigns Pro Player to receive commands, it will need to be connected to the Internet. |

---

## The ‘About’ Option

The **About** option provides data on your Pro Player, in addition to different options.

![](https://support.optisigns.com/hc/article_attachments/35577555680659)

This lets you know everything from the name attached to your screen, to whether the Player is connected to the internet, to the storage used.

It also provides further options.

- **Reboot** does what it says. It will reboot your device.
- **Device Log** allows you to export your device log. More detail is provided below.
- **WiFi Setup** lets you tweak the WiFi settings of the device. This is done the same way as on the device’s initial setup.
- **Advanced Settings** provide additional network options. More detail is provided below.

### Device Log

The device log option allows you to export the device log into an external device. In order to use this option, you’ll need a USB drive or MicroSD card plugged into your Pro Player. When you hit the **Device Log** option with an external drive plugged in, you’ll see the following message:

![](https://support.optisigns.com/hc/article_attachments/35577555683603)

You can then take your external device and do whatever you like with the device log.

### Advanced Settings

![](https://support.optisigns.com/hc/article_attachments/44646006336915)

On the **Advanced Settings** screen, you can perform various functions such as enabling/disabling Network Proxy, NTP, the On-screen Keyboard, SSH, configuring a Static IP for either WLAN or Ethernet, and enabling 802.1x Ethernet. Selecting any of these options will enable further options in the window:

![](https://support.optisigns.com/hc/article_attachments/44646006339731)

- **Certificate File** **-** Allows you to [install a root certificate](https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens) for displaying an internal website. The certificate will need to be present locally on the device in order for it to be installed.
- **NTP Server -** Input server information for your Network Time Protocol (NTP). This can be used to ensure the OptiSigns Pro Player has its computer clock time with other time sources in your network.
- **WiFi SSH IP** - IP address associated with your SSH. Only appears when SSH is enabled.
- **Network Proxy -** Server information for any network proxy. This is a system or router which serves as a middleman between our Pro Player and the internet and can be used to enhance security, privacy, or efficiency.
- **KeyBoard Layout -** Choose between various international keyboard layouts. Default is US.
- **Static IP Information -** An IP address that remains the same over time. We allow two types of Static IP: WLAN or ETH. These can improve network performance. This screenshot shows WLAN; if Static ETH IP is chosen, these will be ETH IP Address, Default Gateway, Subnet Mask, and DNS Server.
  - **IP Address -**Set the Static IP address.
  - **Default Gateway**- Set the Default Gateway for the Static IP address. This is the IP address of your router.
  - **Subnet Mask**- Set the Subnet Mask for the Static IP. Usually, this number is 255.255.255.0 or some variant of this.
  - **DNS Server**- Lets you set up your DNS server for the Static IP address.

![](https://support.optisigns.com/hc/article_attachments/44646006341779)

- **802.1x UserName**- Username of the 802.1x Enterprise Ethernet network
- **802.1x Password**- Password of the 802.1x Enterprise Ethernet network
- **802.1x Certificate**- Allows you to install a certificate for accessing an 802.1x Enterprise network. The certificate will need to be present locally on the device in order to be installed.

---

## How to Bring Up the System Terminal

The OptiSigns Pro Player has a console you can use to input commands directly. This can be accessed through the OptiSigns portal.

### Enabling Remote Commands Feature on Account

Remote Command Execution is disabled by default. To use it, it will need to be turned on. To do this, navigate to [the Preferences section](https://app.optisigns.com/app/s/preference-settings) in the OptiSigns portal.

|  |
| --- |
| For security reasons, **only the account owner** can enable or disable Remote Command Execution. |

[![](https://support.optisigns.com/hc/article_attachments/45161221791635)](https://support.optisigns.com/hc/article_attachments/45161221791635)

### Executing Remote Commands

Now we can actually send Remote Commands from the OptiSigns portal to your Pro or ProMax player. From the **Screens tab**, click the **3 Dots** **→ Execute Remote Commands**.

![](https://support.optisigns.com/hc/article_attachments/35577555693075)

You’ll be taken to the below screen:

![](https://support.optisigns.com/hc/article_attachments/35577555668755)

Target the screen you’ve paired with your OptiSigns Pro Player, then enter the **showTerminal** command in the highlighted field. After a few seconds, you should see the following:

![](https://support.optisigns.com/hc/article_attachments/35577511404819)

This means the OptiSigns Pro Player has received the command and executed it. Your console terminal should now be visible on your screen and can be interacted with.

---

## How to Use SSH to Remote Into Device

Pro Players allow remoting into devices using SSH. Here's how to set that up.

First, enable **SSH**in your Advanced Settings.

![ssh advanced settings](https://support.optisigns.com/hc/article_attachments/40985616289939)

This will provide you with the SSH IP and Port number. By default, the port is **3000**, but it can be changed to whatever you like.

![ssh ip and port](https://support.optisigns.com/hc/article_attachments/40985596548243)

Now that SSH is enabled and you have the IP and Port, you can use a computer terminal to remote into the device.

Type the following command:

```auto
SSH optisigns@<ip-address-here> -p <port-number-here>
```

When it asks for a password, type **optisigns**. This should connect you to the device via SSH.

To change the default password (which we ***highly recommend***), type:

```auto
passwd
```

This will ask you to type the current password, then new, then to type in the new password again.

![](https://support.optisigns.com/hc/article_attachments/41021980486931)

|  |
| --- |
| **NOTE** |
| Restarting the OptiSigns Pro Player will cause SSH to automatically disable for security purposes. |

That's it! You should be able to use the SSH function now.

---

## How to Perform a Factory Reset

Sometimes, it might be necessary to perform a factory reset on your OptiSigns Pro Player.

To do this, attach a keyboard to the Player. Then, **Reboot** it. As it restarts, rapidly tap the **↑ arrow**. It will boot into this screen:

![](https://support.optisigns.com/hc/article_attachments/35577555703187)

Here, you have several additional options. Hit **Factory Reset**. You’ll receive this prompt:

![](https://support.optisigns.com/hc/article_attachments/35577555704723)

You’ll need to enter your **admin password.**

|  |
| --- |
| **NOTE** |
| As you enter the password, no symbols will display. Rest assured, however, that the device is registering your keystrokes. |

Once entered, you’ll see a screen like this:

![](https://support.optisigns.com/hc/article_attachments/35577555707923)

Afterwards, your factory defaults will be restored.

### **That’s all!**

OptiSigns is a leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
