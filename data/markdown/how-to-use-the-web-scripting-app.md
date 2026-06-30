# How to use the Web Scripting App

Article URL: https://support.optisigns.com/hc/en-us/articles/1500012522362-How-to-use-the-Web-Scripting-App
Article ID: 1500012522362
Last Updated: 2026-05-14T16:05:37Z

### Web Scripting is an advanced feature for OptiSigns' Pro Plus subscribers or higher, enabling users to automate website navigation and form entries without any coding. This guide will walk you through recording your script, creating Web Scripting assets in OptiSigns, and using them securely on your screens.

**In this article**

- [What is Web Scripting?](#What)
- [Record Your Script (no 2FA)](#Record)
- [Record Your Script (2FA Enabled)](#2FA)
- [Create Web Scripting Asset in OptiSigns](#Create)
- [Using It on Your Screens](#Using)
- [Web Scripting Security Features](#SecurityFeatures)

---

## What is Web Scripting?

Web Scripting is a feature that allows users to automate navigation and form entry on websites without any coding. This tool records user actions, such as entering usernames and passwords, navigating to specific pages, handling pop-ups, running your own JavaScript and more on a website, and then encrypts the recorded script for secure execution on designated devices.

OptiSigns encrypts all the scripts and your password entered with our own private keys.

- This will ensure your data/password is safe as soon as it left your browsers and only get decrypted at device level before the fields are entered.

We also provide Zero Knowledge encryption method so that you can protect your script with your own Master Password. *You can read more at the end of this article.*

If your dashboard requires login with the 2FA, OptiSigns supports the 2FA in the Web Scripting app. You can read more [here](https://support.optisigns.com/hc/en-us/articles/19145077187859).

**Let's jump in and get started!**

|  |
| --- |
| **NOTE** |
| Web Scripting is not supported on:   - Samsung SSSP smart TVs - LG WebOS smart TVs - Apple TV devices |

---

## **Record Your Script**

In this article, we will show you how to use a tool called Burp Suite Navigation Recorder. You can use other tools if that can generate similar scripts that works too. We recommend Burp Suite because it's a reputable tool used by many companies, including the Fortune 500.

**1. You need to install Burp Suite Navigation Recorder.**

Open **Chrome Browser**.

Go to Chrome Web Store: <https://chrome.google.com/webstore/category/extensions>

Search for: "**Burp Suite Navigation Recorder**".

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/1500019933121)

Click on it.

Then click **Add to Chrome.**

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/1500019933141)

Burp Suite Navigation Recorder is installed

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/1500019660122)

Click on the **Navigation Recorder Icon.**

Then click **Open Settings** to finish set up.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/1500019660142)

Scroll down and click **"Allow in Incognito".**

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/1500019660162)

Close this tab.

Now, if you click on the Navigation Recorder icon again, you will have option to Start Recording.

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/1500019933161)

**2. Record your Script**

From the Navigation Recorder extension pop out like in above screenshot, click **Start Recording.**

It will open an **Chrome Incognito window**.  
You can put in the URL of the website or page you want to start with.  
Then fill out the forms. (such as, entering your username, password and click Login)

|  |
| --- |
| **Important Notes to Follow to Reduce Issues Later!** |
| **Always start with the destination URL** (The URL of the page you want to display). Let the website handle the redirection once you fill out the login information. |
| **Always click the Login button,** instead of Enter. |
| **Correctly enter your fields in 1 attempt!** Type slow and carefully. Don't use backspaces or arrows keys to modify. If you mess up, please restart this step from the beginning. |

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/1500019660182)

You can click around, navigate to certain page, position on page etc.

Once you are done,  click on the **Navigation Recorder Extension icon** and click **Stop Recording.**

This will close the Incognito window that you are working on.

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/1500019933181)

Go back to Chrome, click **Navigation Recorder icon.**  
Click "**Copy to Clipboard**". This will copy your script to clipboard.  
Now you are ready to put in use in OptiSigns.

