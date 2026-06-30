# How to get the MAC Address on your media player

Article URL: https://support.optisigns.com/hc/en-us/articles/8099928867475-How-to-get-the-MAC-Address-on-your-media-player
Article ID: 8099928867475
Last Updated: 2025-08-29T20:29:34Z

If your IT team is looking for the MAC address on your media player, you can follow this article to get the MAC Address on your devices.

In this article, we will guide you on how to get the MAC Address on these devices.

- OptiSigns Android Stick
- Fire Stick
- Raspberry Pi
- Windows

### 1) How to get the MAC Address on the OptiSigns Android Stick

1. Go to the Android Home Page > Settings

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/8099392313107)

2. Click "Network & Internet"

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/8099440965779)

3. Select "your wifi SSID name"

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/8099446318099)

4. You will see your device's MAC Address.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/8099481961235)

### 2) How to get the MAC Address on the Fire Stick

1. Go to the Fire Stick Home Page > Settings > My Fire TV

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/8099583974803)

2. Click "About"

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/8099585346451)

3. Then go to "Network", you will see the MAC Address

![mceclip8.png](https://support.optisigns.com/hc/article_attachments/8099602869139)

### 3) How to get the MAC Address on the Raspberry Pi

1. Open the "**terminal**"

![mceclip12.png](https://support.optisigns.com/hc/article_attachments/8099797282067)

2. Type the

```
ifconfig
```

3. The result will be like this, check section eth0 if you are using wired connection. Check section wlan0 if you are using WiFi connection.

![mceclip11.png](https://support.optisigns.com/hc/article_attachments/8099782797587)

The MAC address is visible after the **“ether”** keyword.

### 4) How to get the MAC Address on the Windows

1. Enter **cmd**in the search box at the bottom left-hand corner of your screen. You will see the "Command Prompt" and click it

![mceclip15.png](https://support.optisigns.com/hc/article_attachments/8099829447827)

It will show like this.

![mceclip14.png](https://support.optisigns.com/hc/article_attachments/8099827611283)

2. Type the

```
ipconfig /all
```

![mceclip17.png](https://support.optisigns.com/hc/article_attachments/8099901932307)

3. Navigate to the section “Wireless LAN adapter Wi-Fi” or "Ethernet adapter Ethernet" depending on whether you connect through wireless or wire network. The MAC Address will be shown next to “Physical Address”.

![mceclip16.png](https://support.optisigns.com/hc/article_attachments/8099899957651)

## That's all!

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
