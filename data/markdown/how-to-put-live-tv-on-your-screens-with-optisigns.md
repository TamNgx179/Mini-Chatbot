# How to put Live TV on your screens with OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/10159088954387-How-to-put-Live-TV-on-your-screens-with-OptiSigns
Article ID: 10159088954387
Last Updated: 2025-09-02T20:01:30Z

With OptiSigns, you can show the Live TV from your cable TV services (such as Xfinity, DirectTV) on your screens. There are 2 ways you can do it with OptiSigns.

- If you are using a windows player and just need to show it on a single screen, you can follow the HDMI Video Input approach and use the Live TV app to achieve it. You can refer to [this article](https://support.optisigns.com/hc/en-us/articles/1500002042241) for more details.
- If you would like to broadcast to more than one screen and use any media players, you can follow this document and use the video streaming app to achieve it.

Video streaming app is used to subscribe to the live streams transferred through HTTP, such as HLS, DASH. HTTP is widely used for the internet data transfer, it is supported well on almost all the platforms, such as Windows, Linux, Android, etc. To stream Live TV, you will need to get a HDMI Video Encoder to convert the Live TV to a HLS stream, such as this [URayCoder HDMI Video Encoder](https://a.co/d/ezieSsp). Then the video streaming app can be used to show the Live TV on your screens, and you can use the same HLS stream on multiple screens as long as they are in the same network.

In this document, we will walk through how to show the Live TV using the video streaming app. It consists of 3 steps at high level.

1. Set up the HDMI Video Encoder.
2. Create the video streaming app
3. Put the Live TV on your Screen

If you have an IPTV system in place which supports HLS already, you can skip step 1 and set up the video streaming app to put it on your screens directly.

**1. Set up the HDMI Video Encoder**

The HDMI Video Encoder has an admin console to manage the configuration and settings. Depending on the encoder you use, you will need to access it differently. Please follow the instructions of the HDMI Video Encoder to access the admin console. For the UrayCoder HDMI Video Encoder, the default IP address to access the admin console is 192.168.1.168

Once in the admin console, please go to the setting page to configure the video stream to be used. In this case, we will need to make sure the HLS stream is enabled, the rest of the streams can be disabled.

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/10158743969939)

Click Apply after the change, then you will be able to see the URL to use for the HLS stream from the status page.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/10158882063635)

**2. Create the video streaming app**

Go to asset->app section to create a video stream app. Simply put the HLS stream URL of the HDMI video encoder in the video streaming app, then it will be available for use. You can refer to [this article](https://support.optisigns.com/hc/en-us/articles/8369526604435) for more information about the video streaming app.

.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/10158846152467)

**3. Put the Live TV on your screens**

Now the video streaming app is available for use, you can assign it to any screens you want to show the Live TV. Please make sure that the screens need to be in the same network as the HDMI video encoder, so that the HLS stream is accessible by your screens. For more information on how to assign content to the screens, you can refer to [this article](https://support.optisigns.com/hc/en-us/articles/360016375153).

You can also put it in the splitscreen app, then you will be able to have other information to show together with the Live TV. You can refer to [this article](https://support.optisigns.com/hc/en-us/articles/360026559573) for more details on how to setup multiple screen zones.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/10159027869971)

### **That's all! Congratulation!**

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
