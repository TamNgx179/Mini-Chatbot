# How to use RTSP Stream on Windows or Raspberry Pi via OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/8066591235603-How-to-use-RTSP-Stream-on-Windows-or-Raspberry-Pi-via-OptiSigns
Article ID: 8066591235603
Last Updated: 2025-09-02T19:20:51Z

#### Nowadays, RTSP Camera Streaming is popular. You can display your RTSP Stream on your Digital Screen via OptiSigns. Support_article_-2.png

This article will guide you through how to create and use the RTSP Stream app on Windows or Raspberry Pi. Note: For this feature, you must run OptiSigns player version 5.3.2 or newer on your devices. You can download the latest version of the app at [https://www.optisigns.com/download](http://www.optisigns.com/download)

If you want to use the Fire Stick or Android Stick to display the RTSP Stream app. The setup will be different. You can click [here](https://support.optisigns.com/hc/en-us/articles/8098889840531).

Windows and Raspberry Pi don't support the RTSP HTML5 directly. Before you create the RTSP Stream app, you will need to transcode RTSP to HTTP. Then you can implement RTSP live streaming on the Windows and Raspberry Pi devices. The easy way of achieving RTSP HTML5 playback on Windows and Raspberry Pi is to embed VLC into the HTML5 webpage and adopt it as an HTML5 RTSP player.

### **Let's jump in and get started:**

#### **1. How to use it on Windows and Raspberry Pi devices.**

Before setting up, you will need to prepare:

1. Need the VLC Media Player. You can download it [here](https://www.videolan.org/vlc/index.html).
2. RTSP URL. (Here is an example: rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny\_115k.mp4)

Then you can follow these steps to set it up.

Step 1. Launch VLC Media Player, go to the "**Media**" > **Open Network Stream**

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/8066835391379)

Step 2. Go to the "**Network**", type in the RTSP URL to the "**Network URL**". We use this as a sample example. (rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny\_115k.mp4)

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/8066888364051)

Step 3. Click the dropdown and select "**Stream**".

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/8066876184211)

Step 4. Click "**Next**"

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/8066895761171)

Step 5. Select "**HTTP**", and Click "**Add**"

![mceclip8.png](https://support.optisigns.com/hc/article_attachments/8066948003603)

Step 6. Type "**9999**" in the "**Port**" and "**/stream.ogv**" in "**Path**". The address of the output stream will be the IP address of "your native server/stream.ogv". Click "**Next**" to proceed.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/8099130145555)

Step 7. Select "**Video-Theora+Vorbis (OGG)**". Then click "**Next**"

![mceclip11.png](https://support.optisigns.com/hc/article_attachments/8066996433683)

Step 8. Check the output media codec at "Generated stream output string", make sure **vcodec=theo** and **mux=ogg,** otherwise manually modify. Then, click "**Stream**".

![mceclip12.png](https://support.optisigns.com/hc/article_attachments/8067037167379)

When it is successful, it will start the run. You can see the screenshot below.

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/8099117325203)

#### **2. Now it's time to create the RTSP stream app in OptiSigns Web Portal.**

Note: Keep VLC running for constantly transcoding, and embedding RTSP stream HTML5 webpage.

Go to Files/Assets, Click on "App", search for, and add the RTSP Stream app to your Account.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/8066535317907)

Enter your RTSP Stream App information:

## mceclip3.png

- Name: Name of your RTSP Stream app, this is the name of the app in your asset list. It will **not** be displayed on your screens.
- URL: the URL link will be your local IP address with your setup. (http://[Your IP address]:[Port]/[path])

Click Save to save your asset.

## That's all!

Congratulation! You have created your RTSP Stream App. Then you can assign it to your Windows or Raspberry Pi device.

You can change the wall at any time by clicking on it in the Files/Assets tab.

You can put the walls in a Playlist, Schedule too.

If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
