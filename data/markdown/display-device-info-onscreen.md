# Display Device Info Onscreen

Article URL: https://support.optisigns.com/hc/en-us/articles/27070013297427-Display-Device-Info-Onscreen
Article ID: 27070013297427
Last Updated: 2025-09-04T15:08:40Z

### In this article, we will guide you through the process for displaying your device's information on screen.

- [Before You Begin](#Begin)
- [Step 1: Create Designer Asset](#Step1)
- [Step 2: Add a Device Data DataSource to the Asset and Map It](#Step2)
  - [Optional: Creating Additional Device Attributes](#Optional)
- [Step 3: Assign the Asset to Screens](#Step3)

Displaying your device's information onscreen has various advantages. Information like the screen name, assigned contents, and more can be helpful when:

- Managing a large network.
- Many screens are placed together in the same location.
- Running deployment or troubleshooting.

Device information can be easily displayed using the OptiSigns Dynamic Data Mapping feature. By using this, you'll only need to create a single asset, which can be used on any device to display that specific device's information. Let's get started.

---

## Before You Begin

Dynamic Data Mapping is available to **Pro Plus** subscribers or above.

Setting up a dynamic Device Info asset consists of three steps:

1. Create a designer asset that fits your needs
2. Enable the data source for device info and maintain the mapping.
3. Assign the asset to your screen.

---

## Step 1: Create a Designer Asset

To begin, go to the **Files/Assets** tab in the OptiSigns web portal. Click **Apps**.

![firefox_k4Purluovg.jpg](https://support.optisigns.com/hc/article_attachments/38883675197587)

Now, open the **Designer** app:

![firefox_Bo3ccQ4spb.jpg](https://support.optisigns.com/hc/article_attachments/38883666973459)

Once you've entered the Designer app, you'll need to create your Designer asset. This can display any way you'd like. If you wish to reuse it and apply it to all your screens, you may need to make this asset a generic size for placing into a [**Split Screen zone**](https://support.optisigns.com/hc/en-us/articles/360026559573-How-to-Create-and-Use-the-Split-Screen-App).

In this example, we will set the canvas size to **585 x 315** in order to best fit a Split Screen zone. We'll create some placeholder text here to replace with our dynamic data in the next step:

![](https://support.optisigns.com/hc/article_attachments/42859076732691)

---

## Step 2: Add a Device Metadata DataSource to the Asset and Map It

Next, we'll need to add a Device Metadata DataSource to retrieve device data. Click the **DataSource** tab on the left side of the screen, then hit **Add DataSource** at the top of the menu:

![](https://support.optisigns.com/hc/article_attachments/42859068384403)

A screen with numerous options will pop up. Scroll down until you see **Device Metadata** under Adv. DataSources, then click it.

![](https://support.optisigns.com/hc/article_attachments/42859076737427)

You'll be taken back to the DataSource menu, but there will be a new option - **Device Data (default)**. Click it.

![](https://support.optisigns.com/hc/article_attachments/42859068388243)

You'll be presented with data that looks something like this:

![](https://support.optisigns.com/hc/article_attachments/42859068390675)

By mapping these values to your asset, the specific screen data will be pulled, and the values in red will be replaced with values ***specific to your screen***. In order to map them, simply click and drag the value into the field where you want them to display.

You can also display custom device attributes, but this is not necessary. If the default data is enough for you, skip to [**step 3**](#Step3).

### Optional: Setting Device Attributes

In some cases, you may wish to configure a custom attribute on your device and have that displayed.

In the example above, we've made an "assetId" field, which is a custom attribute defined on the screen level. These attributes can denote anything - from the asset being displayed to the shop the device is used in. It's all up to you.

To create this, navigate to your **Screens** tab. Find the screen whose attributes you wish to change, then hit **Edit**. You'll be taken to the **Edit Screen** menu. Hit **Advanced →** **More → Device additional attributes**.

![firefox_hdXgPSnyE2.jpg](https://support.optisigns.com/hc/article_attachments/38883666992659)

![firefox_eigWT4aT3p.jpg](https://support.optisigns.com/hc/article_attachments/38883666993555)

This will bring up the **Device additional attributes** screen. Here, to create a new attribute, click **New Attribute:**

![firefox_Z4jbp2DWQv.jpg](https://support.optisigns.com/hc/article_attachments/38883675214355)

Now, fill in the desired attributes with the appropriate data, then hit **Update**:

![firefox_7ZsHFOeUuN.jpg](https://support.optisigns.com/hc/article_attachments/38883666999059)

These additional attributes will now map to a Device Metadata Datasource. You will need to configure these additional attributes per screen in order for them to display.

---

## Step 3: Assign the Asset to Screen

Once the mapping is complete, you can simply assign it to a screen. The asset will display information specific to the screen it's been assigned.

For the above example, let's assign it to a screen called "Demo Laptop". We've configured the "assetId" through Device Additional Attributes to be 123, and the rest of the data has been mapped appropriately. It should display like so:

![mceclip0(1).jpg](https://support.optisigns.com/hc/article_attachments/38884919962643)

If we were to assign it to another screen, these values would change. This makes the Device Info asset highly valuable as a troubleshooting tool.

**That's all!**

This is how you can display device info on the screen using device data mapping feature.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