![mceclip8.png](https://support.optisigns.com/hc/article_attachments/1500019660322)

---

## **Record Your Script (2FA Enabled)**

If 2FA is enabled on your login, you'll need to obtain a **Secret Key**.

To get this, click the "I Can't Scan the QR Code" button on your authenticator:

![](/attachments/token/xOjvcQdIqA9avnfjpzeOZVRqG/?name=image.png)

It will provide you with a Secret Key:

![](/attachments/token/0MBnE1wGrWf20KsUlRNDpncuK/?name=image.png)

Copy this Secret Key for use later, then finish the 2FA process.

Now, record the script as described in [the above step](#Record).

After this step, you should have:

- 2FA Secret Key
- 2FA Code

Now you're ready to create a Web Scripting Asset.

---

## **Create Web Scripting Asset in OptiSigns**

Log in to OptiSigns <https://app.optisigns.com/>

Click **File/Assets**

Click **Apps** and select **Web Scripting.**

![](https://support.optisigns.com/hc/article_attachments/51710297906323)

Enter the information for your Web Scripting asset:

![](https://support.optisigns.com/hc/article_attachments/51710297909011)

- **Name:** Name of your asset your asset list. It will **not** be displayed on your screens.
- **Master Password:** By default, OptiSigns will encrypt the whole script with OptiSigns private key to protect your script, especially username, password in the script. You can add another protection layer by entering a Master Password. If you enter Master Password here, at each device, you will need to enter that Master Password one time in OptiSigns app so it can decrypt the content.
- **Recorded Script:** Paste the script recorded by the Navigation Recorder here. You can take notice to the script, it's actually not very complicated, you can make some minor changes if you need to.
- **Scripts Injection:** Allows you to add specific scripts into your web script.
- **Block third-party cookies:** Has the web script block third-party cookies.

  ![web scripting app section 2](https://support.optisigns.com/hc/article_attachments/51710297911443)
- **Secret 2FA:** This is the Secret Key mentioned in the 2FA section. Only needed if your login requires 2FA.
- **Recorded 2FA Code:** If your login requires 2FA, this is where you input the code you received. Paired with the Secret Key, this keeps your 2FA channel open for this asset to use repeatedly.
- **Delay Execute 2FA JavaScript:** Delays execution of JavaScript elements on the 2FA element by a set amount of time, measured in seconds.
- **Delay Executing JavaScript:** Delays execution of JavaScript elements on the page by a set amount of time, measured in seconds.

---

## **Deploying Your Web-Scripting Asset on Your Screens**

Once created, the Web Scripting asset can be used in by itself or in Playlists, Schedules, or SplitScreen zones just like any other assets.

If you don't use Master Password, device will use OptiSigns private key to decrypt and execute, so no additional action is needed on the devices.

If you choose to use Master Password and our Zero Knowledge Encryption framework, you will have to enter your Master Password at each device

- This only needs to be done once on each device and can be used to decrypt all Scripting Assets. (Of course, you have to use the same Master Password to encrypt them).

---

## **Web Scripting Security Features**

When anyone other than the creator of a Web Scripting asset looks at it, it will look like this:

![web scripting security other owner](https://support.optisigns.com/hc/article_attachments/51710297912979)

Sensitive information will be hidden, and the **Override** button must be hit before the Recorded Script or Injection can be altered. There is no way for any non-owner to actually see what the script says.

If a **Master Password** is enabled, the owner will have to enter a password before the script is revealed.

**Here's how the encryption flow works:**

![mceclip12.png](https://support.optisigns.com/hc/article_attachments/1500019937601)

If you want to add additional security by utilizing a Master Password and our Zero Knowledge Encryption framework you will have to enter your Master Password when:

- Creating/editing assets
- One time at each devices, so it will know how to decrypt

Your script is encrypted at your browser, and transfer securely using HTTPS/SSL during transits and stored on our servers.  
It then sends securely to devices, and decrypted at device level right before executing on the target website.

### **That's all!**

Congratulations, you have created Web Scripting assets! Now you can automatically log in to gated websites and navigate to pages as needed.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
