# Integrating Point-of-Sale (POS) Systems to Build Digital Menu Boards with OptiSync

Article URL: https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync
Article ID: 31860170199955
Last Updated: 2025-09-04T20:31:25Z

### OptiSync allows you to create dynamic digital menus through API integration. Your POS systems can interface directly with OptiSigns to automatically update prices, track inventory, and more.

- [How to Integrate POS Systems Through API Requests](#Section%201)  
  - [Get API URL Endpoint and Set Up API Request DataSource](#Section%202)
  - [Additional Information on API Authentication](#Section%203)
  - [Handling Multiple Stores or POS Locations](#Section%204)
  - [How to Use Post-Request Processing to Convert API Data](#Section%205)
- [How to Build Digital Menu Boards in Designer with OptiSync](#Section%206)  
  - [Using DataSources and Repeaters](#Section%207)
  - [Element Mapping](#Section%208)  
    - [Adding Text Elements to Your Menu](#Section%209)
    - [Creating Strike Throughs and Sold Out Warnings](#Section%2010)
- [Pushing a Digital Menu Board to a Screen](#Section11)

In this article, we will create a real Digital Menu Board (DMB) integrated with a Clover POS system. The DMB pulls product info from Clover and display it onscreen. When an item is not available, it will display as "SOLD OUT."

|  |
| --- |
| **NOTE** |
| API Integration is only available with a **Pro Plus** plan or higher. |

---

## How to Integrate POS Systems Through API Requests

Most POS systems have an API library which OptiSigns can use to get the relevant data from the system programmatically. This API can return menu items, item price, availability, and more.

With OptiSync, we can link APIs to the OptiSigns portal and push the data to screens as a Digital Menu Board (DMB) or any other type of screen you'd like without the need of human intervention.

![api optisigns integration diagram](https://support.optisigns.com/hc/article_attachments/31860108901523)

This article will focus on these POS specific wrinkles, and the process of mapping POS data to assets and pushing them to screens.

|  |
| --- |
| **IMPORTANT** |
| In order to integrate a POS system, you'll need to first set up an API Gateway request. A complete guide for how to do that can be found [here](https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync). |

---

### Get API Endpoint URL and Set Up API Request DataSource

We have a [comprehensive guide](https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync) on how to set up your API gateway request. We recommend following this guide until your initial request is set up.

Bare minimum, you'll need an API endpoint URL and an API Authentication token.

### Additional Information on API Authentication

For most token based authentication, setting up the authentication token with the key store is normally all that's required for an API request. But certain APIs (such as Toast) will require additional calls to get the authentication token for each request, this can be handled through pre-request processing. To see how to handle that, see our [article on Toast APIs](https://support.optisigns.com/hc/en-us/articles/31113088917907-How-to-use-Toast-API-data-with-OptiSigns).

### Handling Multiple Stores or POS Locations

Once you've got your basic API Gateway request set up, there are a few additional steps you'll want to perform if you have multiple locations for your screens. These different locations may have different menus, or different specials for that day, or even different pricing depending on various factors.

POS systems normally require separate license for each location. Your POS system API may provide different store ID in the API endpoint or using different authentication token. For larger deployment with multiple stores, you can use substitution parameters to handle that with OptiSigns.

There are two ways to handle multiple POS locations:

1. Set up individual API requests for each of your POS locations, changing the value in the URL endpoint each time and mapping them to each of your screens individually. If you only have a few locations where your POS system is used, this will work just fine.
2. *(Recommended)*Configuring each screen to send its storeID to the API call, allowing a single API request to provide data to multiple screens. For anything more than two or three screens, we recommend this method.

Here's how to handle option 2.

To get started, find the screen you wish to edit.

![edit screen](https://support.optisigns.com/hc/article_attachments/31893086724755)

Click **Advanced** **→** **More** **→** **Device Additional Attributes.**

![device additional attributes on edit screen](https://support.optisigns.com/hc/article_attachments/31893080684563)

Two fields will show up, **Key** and **Value**.  
![device additional attributes key value](https://support.optisigns.com/hc/article_attachments/32043124363155)

- **Key** - A parameter that will be used during the API call to substitute for your store's value. This will replace part of your API URL endpoint.
- **Value** - Represents the unique code associated with the store or location you wish to pass through to your API.

In this example, we'll pretend the parameter you are changing is called "merchantID". The value inputted will need to be obtained on your end as it will be unique.

Now, go back to the API request config page. Substitute the merchantID in the API endpoint with the Key name you previously defined.

#### **clover url request**

When the API request is triggered on the device, it will take the value from the device and substitute it at runtime. For each screen, you'll want to perform these same steps, keeping the Key name the same while changing the Value. This will allow you to push different data to different screens off a single API Request.

### How to Use Post-Request Processing to Convert API Data

When retrieving data from your POS system, it may not initially show up exactly the way you'd like, or you might want to add some functionality, such as the ability to display SOLD OUT for items out of stock.

For example, prices may display as whole numbers (i.e. 1299 instead of $12.99). That's where the "Post-request" tab comes in - this allows changes to be made to the data after it comes in. This will require some basic coding to use.

Take the example of the price display from earlier. How would we convert a number like 1299 to display as $12.99, and make that piece of code extensible to any similar display errors (e.g. 1899 instead of $18.99)?

![](https://support.optisigns.com/hc/article_attachments/31893086743187)

For this common example, this piece of JavaScript code should solve your issue.

```
let {data, headers, status} = os.context.get("response");  
temp_data = data.elements  
for (let object of temp_data) {  
        object.price = '$' + (object.price*.01);  
        if (object.available == true)  
              {object.soldout=0;}  
            else {object.soldout=1;}  
    }  
return temp_data
```

This will fix the returned data, allowing it to display properly. It will also allow for creation of SOLD OUT and strike through for when items are out of stock.

![](https://support.optisigns.com/hc/article_attachments/32060273039763)

|  |
| --- |
| **NOTE:** Enabling and configuring a WebHook allows near real-time updating of the data pulled from your API. If you plan to keep track of store inventory using your digital signs, we recommend setting one up. You will need to input the provided WebHook key into your API to set this up. |

 

---

## How to Build Digital Menu Boards in Designer with OptiSync

In order to create a DMB with data from your POS system, the API Request will need to be registered as a DataSource. This allows data elements to be added to [OptiSigns' Designer app](https://support.optisigns.com/hc/en-us/articles/4404151402899-How-to-use-OptiSigns-Template-Designer-app-to-make-your-Digital-Signs-in-minutes), where it can be formatted and incorporated into any visual design you'd like to display.

The Designer app and templates can be used to do the formatting, and mapping the element to the data from the API data source. Any text box or image element can be mapped in Designer. When you map an image element, the URL of the image will be replaced at run time.

---

### Using DataSources and Repeaters

To get started, find your design or create a new one in the **Files/Assets** tab.

With the design open, click **"DataSource"** in the left hand column. Then, click **"Add DataSource"** to add an API data source to the design.

![firefox_ebkICMVoVf.jpg](https://support.optisigns.com/hc/article_attachments/43051537966355)

Scroll down to where it says **"API Gateway Collection"** and click it.

![firefox_mCdtjleFse - Copy.png](https://support.optisigns.com/hc/article_attachments/31936613189523)

You can also set up a one-time Gateway with the *API Gateway* command if you need a one-off design with no pre- or post-request processing. In our example, however, we are, so we'll use Gateway Collection.

You should see this screen:

![firefox_xXJk2r7wuv - Copy.png](https://support.optisigns.com/hc/article_attachments/31936613193747)

- **Name -** The name of the DataSource. This is internally facing and will not be shown on your screens.
- **Select APIs -** Here you'll select from the API Gateways you've already set up in earlier steps. You can select just one, or multiple. If multiple are selected, the API DataSource will automatically aggregate them.
- **Update Interval -** How often to send requests back to the API for updates. Select from None (never call the API back), 30 minutes, 60 minutes, or every 6 hours. If you Enable WebHook on your API Request and input the provided URL in your API, this Update Interval will change to near real-time.

Hit **Save**, and the DataSource is created.

It should appear in the left column under **"Used in this design".**It will definitely appear in the **"Other DataSources"** section. You may need to refresh the page for it to appear.

![](https://support.optisigns.com/hc/article_attachments/31937799814163)

### Element Mapping

Now that you've got your API DataSource has been created, we're ready to map the data. In this example, we will show you how to make a DMB with the ability to strike through product names and display the phrase "SOLD OUT" when the item is out of stock.

#### Adding Text Elements to a Digital Menu Board

First, create your design. You can create your menu within our Designer app.

![firefox_g87oDmb7i3.jpg](https://support.optisigns.com/hc/article_attachments/43051537968787)

The easiest way to set up a DMB is with a **Data Repeater**. For a full breakdown of a Repeater's capabilities, [see this article](https://support.optisigns.com/hc/en-us/articles/29217646663187). Here, we'll stick to teaching how to add information from your POS system.

To set up a Repeater, click **"Repeaters" → Add Blank Repeater**.

![](https://support.optisigns.com/hc/article_attachments/43051537970195)

With the Repeater selected, click **Settings**. Then select **Connect to DataSource** on the Side Menu.

![firefox_yX20kMKstf.jpg](https://support.optisigns.com/hc/article_attachments/43051537971219)

Select the DataSource you set up in the last set under **"Other DataSources"**.

You'll be taken back to the last pane with your DataSource now selected. Now, click **Edit** or double click the selected Repeater to head to the Repeater Editor. This is like a design-within-a-design, specifically for your Repeater (menu) items. With text selected, click the arrow on the left.

![](https://support.optisigns.com/hc/article_attachments/32078326973331)

That brings up the DataSource tab. Click on the DataSource Used in this Design and you'll see something like this:

![](https://support.optisigns.com/hc/article_attachments/31968058948371)

In this example, we want to display the name and the price, with the possibility of saying "SOLD OUT"

By creating text and dragging data points to it, we can create a menu item like this:

![](https://support.optisigns.com/hc/article_attachments/32060268861331)

This was created by finding data points from the API and dragging them into the desired text boxes. In this case, we only wish to display the "name" and "price," so those values were what we dragged into a blank or existing text box.

If your numbers need extra formatting, click on the number, then hit **Settings.**

**![](https://support.optisigns.com/hc/article_attachments/32077278901139)**

Click **Advanced Options →** **"Display Format"** and choose **"Number,"** then click **"Number Format"** and select the formatting you'd like. This will allow you to add dollar signs to your prices, with other options.

![ShareX_q0ybaobi0E.png](https://support.optisigns.com/hc/article_attachments/32060268867859)

Make sure to hit **Update** to make your new number format display.

![mraS5gfp1n.png](https://support.optisigns.com/hc/article_attachments/32060273056019)

The value of a repeater is that it will copy the format of this one cell, then replace the data points with others from your API. Done correctly, your menu should look something like this:

![](https://support.optisigns.com/hc/article_attachments/32077278906643)

The Repeater will pull as many data points as you have set up on your API. In this example, we've made a menu with 9 items, but with proper design you can put as many items as you'd like, with dynamic descriptions as well. If you have more items than what you've set to show on your screen at any one time, the items on the menu will rotate through them until they have all displayed.

#### Creating Strike Throughs and Sold Out Warnings

In the above example, we show a Sold Out warning. However, we don't want to display that all the time - only when the item isn't available. With OptiSync, this can be accomplished thanks to the Post-request processing we did earlier. Our code created this **"soldout: 0"** data. This is tied to our **"available"** data:

![](https://support.optisigns.com/hc/article_attachments/32077278913043)

When the "available" data reads "true," the "soldout" data reads 0. When your POS system detects items are unavailable, the "available" data will read "false". This will make the "soldout" data read 1.

We can use this knowledge to set up our Sold Out warnings and strike throughs to only appear when items are not available.

Going back to our Repeater Editor, we can click on a piece of text we want to strike through and hit **Settings**:

![](https://support.optisigns.com/hc/article_attachments/32077293399315)

In the Settings tab, hit **Advanced Options**.

![](https://support.optisigns.com/hc/article_attachments/32077801189779)

Under Advanced Options, hit **Property Mapping**.

![](https://support.optisigns.com/hc/article_attachments/31968071408915)

Two values will show up: **Property** and **Value**.

![](https://support.optisigns.com/hc/article_attachments/31968059040275)

Under Property, choose **Linethrough**.

![](https://support.optisigns.com/hc/article_attachments/31968450832915)

Under Value, choose **.soldout.** Before the "." will be the name of your API Request.

**![](https://support.optisigns.com/hc/article_attachments/32077293403411)**

This sets the text to be crossed out when the "soldout" data reads 1.

We can repeat this with the Sold Out reading, except instead of Linethrough, choose **Visible**.

![](https://support.optisigns.com/hc/article_attachments/31968463038227)

This will make the Sold Out text only appear when the "visible" data reads 1 - in other words, when your product is sold out.

Your final menu ought to look something like this:

![](https://support.optisigns.com/hc/article_attachments/32077820105875)

Finally, you're ready to Name and **Save** your Design.

## Pushing Digital Menu Boards to Screens

Getting your new DMB onto a screen is relatively simple. Go back to the screens you set up with substitution parameters earlier. Then, hit **Edit Screen.**

![](https://support.optisigns.com/hc/article_attachments/31969909937299)

Under **Type**, choose asset, then select your DMB asset to play.

## That's all!

You should be able to create an Digital Menu Board with dynamic data features.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
