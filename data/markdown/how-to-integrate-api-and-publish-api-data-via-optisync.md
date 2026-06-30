# How to Integrate API and Publish API Data via OptiSync

Article URL: https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync
Article ID: 22875592994195
Last Updated: 2025-09-04T21:00:02Z

### Integrating your API with OptiSigns has many uses and allows easy display of auto-updating data on your screens. In this guide, we'll walk you through how to connect your API - no software engineering background required.

- [What API Integration Can Do](#Integration)
- [What You'll Need to Get Started](#What)
- [How to Set Up an API Request](#Request)  
  - [Step 1: Store Your API Authorization Token in the OptiSigns API Keystore](#Store)
  - [Step 2: Set Up and Test the API Request](#Test)
    - [How to Use Parameters](#Parameters)
    - [How to Use Pre- and Post-Request](#PrePost)
  - [Step 3 (Optional): Use Substitution Parameters from Device Attributes](#Substitution)
- [How to Map API Data in Designer](#Map)
  - [Step 1: Creating an API DataSource](#Create)
  - [Step 2: Maintain the Element Mapping](#Maintain)
- [More on OptiSync Use Cases](#Use%20Cases)

|  |
| --- |
| **NOTE:** API Integration is only available with a **Pro Plus** plan or higher. |

---

## What API Integration Can Do

OptiSigns allows easy integration with user APIs. This allows data from a user's API to be shown on any of your digital signs. This allows dynamic updates for:

- **Digital Menu Boards** - Integrate with your POS systems and get the DMB updated automatically, and edit the format of your DMB using the designer app whenever needed.
- **Automated HR Update** - Use the API from your HR systems to display birthdays or work anniversaries on the screens automatically.
- **Warehouse Inventory Tracking** - Use your Warehouse's API to display inventory levels with automatic updates throughout your organization
- Any other information display use cases that you will need to consume API data and display the data on the screens.

This API integration can be achieved in OptiSigns with little to no coding, making it approachable for those without backgrounds in software engineering. In this guide, we will walk you through how to get it set up with the example below using an API from the Clover POS system.

---

## What You’ll Need to Get Started

You’ll need your:

- **API Endpoint URL**
- **API Authorization Token**

These are required for OptiSigns to connect with your desired API. Make sure you have them in an easily accessible place before you try to set up your API Request in the OptiSigns Web Portal. You should be able to obtain these from an IT professional in your organization, or through your POS system administrator.

---

## How to Set Up an API Request

The API gateway is a powerful tool that allows users to centrally manage the APIs, as well as configure and test the APIs.

Now that you have everything you need, let's get started on setting up an API Request. With an API request, you can:

1. Use the OptiSigns API Keystore to securely store and use API keys from other systems.
2. Test the API endpoints, with the capability to modify headers and parameters.
3. Use substitution parameters and pre-processing and post-processing rules to handle complex integration. Pre-processing rules can help you handle those API integration situations that require an additional call to get an authentication token before making the API call. Post-processing will allow you to process the returned data and tailor it to fit your use better.

To get started, open your OptiSigns Web Portal.

Once there, navigate to the upper right corner of the screen, and hover over your account name.

Hover over **More →** **DataSources**

**![](https://support.optisigns.com/hc/article_attachments/32427378791315)**

You'll see the screen below.

![](https://support.optisigns.com/hc/article_attachments/32427378806803)

Now you're ready to get started.

---

### Step 1: Store Your API Authorization Token in the OptiSigns API Keystore

The first step is to take your API Authorization Token and store it in the OptiSigns API Keystore.

This step is technically optional: you can input your API Authorization token into an individual API request. However, the Keystore has a few major advantages:

- Allows your API Authorization token to be sent to multiple API requests, without the need to manually input it each time
- Provides superior security for your API Authorization token, making it much harder for outside actors to discover it

Therefore, we ***highly recommend*** this step.

To enter the Keystore, find the **Lock Icon** and click it.

![firefox_YNrLQDITUl.png](https://support.optisigns.com/hc/article_attachments/32427362113683)

This will open the **API Keystore.**

![](https://support.optisigns.com/hc/article_attachments/32427378817171)

Click **Add Key**.

![firefox_Af1bBuAYxy.png](https://support.optisigns.com/hc/article_attachments/32427378823187)

There are two fields here.

- **First Field -** Enter the name of the key here. We recommend something that will help you remember it. You'll be using this to set up an API request.
- **Second Field -** The actual unique passcode for your API communications.

Once you've input your API Authorization token, hit **Save**. When you want to run a request using this API Key, you'll use the term: **{{apiKeystore.<<key>>}}** where "<<key>>" is replaced by the name you inserted earlier. In this example, we'll name our request "clover".

![](https://support.optisigns.com/hc/article_attachments/32427378828051)

Now, we're ready to set up your API request.

---

### Step 2: Set Up and Test the API Request

Before moving forward in OptiSigns, we recommend [**testing your API**](https://www.postman.com/api-platform/api-testing/) connection using a free tool, such as [**Postman**](https://www.postman.com/). This provides several advantages, including:

- Checking your data formatting
- Ensuring the correct data is being provided
- Verifying your authentication
- Identifying integration problems or connection errors

The test parameters, endpoints, and authenticators can then be used in OptiSigns to set up your API request. Here's how to do that.

![firefox_orSTybxxGU.png](https://support.optisigns.com/hc/article_attachments/32427362124563)

Click the **Add Request** button, it will launch the window for you to configure and test the API request.

![firefox_owER9ex9xQ.png](https://support.optisigns.com/hc/article_attachments/32427362128147)

- **Display Name -** This will be shown under the API gateway list, mainly to help users identify the API request.
- **Name -** This is used as a reference to the API request, it is a technical name that will be used later in the path to refer to the API request data.
- **URL -** This is the API endpoint, you can use the GET or POST method depending on the API request, for example, if you are using GraphQL, then all requests will be using POST.
- **Params -** Allows you to define the parameters in your API request. You may see parameters in your API endpoint URL, these will be preceded by a "?" mark. These can be used in pre and post processing request code to further automate your API request.
- **Headers -** The header(s) of the API request. You will want to input your API Authentication token here.
- **Pre-request -** An optional piece of code which prepares the context before the API request. For example, you may need to call another API to get a short-lived authentication token before calling the API, or you need to calculate some variables to be used in the API request.
- **Post-request -** An optional piece of code which modifies the data received from the request. For example, if the data you receive is not exactly how you want it displayed, you can write a bit of code to modify it according to your digital display needs.
- **Enable Webhook -** Generates a webhook link and an associated token. This webhook can be used to notify us of a change in the data, which will refresh the API request and update your screens automatically.
- **Enable this Request** - Set the status of the API request.

To test the request, we'll need to configure the header. This is where the Keystore comes in. In the second box, type **Bearer {{apiKeystore.<<key>>}}**, where *Bearer* is the type of token and *{{apiKeystore.<<key>>}}* pulls the token stored in the Keystore. In this example, we'll use the name "clover" as referenced above.

Once that's done, click **"Run Test"**. If the response code is 200, the API has returned data successfully. If there is any other code, there is an issue in the API Request.

![](https://support.optisigns.com/hc/article_attachments/22917836593171)

#### How to Use Parameters

Parameters are present in URLs of all types. There are two elements to a parameter:

- They have to follow a '?' mark in the URL;
- They have a value associated with them

The **Params** tab lets you specify the Parameters whose value you would like to change.

Usually, the **Params** tab is used in conjunction with the Pre-request and Post-request tabs to create automatically updating values.

#### How to Use Pre- and Post-Request Processing

To use pre- and post-request processing, some amount of Javascript knowledge is needed.

|  |
| --- |
| What is the Difference Between the Two? |
| **Pre-request:** This is a code snippet normally set the context ***before*** the API request. This can be retrieving an authentication token from another API, or to change parameters to allow for more automation. |
| **Post-request:** A piece of code to apply to the data ***received from*** the API request. This code can be used to modify the received data to change how it is displayed on your screens. |

The **Pre-request** tab is where you'll input code for pre-request processing.

**Example:** For the systems that requires a dynamically generated authentication token like Toast, this can be used to call another API to retrieve the authentication token and set it to the context of the API.

For more on this example, see this article on [how to connect your Toast API](https://support.optisigns.com/hc/en-us/articles/31113088917907-How-to-use-Toast-API-data-with-OptiSigns).

The **Post-request** tab is where you'll input code for post-request processing.

**Example:** You are receiving data from your point-of-sale (POS) software API, but certain pieces of data aren't displaying the way you'd like.

Prices may display as whole numbers (i.e. 1299) instead of as a proper pricing (i.e. $12.99). For this, we'd need a piece of code to convert the whole number into a price, and have that code be extensible to any similar display errors (e.g. 1899 instead of $18.99).

![](https://support.optisigns.com/hc/article_attachments/32427362130195)

For this common example, this piece of JavaScript code should solve your issue. We can also set up the ability to map product availability at the same time.

This will fix the returned data, allowing it to display properly:

![](https://support.optisigns.com/hc/article_attachments/32427362133523)

This can also be used to make data appear as "SOLD OUT," to strike through an item if it's unavailable, or to display warnings in an inventory management system. For more on this example, see our article on [Digital Menu Boards.](https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync)

---

### Step 3 (Optional): Use Substitution Parameters from Device Attributes.

Many point-of-sale (POS) systems are licensed by store/location. It's possible to configure a single API Request with OptiSync and have it work with different locations using **substitution parameters**. Inputting these allows your screen to communicate its store or location identification information. This means a single API request can communicate different data to different stores or locations, rather than needing to make individual API requests per screen.

To get started, find the screen you wish to edit.

![](https://support.optisigns.com/hc/article_attachments/32427362139411)

Click **Advanced** **→** **More** **→** **Device Additional Attributes.**

![](https://support.optisigns.com/hc/article_attachments/32427378848019)

Two fields will show up, **Key** and **Value**.  
![firefox_KkCBvxsPKU.png](https://support.optisigns.com/hc/article_attachments/32427362146707)

- **Key** - A parameter that will be used during the API call to substitute for your store's value. This will replace part of your API URL endpoint.
- **Value** - Represents the unique code associated with the store or location you wish to pass through to your API.

In this example, we are maintaining the Clover merchantID here. The value inputted will need to be obtained on your end as it will be unique.

Now, go back to the API request config page. Substitute the merchantID in the API endpoint with the Key name you previously defined.

#### 

When the API call is triggered on the device, it will take the value from the device and substitute it at runtime. For each screen, you'll want to perform these same steps, keeping the Key name the same while changing the Value. This will allow you to push different data to different screens.

---

## How to Map API Data in Designer

In order to push data from your API to a screen, it will need to be registered as a DataSource. This allows data elements to be added to OptiSigns' Designer app, where it can be formatted and incorporated into any visual design you'd like to display.

The Designer app and templates can be used to do the formatting, and the API data source will handle the data mapping. Any text box or image element can be mapped in Designer. When you map an image element, the URL of the image will be replaced at run time.

---

### Step 1: Creating an API DataSource

To get started, find your design or create a new one in the **Files/Assets** tab.

With the design open, click **"DataSource"** in the left hand column. Then, click **"Add DataSource"** to add an API data source to the design.

![](https://support.optisigns.com/hc/article_attachments/42850937896211)

Scroll down to where it says **"API Gateway"** and click it.

![](https://support.optisigns.com/hc/article_attachments/42850937907987)

You should see this screen:

![](https://support.optisigns.com/hc/article_attachments/42850937909523)

Select the API Request created above. You'll see a screen like the one below:

![](https://support.optisigns.com/hc/article_attachments/42850937911187)

Here, you can choose what data specifically you want to add to the Design. If you want all the options, hit **"Continue"**. This screen will appear.

![](https://support.optisigns.com/hc/article_attachments/42850937917715)

**DataSource Name** is how this DataSource will appear in Designer. Name it whatever helps you identify it.

**Synchronization** lets you choose how often to sync back to your API. *Only import once* makes sense for one-time promos and the like. If this is for a longer-term asset, choose *Periodic direct access*or *Periodic background sync* depending if you need to use the data from specific device to set the context*.*

Hit **Done**, and the DataSource is created.

It should appear in the left column under **"Used in this design".**It will definitely appear in the **"Other DataSources"** section. You may need to refresh the page for it to appear.

Now, we move to step 2.

---

### Step 2: Maintain the Element Mapping

Once the API DataSource has been created, you're ready to map the data.

In Designer, open your DataSource.

![](https://support.optisigns.com/hc/article_attachments/42850953614611)

Click on it and a screen similar to this will pop up:

![](https://support.optisigns.com/hc/article_attachments/42850953615763)

Opening up any of these will display the data pulled from your API:

![](https://support.optisigns.com/hc/article_attachments/42850953617427)

By clicking on any piece of this data and dragging it onto the screen, the data will appear. You'll have the option to use the data as a Repeater or on its own.

![](https://support.optisigns.com/hc/article_attachments/42850937928467)

In this case, we want to use it on its own. For menus, a Repeater makes the most sense.

In order to check the data binding, you can click on any mapped element, then click **Settings**. You will see the **Asset Element Name** there.

![](https://support.optisigns.com/hc/article_attachments/42850937932307)

We have the item name and price from the API mapped to the design. When published on the screen, the value will be automatically replaced with the value from the API. If updates are made in the Clover POS system, the change will be reflected on the screen automatically.

![](https://support.optisigns.com/hc/article_attachments/42850937936019)

Repeat this step for all the elements that you want to map to the API data source, and save the design. Your design is ready to go.

---

## More OptiSync Use Cases

If you'd like more detail on API integration use cases, we have several additional articles. Please see:

- [Point-of-Sale Systems to build Digital Menu Boards](https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync)
- [Displaying Event Schedules](https://support.optisigns.com/hc/en-us/articles/33468569218067-How-to-Display-Dynamic-Event-Schedules-Using-OptiSync)
- [Integrating Toast API Systems](https://support.optisigns.com/hc/en-us/articles/31113088917907-How-to-use-Toast-API-data-with-OptiSigns)
- Custom RSS Feeds
- [Dynamic Data-Mapping](https://support.optisigns.com/hc/en-us/articles/4404511767571-How-to-use-Dynamic-Data-Mapping-feature-with-Google-Sheets)

---

## That's all!

This is how you integrate API data and get it published on your screen. Most importantly, with no coding!

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
