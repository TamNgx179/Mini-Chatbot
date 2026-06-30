# How to Connect to 802.1x Enterprise WiFi on Raspberry Pi

Article URL: https://support.optisigns.com/hc/en-us/articles/4411743936147-How-to-Connect-to-802-1x-Enterprise-WiFi-on-Raspberry-Pi
Article ID: 4411743936147
Last Updated: 2025-09-04T15:24:46Z

When you are trying to connect to 802.1x WiFi with WPA enterprise on Raspberry Pi,  you will see the WiFi access point is greyed out on Raspberry Pi, like below. It is because Raspberry Pi is using the simple network service on the GUI, which doesn't support enterprise WiFi.  However, Raspberry Pi is supporting 802.1x enterprise WiFi. And the simplest way to setup the connection to 802.1x enterprise WiFi on Raspberry Pi is to use standard Linux network manager to replace the simple network service. In this tutorial, we will walk through how to set it up.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4411750345875)

**Open the terminal window on Raspberry Pi, and run below commands to get the standard Linux network manager installed.**

sudo apt install network-manager network-manager-gnome  
sudo systemctl disable --now dhcpcd  
sudo systemctl enable --now network-manager

sudo reboot

**Explanation:**

1st line is to install the Linux network manager

2nd line is to disable the DHCP, because DHCP will not work with the network manager

3rd line is to enable the network manager service

Last line is to reboot the device.

**After rebooting the device, you will be able to see a new network icon, click on the icon, you will not be able to connect to the 802.1x enterprise WiFi.**

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4411743714067)

**Then fill in the information as you normally do with 802.1x enterprise WiFi connection, and you will now be able to connect to the network.**

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/4411743744787)

**That's it! You're ready to go.**

**Note:** To download and install the network manager, you will need internet connection first. Please consider have it connected to a wired network or another normal WiFi network first to get it setup.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
