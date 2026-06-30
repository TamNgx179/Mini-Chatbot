# Display Salesforce Dashboards with MFA using Web Scripting

Article URL: https://support.optisigns.com/hc/en-us/articles/32839794222099-Display-Salesforce-Dashboards-with-MFA-using-Web-Scripting
Article ID: 32839794222099
Last Updated: 2025-09-02T20:45:08Z

#### Displaying Salesforce Dashboards on your digital screens is crucial to getting real-time data directly to who needs it. Let's go through how to set up your MFA-protected Salesforce Dashboard by using our Web Scripting app!

Things You'll Need:

- [Salesforce Dashboard](https://www.salesforce.com/)
- [Burp Suite Navigation Recorder](https://chromewebstore.google.com/detail/burp-suite-navigation-rec/anpapjclbjicacakeoggghfldppbkepg)
- Authenticator App (ex., Google Authenticator)

---

## Setting Up MFA

|  |
| --- |
| *If you don't already have MFA set up for your Salesforce account, please visit their support article: **[Multi-Factor Authentication for Salesforce Orgs.](https://help.salesforce.com/s/articleView?id=sf.security_overview_2fa.htm&type=5)*** |

Next, go to your account settings > My Personal Information > Advanced User Details

From there, click **"Connect"** on "**App Registration: One-Time Password Authenticator**"

![Salesforce account settings and setting up authenticator app](https://support.optisigns.com/hc/article_attachments/35528791304211)

When Salesforce prompts you to connect an Authenticator App, **DO NOT** immediately scan the QR code.

Click "**I Can't Scan the QR Code**".

![Salesforce setting up authenticator app. Select 'I can't scan the QR code'](https://support.optisigns.com/hc/article_attachments/35528807336979)

**Copy and paste the alphanumeric string** displayed underneath "Key". **Save this key** somewhere secure, like the Notepad app.

- This is ***necessary*** for the web scripting process later.

Next, enter that setup key in your authenticator app, then enter the verification code into Salesforce, and connect!

![Save the setup key that Salesforce provides you.](https://support.optisigns.com/hc/article_attachments/35528807340691)

**Your MFA is now set up!**

---

## Record & Set Up Your Web Scripting App

|  |
| --- |
| *You can refer to our **[How to use the Web Scripting App article](https://support.optisigns.com/hc/en-us/articles/1500012522362)** on how to download Burp Suite Navigation Recorder and record your script.* |

During the recording process, **write down the exact verification code** you inputted to log in to your account.

- This is ***necessary*** when setting up the Web Scripting app.

Once your script is recorded, Burp Suite should automatically copy it to your clipboard. You can also copy it to your clipboard by opening Burp Suite in the extension manager:

![Click 'Copy to clipboard' on Burp Suite Navigation extension to copy the script again.](https://support.optisigns.com/hc/article_attachments/35528791311507)

Log in to your OptiSigns account and open the Files/Assets page to create your asset. Click on **"Apps"** You need to:

1. Paste your script into the "**Recorded Script**" box
2. Paste the alphanumeric setup key you saved from Salesforce into "**Secret 2FA**"
3. Input the *exact* verification code you used during the login process while recording into the "**Recorded 2FA Code**" box.

![Web scripting in OptiSigns and pasting the script, setup key, and 2fa code in their respective boxes.](https://support.optisigns.com/hc/article_attachments/35528807348627)

Click **Save!**

---

Now you can [push this app to your screen,](https://support.optisigns.com/hc/en-us/articles/18988049363859) [add it to a split screen app](https://support.optisigns.com/hc/en-us/articles/360026559573), and more!

![A salesforce dashboard displayed on a split screen app to show the dashboard, weather, and important news on your TV.](https://support.optisigns.com/hc/article_attachments/35377393852691)

If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at support@optisigns.com
