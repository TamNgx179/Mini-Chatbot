# How to Install a Root Certificate and Display an Internal Website on Screens

Article URL: https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens
Article ID: 35184720136595
Last Updated: 2025-09-04T16:54:34Z

### In this article, we will explain how to install a root certificate on your devices to set up an internal website for use with OptiSigns.

- [Installing a Root Certificate on an OptiSigns Gen 3 Pro Player](#ProPlayer)
- [Installing a Root Certificate on a Linux/Ubuntu Device](#Ubuntu)
- [Installing a Root Certificate on a Windows Device](#Windows)
  - [Open the Microsoft Management Console (MMC)](#MMC)
  - [Add the Certificates Snap-in](#Snap-In)
  - [Import the Certificate](#Import)
  - [Verify the Installation](#Verify)
  - [Command Line Installation](#Command1)
- [Installing a Root Certificate on a MacOS Device](#MacOS)  
  - [Install Certificate](#Install)
  - [Command Line Installation](#Command2)
- [Installing a Root Certificate on Chrome-Based Web Browsers](#Chrome)
- [Setting Up an Internal Website for Use on OptiSigns Using the Website App](#InternalWebsite)
  - [Using Web Scripting to Bypass Logins](#WebScripting)

OptiSigns digital signage software is an extremely valuable tool for internal communication, capable of displaying internal memos, communications, and announcements across numerous locations and offices. Messaging can be tailored to specific audiences, scheduled, and automatically synced to data sources.

With all these capabilities, it stands to reason that some want to incorporate OptiSigns into their intranet, or internal website. These can be displayed on your screens using the OptiSigns Website app, or Advanced Website app in some cases.

However, in order to do this, you’ll need a trusted, self-signed root certificate installed on the platform you choose to run it on. Here, we’ll show you how to get that installed.

Please note that you’ll need to obtain a trusted certificate yourself. This will need to be some sort of key, usually denoted by a **.pem** file extension.

In this article, we will walk you through two main steps:

1. Installing a root certificate on your device of choice (OptiSigns Pro Player, Ubuntu, Windows, MacOS, or Chrome browser)
2. Configuring a Website app to display your internal website

|  |
| --- |
| **NOTE** |
| Before you start, make sure you’re connected to the same network as the server you’re trying to access. |

|  |
| --- |
| **Please note that Android devices are not supported at this time.** |

---

## Installing a Root Certificate on an OptiSigns Gen3 Pro Player

In order to get your root certificate onto an OptiSigns Pro Digital Signage Player, you’ll need to manually add it. Find where your certificate is stored, then download it to a USB or MicroSD card. Plug the card into the Pro Player.

|  |
| --- |
| **IMPORTANT** |
| For installation on a Gen 3 Pro Player, your certificate must have a **.crt** extension. However, it is important that this certificate is signed and contains your public key. These are usually generated as **.pem** files. You’ll need to rename your certificate (.pem) file and change its extension to **.crt** for your internal website to properly display. |

Now, open your OptiSigns player menu. Go to **About → Advanced Settings**.

**![](https://support.optisigns.com/hc/article_attachments/35184705322515)**

Here, you’ll see a field called **Certificate File**.

![](https://support.optisigns.com/hc/article_attachments/35184705339539)

Simply locate your certificate on your USB or MicroSD card and select it. The certificate will automatically be downloaded to the appropriate location. This will allow your OptiSigns player to display your internal website.

---

## Installing a Root Certificate on OptiSigns Gen 2 Pro Players and Linux/Ubuntu Devices

To install a root certificate on a Linux or Ubuntu device, you’ll need to make heavy use of the **Terminal.**

To begin, take your trusted, signed certificate (.pem file) and place it in the /usr/share/ca-certificates folder.

![](https://support.optisigns.com/hc/article_attachments/35184720058515)

|  |
| --- |
| **NOTE** |
| You will need to rename your **.pem** file to make it a **.crt** file, or else this will not work. |

After the certificate has been moved and renamed, you’ll need to refresh the installed certificates and hashes. Open your **Terminal** and type in this command:

```
sudo update-ca-certificates
```

Once this command is executed, it should say that it has installed 1 (or more) new certificate.

![](https://support.optisigns.com/hc/article_attachments/35184720067475)

This means the certificate has been added to the operating system and signed certificates will be trusted.

Now, you’ll want to install the certificate in the Chromium store using this command:

```
certutil -A -n "ROOT-CA" -t "TCu,Cu,Tu" -i /usr/share/ca-certificates/[name-of-cert].crt -d sql:/home/[user]/.pki/nssdb
```

The Linux-based OptiSigns app uses Chromium, so this will allow the certificate to pass through the OptiSigns app.

Now reboot your device.

Congratulations! You’ve successfully installed a root certificate on Ubuntu.

---

## Installing a Root Certificate on a Windows Device

Broadly, there are four major steps to installing a root certificate locally on a Windows device:

1. Open the Microsoft Management Console (MMC)
2. Add the Certificates Snap-In
3. Import the Certificate
4. Verify the Installation

These same steps can be performed quickly using the Windows Terminal, if you’re so inclined.

Be cautious when installing root certificates, especially self-signed ones. Only install certificates from sources you trust completely.

|  |
| --- |
| **NOTE** |
| You need administrator privileges to install certificates in the Trusted Root Certification Authorities store. |

### Open the Microsoft Management Console (MMC)

The first step is opening the Microsoft Management Console (MMC), which is a framework for managing Windows components.

To do this, click **Start,** type **mmc** into the Search bar, then press **Enter**.

![](https://support.optisigns.com/hc/article_attachments/35184705345939)

### Add the Certificates Snap-In

With the MMC open, go to **File → Add/Remove Snap-In**.

![](https://support.optisigns.com/hc/article_attachments/35184705348371)

In the “Available snap-ins” list, select **Certificates** and click **Add.**

![](https://support.optisigns.com/hc/article_attachments/35184720078227)

Choose **Computer account** to manage certificates for the local computer. Click **Next**.

![](https://support.optisigns.com/hc/article_attachments/35184705352851)

Next, click **Local computer** and click **Finish**.

![](https://support.optisigns.com/hc/article_attachments/35184705355155)

Click **OK** to close the “Add or Remove Snap-ins” dialog.

### Import the Certificate

Now **Certificates (Local Computer)** will appear as an option in your MMC. To continue, exp[and the **Certificates (Local Computer)** option within the right pane of the console. Then, expand **Trusted Root Certification Authorities**.

![](https://support.optisigns.com/hc/article_attachments/35184720086931)

Right-click on the **Certificates** folder and select **All Tasks → Import**.

**![](https://support.optisigns.com/hc/article_attachments/35184720091795)**

This will open the Certificate Import Wizard. Click **Next** to get started.

Now, click **Browse.** Locate your self-signed certificate and select it. This should be a .pem file. You may need to expand the file name options to **All Files** to see it.

![](https://support.optisigns.com/hc/article_attachments/35184705362323)

Select the file and click **Open → Next.**

Select **Place all certificates in the following store.** Ensure that **Trusted Root Certification Authorities** is selected, then click **Next.**

**![](https://support.optisigns.com/hc/article_attachments/35184705364115)**

Now you’ll be asked to confirm whether you want to complete the import. As long as you trust the certificate, agree to it by hitting **Finish**.

**![](https://support.optisigns.com/hc/article_attachments/35184705368339)**

### Verify the Installation

Close the MMC.

Open a web browser and try accessing the local host domain. If the certificate is installed correctly, you should no longer see the security warning. However, because it's a self-signed root certificate, you might still see a warning indicating that the website's identity cannot be verified.

If you encounter any issues, double-check the file paths, file names, and the output of the Certificate Import Wizard for any error messages.

### Command Line Installation

You can also use the **Terminal** to directly install the certificate. Simply open up the Terminal app with Administrator privileges after searching for it on your Start bar, and input the following command:

```
certutil –addstore –f "Root" “C:\path\to\your_certificate_file”
```

This will automatically install the certificate to the Trusted Root Certificates folder and you should be able to access the host domain in the same way as above.

---

## Installing a Root Certificate on a MacOS Device

To prepare for the installation, make sure your device is connected to the same network of host servers you plan to use. Also, make sure your certificate is in a folder (the Download folder will work) on the device installing the certificates.

### Install Certificate

To begin, open **Keychain Access**. This is normally located in the “Other” folder in the launchpad.

![](https://support.optisigns.com/hc/article_attachments/35184720101907)

Select the System tab within the menu on the left. If you see a padlock icon next to the System folder, right click to unlock and enter the system password.

![](https://support.optisigns.com/hc/article_attachments/35184720103571)

![](https://support.optisigns.com/hc/article_attachments/35184720107027)

Open the folder where your certificate is stored. Drag and drop the certificate into the system folder in Keychain Access. If a red x is displayed next to the certificate like below, keep following along. Otherwise, you’re done.

![](https://support.optisigns.com/hc/article_attachments/35184705380883)

Right click the certificate and select “get info”

![](https://support.optisigns.com/hc/article_attachments/35184705382291)

Select “Trust”.

![](https://support.optisigns.com/hc/article_attachments/35184720114579)

Select “Always Trust”. This means your computer will always trust this certificate to keep your connection secure.

![](https://support.optisigns.com/hc/article_attachments/35184705386771)

Exit and you will be prompted with entering password. Enter the system password.

Your certificate is now installed. You will now be able to access the local website.

### Command Line Installation

On MacOS, you can also use the Terminal to directly install the Certificate. Simply type in these commands:

**Use the following command to add a certificate:**

```
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain “new-root-certificate”
```

**Use the following command to remove a certificate:**

```
sudo security delete-certificate -c "name of existing certificate"
```

---

## Installing a Root Certificate on Chrome-Based Web Browsers

Depending on the operating system, Chrome will use the system-wide certificates (such as the ones installed above) or its own certificates. If you are having trouble getting a system-wide certificate to work for your internal website, you may wish to try directly installing a root certificate to Chrome (or any Chromium browser) directly.

To begin, open the **Settings** tab in the Chrome browser.

![](https://support.optisigns.com/hc/article_attachments/35184720118803)

Next, click **Privacy and security** **→ Security → Manage Certificates**

**![](https://support.optisigns.com/hc/article_attachments/35184705392531)**

This will open the Certificates manager. You’ll need to add your internal website certificate as an authority. Here, click the **Trusted Root Certification Authorities** tab, then click **Import**.

![](https://support.optisigns.com/hc/article_attachments/35184720125715)

This will open the Certificate Import Wizard. Click **Browse** and locate the certificate necessary for your internal website. Then, click **Next**.

**![](https://support.optisigns.com/hc/article_attachments/35184720127635)**

On the next screen, **Place all certificates in the following store** and make sure it’s “Trusted Root Certification Authorities”. Then hit **Next**.

**![](https://support.optisigns.com/hc/article_attachments/35184705364115)**

Now you’ll be asked to confirm whether you want to complete the import. As long as you trust the certificate, agree to it by hitting **Finish**.

**![](https://support.optisigns.com/hc/article_attachments/35184705368339)**

Congratulations, you’ve installed your root certificate on your Chrome browser.

---

## Setting an Internal Website Up for Use on OptiSigns Using the Website App

The OptiSigns Website app allows you to display an internal website on your screens once a valid private certificate (.pem file) has been installed on your device.

To set it up, navigate to **Files/Assets** in your OptiSigns portal. Find the **Website** app.

![](https://support.optisigns.com/hc/article_attachments/35184705404947)

Enter the **URL** of your webpage here. The Name field is irrelevant to the app’s function and will only make the asset easier to find in OptiSigns.

|  |
| --- |
| **NOTE** |
| If your internal website is large and complex, you can also display it using the **Advanced Website** app. If you’re having trouble displaying it on the basic Website app, create an Advanced Website asset and try again. |

Once the Website asset is created, it can be assigned to a screen.

### Using Web Scripting to Bypass Logins

Many internal websites require logins to work. In this case, the Website app will not be sufficient to access them on the OptiSigns app. In this case, we recommend our Web Scripting app.

Follow our complete [guide to using the Web Scripting app](https://support.optisigns.com/hc/en-us/articles/1500012522362-How-to-use-the-Web-Scripting-App) to set that up.

### That’s all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
