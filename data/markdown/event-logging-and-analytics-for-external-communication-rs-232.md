# Event logging and analytics for External Communication(RS-232)

Article URL: https://support.optisigns.com/hc/en-us/articles/17342932920211-Event-logging-and-analytics-for-External-Communication-RS-232
Article ID: 17342932920211
Last Updated: 2025-09-02T19:09:02Z

With OptiSigns you can enable track of the data communication between the digital signage player and external devices through external communication (RS232). The feature is available for customers on Enterprise plan.

Once it is enabled, it will keep tracking of the inbound/outbound event data that was sent between the digital signage player and external devices. For example, if you are using IoT sensors, the feature can track the serial command that was sent from your sensors, and you can analyze the data to monitor and further optimize your IoT sensors usage. Or you can track the RS232 commands(power on/off, mute/unmute etc) that was sent to your TVs and use it as a proof of your compliance.

### **Prerequisite:**

To use this feature, you will need to confirm in advance that the connection between your digital signage player and external devices are working properly.

The external communication(RS-232) should be configured and tested. Depending on your use case, you can follow below listed documents.

- If you are using RS-232 commands to communicate with your TV, please check the [advanced scheduling feature](https://support.optisigns.com/hc/en-us/articles/9061950942995-Using-RS-232-to-Schedule-TV-Power-On-Off-or-other-commands).
- If you are using IoT sensors, please check [IoT sensor Add-on](https://support.optisigns.com/hc/en-us/articles/13097501958291-OptiSigns-IoT-Sensor-Add-on-Quick-Start).

Note: To test and confirm your external communication(RS-232) connection and configuraiton are set up properly, you can use the "Trigger Event Viewer" from the side menu of OptiSigns player. It can show the events received from external devices/sensors, and also you can use it to test send commands out to external devices.  
![](https://support.optisigns.com/hc/article_attachments/17344618238099)

![](https://support.optisigns.com/hc/article_attachments/17344754633875)

## 

## **Let's jump in and get started:**

**1. Setup: Enable RS232 logging**

If you are on Enterprise plan and interested in this feature, please contact

[support@optisigns.com](mailto:support@optisigns.com)

Once the feature is made available, you can go to settings, under Advanced->External Communications(RS232) you will see the setup(Analytics) page available. You can also use the link below.  
<https://app.optisigns.com/app/s/external-coms>

Click "Analytics", you will be able to enable the RS232 logging here.

![](https://support.optisigns.com/hc/article_attachments/17345659223187)

By default, event data will be logged in real-time.If internet is disconnected, data will be saved locally and will be synced to server automatically when the device come back online.

If for some reason, you don't want real-time data (i.e. to reduce network usage during day time, or if you do "drive-by" data collection once a while). You can unchecked Real-time option and select an upload interval of your choice.

**2. Enable data collection on IoT sensors add-on**

If you are using IoT sensors, you can set it up to collect the event data within the IoT Sensor Add-on. Simply tick the "Send Data" checkbox, it will start to track the event data.  **![](https://support.optisigns.com/hc/article_attachments/17351908243987)**

**3. Data collection with advanced scheduling**

If you are using advanced scheduling to control you TV or other devices supporting RS232, the event data collection is enabled by default if you choose the "RS232 Commands" type. You can configure and send multiple commands together, the commands will be sent to the target device one after anther with small latency. If the target devices are responding with confirmation, the response will be logged as well.

Please note, if you are sending multiple commands together, please check the target device specification, the target device may take longer time to execute the commands, in the case, please send the command separately on its own, otherwise the following commands may not be executed and you will not see response from the logging.

![](https://support.optisigns.com/hc/article_attachments/17352284082323)

**4. Export Data: Schedule data export & download data**

You can configure OptiSigns to regularly export your raw data.

Here you can control the frequency of the data export, time window of the data export, and the recipients of the data exports. Also, if you have your own AWS S3 buckets available, you can also configure your AWS S3 as the destination of the data export, it is easier for you to automate and connect it to your own analytics process.

![](https://support.optisigns.com/hc/article_attachments/17345743164307)

Here's how a data export looks like:

![](https://support.optisigns.com/hc/article_attachments/17343162545043)

You can also go to the report history tab and download the historical data export.

![](https://support.optisigns.com/hc/article_attachments/17345817445779)

## **Summary:**

The RS-232 logging and analytics will collect the event data and make it available to customers. The data is available in JSON format, you can automate the data export and build your own data pipeline to process the data for further analysis.

**That's all!**

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
