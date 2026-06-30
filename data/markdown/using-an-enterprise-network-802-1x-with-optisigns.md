# Using an Enterprise Network (802.1x) with OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/44890229616403-Using-an-Enterprise-Network-802-1x-with-OptiSigns
Article ID: 44890229616403
Last Updated: 2026-05-20T18:11:11Z

### In this article, we'll cover how to get OptiSigns working on an Enterprise-level security network, either over WiFi or Ethernet.

- [Supported Devices](#SupportedDevices)
- [Setting Up 802.1x Enterprise WiFi on a Pro or ProMax Player](#SettingUp)
  - [On Initial Setup](#OnInitialSetup)
  - [Changing From Another Network Source](#Changingfrom)
- [Setting Up a Wired Ethernet 802.1x Enterprise Network](#WiredEthernet)

If your organization uses an 802.1x Enterprise Network, many devices will not be compatible with OptiSigns. Here, we'll let you know which ones are, and how to connect to it on OptiSigns devices.

---

## Supported Devices

- OptiSigns [Pro Player](https://www.optisigns.com/product/hardware/pro-digital-signage-player) or [ProMax Player](https://www.optisigns.com/product/hardware/promax-digital-signage-player)
- Windows
- Linux

Note that this does not include the OptiStick, nor other devices such as Raspberry Pi. These do not support Enterprise networks at this time.

The scope of this article will limit itself to getting OptiSigns to work on OptiSigns devices. For Windows and Linux, connect the device to your network as normal and be sure OptiSigns has been [**whitelisted through your organization's firewall**](https://support.optisigns.com/hc/en-us/articles/360047275934-Whitelist-OptiSigns-IP-addresses-ports)**.**

|  |
| --- |
| **IMPORTANT** |
| You'll need to know whether or not you're using **PEAP** or **EAP-TTLS** for your network security protocol. This will determine what sort of certificate to set up on the OptiSigns device. |

---

## Setting Up 802.1x Enterprise WiFi on a Pro or ProMax Player

Setting up Enterprise WiFi on a Pro or ProMax Player can be done during initial setup, or it can be switched to from a different WiFi source.

### On Initial Setup

You can set your Enterprise WiFi network as See our article on [Setting Up WiFi on the Pro or ProMax Player](https://support.optisigns.com/hc/en-us/articles/32272215514131-OptiSigns-Pro-Digital-Signage-Player#Configuring) for more information on that.

You'll be on the **Device Wi-Fi Settings** menu. Under **Security**, select **WPA2-Enterprise**.

![device wifi settings wpa2-enterprise](https://support.optisigns.com/hc/article_attachments/44890229610259)

Several more options will open up.

![wpa2-enterprise login options](https://support.optisigns.com/hc/article_attachments/44890235677203)

You'll need to enter a **Username** and **Password**, and upload a certificate depending on the needs of your security network. Simply locate this certificate, place it on a USB or MicroSD card, attach it to the Pro Player, and select it here. The certificate will automatically be downloaded to the appropriate location.

This should connect your Pro or ProMax player to your Enterprise WiFi network.

### Changing from Another Network Source

If you've already performed your initial setup, you can still change to an Enterprise WiFi network.

To do this, open up the **Side Menu**, then navigate to **About:**

![pro player side menu about option](https://support.optisigns.com/hc/article_attachments/44890229611283)

On the **About** menu, hit **WiFi Setup**.

![about menu wifi settings option](https://support.optisigns.com/hc/article_attachments/44890235678867)

From here, it's the same process as above. You'll be on the **Device Wi-Fi Settings** menu. Under **Security**, select **WPA2-Enterprise**.

![wpa2-enterprise login options img2](https://support.optisigns.com/hc/article_attachments/44890229610259)

Several more options will open up.

![device wifi settings wpa2-enterprise img2](https://support.optisigns.com/hc/article_attachments/44890235677203)

You'll need to enter a **Username** and **Password**, and upload a certificate depending on the needs of your security network. Simply locate this certificate, place it on a USB or MicroSD card, attach it to the Pro Player, and select it here. The certificate will automatically be downloaded to the appropriate location.

This should connect your Pro or ProMax player to your Enterprise WiFi network.

---

## Setting Up a Wired Ethernet 802.1x Enterprise Network

To set up an 802.1x Enterprise Ethernet connection on an OptiSigns Pro or ProMax player, you'll need to attach an Ethernet cable to your player first.

Then, open the **Side Menu**, then go to **About**.

![side menu about](https://support.optisigns.com/hc/article_attachments/44890229611283)

On the **About** menu, go to **Advanced Settings:**

![pro player side menu advanced settings](https://support.optisigns.com/hc/article_attachments/44890229612307)

Next, click the **802.1x Ethernet** switch to enable it. Several additional options will become available:

![802.1x ethernet login options](https://support.optisigns.com/hc/article_attachments/44890235683987)

You'll need to enter a **Username** and **Password**, and upload a certificate depending on the needs of your security network. Simply locate this certificate, place it on a USB or MicroSD card, attach it to the Pro Player, and select it here. The certificate will automatically be downloaded to the appropriate location.

### That's all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
