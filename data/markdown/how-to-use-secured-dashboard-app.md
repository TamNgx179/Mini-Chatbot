# How to use Secured Dashboard App

Article URL: https://support.optisigns.com/hc/en-us/articles/19589190970771-How-to-use-Secured-Dashboard-App
Article ID: 19589190970771
Last Updated: 2025-09-02T20:28:00Z

Displaying KPIs and reports on the screen is a common use case for enterprise customers, however, companies are using different reporting systems, which makes this a difficult task to accomplish. OptiSigns has delivered a [Web Scripting App](https://support.optisigns.com/hc/en-us/articles/1500012522362) for customers to access their password-protected reporting systems without coding, it also supports Multi-Factor Authentication, for details please follow this [article](https://support.optisigns.com/hc/en-us/articles/19145077187859).

Web Scripting App executes the scripts locally on the device, it is the recommended solution for customers to access their reports. However, there are still cases in which customers need another way to execute and display the reports. Below are a few examples. A Secured Dashboard is recommended in these situations.

- Customers use the same account with MFA to authenticate on multiple devices. Since MFA is using a one-time passcode, it will error if multiple device authentications are started at the same time.
- Customers have a mixed device fleet, like Windows and Android are used together. Reports may render differently on Windows and Android, which may cause inconsistency in the report presentation.
- Customers have reports that take a long time to execute/load, and looking for ways to avoid showing the loading status on the screen.

Secured Dashboard App will take the same scripts you recorded with the Web Scripting App, put it to execute on a dedicated instance, and return a screenshot of the reports. It can help address all the situations mentioned above and more.

## **Let's jump in and get started:**

**1. Get the scripts ready**  
Secured Dashboard uses the same scripts you recorded when you use the Web Scripting App. You can follow the document below and use Burp Suite Navigation Recorder to prepare the scripts and test them on the Web Scripting App.  
[How to use Web Scripting App – OptiSigns](https://support.optisigns.com/hc/en-us/articles/1500012522362-How-to-use-Web-Scripting-App)  
If you are using MFA, you can follow this document, to get the MFA set up with the token and secret.

[How to use Web Scripting App with 2FA](https://support.optisigns.com/hc/en-us/articles/19145077187859)  
Once the script is tested with Web Scripting App, you can copy it and create the Secured Dashboard App with the same info.

![](https://support.optisigns.com/hc/article_attachments/19593475063955)

**2. Configure the Secured Dashboard execution**  
There are a few settings that allow you to control how the scripts are executed. Secured Dashboard will execute the scripts on a dedicated instance, and then take a screenshot of the report according to your settings.

- Resolution: The default setting is 1080p - FHD(1920x1080) in landscape mode. You can choose other resolutions, even custom resolutions. Please note if you would like to display in portrait mode, you will need to choose custom resolutions and set the resolutions accordingly, e.g. 1080x1920.
- Full Page: If you select full page, it will take a screenshot of the entire webpage, even if the webpage is scrollable.
- Clip: This allows you to take screenshots of certain sections of the webpage. You can set the starting point of the screenshot from the top left, and the width and height of the screenshot.  
  ![](https://support.optisigns.com/hc/article_attachments/19595347412627)
- Delay: This allows you to set when the screenshot is taken. The default is 30 seconds, meaning the screenshot will start the 30s after the scripts are executed. If your report data takes a long time to load, you can set a proper value here to pass the loading.

After completing all the settings, you can assign it to the screens, the screenshots will update at the set interval.

**Note:** If your reporting systems have firewall rules or using CAPTCHA to block bots, you can contact us to get the IP address that you can use for whitelisting

## **That's all!**

If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
