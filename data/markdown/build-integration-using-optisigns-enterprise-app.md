# Build Integration Using OptiSigns Enterprise App

Article URL: https://support.optisigns.com/hc/en-us/articles/13320135306515-Build-Integration-Using-OptiSigns-Enterprise-App
Article ID: 13320135306515
Last Updated: 2025-08-28T20:24:19Z

The digital signage use case for enterprise user is complex. There may be needs to integrate with various systems and have those systems to initiate a process to send data and control the screen.Or in some cases, there may be a need even to build a custom single purpose app used to operate the screens. OptiSigns Enterprise App is specifically designed for these types of real-time enterprise data integrations. With OptiSigns Enterprise app, you can easily achieve:

- Load a custom-designed page on the screen as needed and have data points integrated with any applications that need to control the screen.
- Embed and build the integration with your enterprise applications and allow you to send freeform data to the screens.
- Develop your own single purpose application to manage the screens and assets with all the APIs that are available with the framework.

OptiSigns Enterprise app is a framework and pre-built template to help enterprise customers easily build integration with their enterprise applications that need to send data to the screen and control the screen. It can be used in various cases, for example, you can use it to send customer specific communications from your CS system to your customers. In this guide, we will walk you through how to use the OptiSigns Enterprise app with the example below.  
![mceclip0.png](https://support.optisigns.com/hc/article_attachments/13440210713235)

### **How to use OptiSigns Enterprise App:**

OptiSigns Enterprise App is more than a framework, it also contains templates to help you with the development and deployment. There are mainly 3 steps to get Enterprise App setup and working properly.

1. Create Enterprise App and build your custom designed page.
2. Build the integration to your enterprise systems or custom applications. For this tutorial, we will use the demo control center as an example.
3. Send data from your system to the screen and get it published.

#### **1. Create Enterprise App and build custom designed page.**

Go to [app.optisigns.com](https://app.optisigns.com/).

Click Files/Assets, then click Apps, and select "Enterprise App".

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/13320712580627)

In the next page, click the template picture to create new project, this will be launching a WebIDE with sample code, where you can make adjustment to customize the page layout and how you want to interact with the data points from other systems. If you have an existing URL available, you can use it as well.  
![mceclip3.png](https://support.optisigns.com/hc/article_attachments/13320774310291)

The template comes with sample code that you can use directly, all you need to do is to change how you would like the page to look like and how you want to handle the incoming data points from other systems. Once you are done with the changes, click "Save&Deploy" button, it will be ready for use.

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/13320838658451)

#### **2. Build the integration to your enterprise systems or custom applications.**

We will use the demo Control Center to show how you can send data and interact with the screens in this tutorial. In your cases, the demo Control Center will be your systems that you want to initiate the process to control the screen or a custom application that was specifically built for your need.

Click "Control Center" in the Enterprise App, it will launch the demo Control Center.

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/13320889712915)

The demo Control Center will launch with the logon page first. In this case, you just need to use your OptiSigns account. The framework supports authentication and authorization, when you build your integrations with other systems, you will have the capability to utilize the authorization you defined with in OptiSigns.

After logon, the demo Control Center will list all the screens that you have access to. You can also search the screens that you want to control. In this case, we will try to control the Enterprise App Demo Screen.

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/13321031641363)

Click the "Edit" button will popup the Edit Device page. This is where we can control how to send data to the screen.

![mceclip8.png](https://support.optisigns.com/hc/article_attachments/13321033226131)

#### **3. Send data from your system to the screen and get it published.**

Looking at this screen, we can have any asset/playlist/schedule assigned to the screen. The screen will just play the assigned content as normal. When we initiate the integration from the demo Control Center, we can send the freeform JSON data to the screen, and assign the Enterprise App asset ID to take over the screen immediately and display the data.

Now, the screen is assigned an asset other than the Enterprise App.

![mceclip9.png](https://support.optisigns.com/hc/article_attachments/13321076982035)

If we go back to the demo Control Center, and put in the data that we want to send to the screen, and the Enterprise App asset id, then click Save. It will take over the screen and load the Enterprise App on the screen with the data that we sent over.  
Once done, you can click the "Stop" button to end the integration.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/13440341376531)

To verify the data that was sent to the screen, you can go back to the OptiSigns portal, find the screen. Expand the "Advanced" section, then expand "More" section.

At the bottom of the Edit Screen page, click the button to show the Device Specific Info. You can see the same data sent from the demo Control Center.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/13440441484051)

On the screen, you will see those data sent from the demo Control Center are displayed accordingly. Including the customer name, car model, advisor name, and the image.

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/13440515661203)

**That's all!**

This is how you can build integration with OptiSigns Enterprise App.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
