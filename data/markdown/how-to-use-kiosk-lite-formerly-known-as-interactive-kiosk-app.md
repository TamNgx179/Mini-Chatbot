# How to use Kiosk Lite (formerly known as Interactive Kiosk app)

Article URL: https://support.optisigns.com/hc/en-us/articles/360053993934-How-to-use-Kiosk-Lite-formerly-known-as-Interactive-Kiosk-app
Article ID: 360053993934
Last Updated: 2025-09-04T14:30:55Z

Kiosk Lite app, also formerly known as the Interactive Kiosk app, allows you to let your screens play a set of contents, but when the user taps or clicks on the screens, a website URL will be loaded, and the customer can interact with it.

This is useful for the kiosk use case, where a standard advertising, or promotion playlist can be played, and when the customer touches the screen, they can interact with a website to enter their information, or browse catalogs, etc.

This feature is supported on iOS, Androids, Windows, Linux, MacOS, Raspberry Pi, ChromeOS, and BrightSigns devices. In addition, the Kiosk Lite app is only available through our Engage and Enterprise plans.

## **Let's jump in and get started:**

First, you will need to have your screens set up and paired. For more information on how to do that, click [here](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv).

Then log on to our portal: <http://app.optisigns.com/>

Go to Engage page

Click on "New App"

![](https://support.optisigns.com/hc/article_attachments/24980788231571)

Select Touch Screen Kiosks → Select App

![](https://support.optisigns.com/hc/article_attachments/24981016303635)

Select Kiosk Lite → Build

![](https://support.optisigns.com/hc/article_attachments/24980788262419)

Enter your kiosk information:

![](https://support.optisigns.com/hc/article_attachments/27028402258707)

- Name: Name of your Kiosk Lite App, this is the name of the wall in your asset list. It will **not** be displayed on your screens.
- Default Content Type: Choose between Asset or Playlist as your content type.
- Select Asset/Playlist: Pick the asset or playlist you want to play as your standard content.
- Kiosk URL: The URL of the web page you want to load when the customer touches the screen.
- Timeout: When the screen has been inactive for X seconds on the webpage, the devices will close the web page and display the default content.
- Preload Kiosk URL: If checked, the app will preload the URL in the background, and show it to customers instantly when the customer touches the screen. This is good for user experience, but if you have animation or dynamic content on your web page, you may want to disable this.
- Show Touch Here Icon: Show the Touch Here icon blinking on the screen. This is useful to grab customer's attention and invite them to interact with the kiosk.

- Customize Touch Here Icon:  
  - Touch Here Icon: The default is a pointer hand icon, but you can upload your custom icon.
  - Touch Here Icon Size: Set how big the size of the touch screen icon should be.
  - Touch Here Icon Location: Set where you want the touch screen. You can set it to Top Left, Ton Right, Bottom Left, Bottom Right, or show up randomly on the screen.
  - Touch Here Icon Blinking Rate: Set how fast you want the icon to blink on the screen

- Close & Nav Bar Styler:
  - Icon Position: Adjust the placement of icons within the bar to optimize visibility and access: none, top left, top center, top right, bottom left, bottom center, bottom right
  - Icon Style: Select from a variety of icon designs to match your kiosk's aesthetic: Default, Outline, Solid, or Thin
  - Icon Color: Customize the color of your icons to complement your brand or theme.
  - Icon Size: Scale the icons to the ideal size for easy recognition and usability.
  - Show Back/Forward: Enable or disable back and forward navigation options for user convenience.
    - Navigation Bar Background Color: If Show Back/Forward is turned on, you can customize the color for the navigation bar background to align with your design scheme.
    - Navigation Bar Opacity: If Show Back/Forward is turned on, you can adjust the transparency of the navigation bar for subtle or bold visibility.

If you want to set these options as your default for future use, you can learn how to do that on our "[How to Change Close & Nav Bar Styler Preferences](https://support.optisigns.com/hc/en-us/articles/28115946505107-How-to-Change-Close-Nav-Bar-Styler-Preferences)" page.

![chrome_wUCoFrbwyJ.png](https://support.optisigns.com/hc/article_attachments/28111518265619)

Here's an example of the Close & Nav Bar Styler:

![ApplicationFrameHost_0xbJVUctOv.png](https://support.optisigns.com/hc/article_attachments/28111518282899)

- Advanced setting: Returned URL: If you are showing a lead capture form, and when the user finishes the app it automatically returns to playing the standard content. You can paste the URL where the user is redirected to after they submit the form here. (i.e. <https://www.example.com/form123/thank-you>) then the app detects this URL, and it will return to playing standard content.

Click **Save**.

## **That's all! Congratulation!**

You have created your Kiosk Lite app.

**Note**: Integrating the Kiosk Lite app into a Playlist may not offer an optimal user experience, as the content may inadvertently advance to the next item on the Playlist before completing their interaction with the touch screen. For a more seamless user experience, we recommend placing your playlist within the dedicated Kiosk Lite app.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
