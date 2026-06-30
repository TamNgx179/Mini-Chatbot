# How to Set Up a Power BI Service Principal for Use in OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-Power-BI-Service-Principal-for-Use-in-OptiSigns
Article ID: 32860569148819
Last Updated: 2026-03-17T22:32:17Z

### In this article, we will walk you through the process of setting up a service principal for Power BI in Microsoft Azure, and connecting it to OptiSigns.

- [Creating an Entra App in Microsoft Azure](#Create)
- [Enable Power BI Service Admin Settings](#Enable)
  - [Add the Service Principal to a Workspace](#Add)
- [Authenticating OptiSigns via Service Principal](#Auth)
- [Getting Power BI onto a Screen](#Get)

Using a Power BI service principal with app registration is a preferred option for companies with strict information security rules that don't want to use individual user accounts for Power BI integration.

This reduces headaches in situations when:

- There is a position or permission change of a user and authentication needs to be performed again by a different user.
- A prolonged authentication token period cannot be set for individual users, and you will need to reauthorize and refresh the token every couple of months.

Using a Power BI service principal, the authentication tokens are associated with a registered app instead of a user. This allows you to set a longer validity time for the authentication token and avoids more frequent re-authorization. Using service principal with App registration for Power BI integration is supported well with OptiSigns.

|  |
| --- |
| **NOTE:** This feature is only available to customers on an **Enterprise** plan. |

---

## Create an Entra App in Microsoft Azure

An Entra app will be responsible for handling identity and access management for your service principal. In order to create one, you’ll need to login to Microsoft Azure with a viable Microsoft account.

Once at the Azure portal, search for **“app registrations,”** then select **App Registrations** from the list that appears:

![app registration instructions in microsoft azure](https://support.optisigns.com/hc/article_attachments/32860610406547)

Create a **New Registration**.

![how to create a new registration in microsoft azure](https://support.optisigns.com/hc/article_attachments/32860569069459)

On this screen, type a name for the app, then leave the other settings as default. These can be changed or altered at any time.

![instructions on registering an application in microsoft azure](https://support.optisigns.com/hc/article_attachments/32860610418707)

Once done, hit **Register.**

---

## Enable Power BI Service Admin Settings

Follow this link to the [PowerBI Admin Portal](https://app.powerbi.com/admin-portal/capacities?experience=power-bi).

Once there, click **Tenant Settings**. Then, scroll down to **Developer Settings**.

![finding developer settings in tenant settings within powerbi admin portal](https://support.optisigns.com/hc/article_attachments/32860610420627)

Enable the **Embed Content in Apps Settings**, as below:

![how to enable embed content in apps](https://support.optisigns.com/hc/article_attachments/32860610421779)

In this example, we’ve set this embed to apply permissions to the entire organization. However, you can restrict access to specific security groups based on your needs. These security settings can be changed as per your requirements.

Next, **Enable Service principals can create workspaces, connections, and deployment pipelines** and **Enable Service Principals can call Fabric public APIs**, as below:

![image (28)(1).png](https://support.optisigns.com/hc/article_attachments/42225175622675)

Like before, we’ve applied these to the entire organization. Just like the last step, you can restrict access to specific security groups based on your needs.

### Add the Service Principal to a Workspace

Now we need to assign service principal access to the workspaces you want to show in your PowerBI reports.

In the admin portal, click **Workspaces**. You’ll want to go to the workspace you want to assign service principal access to. Click the workspace, then hit **Access**.

![how to grant service principal access powerbi](https://support.optisigns.com/hc/article_attachments/32860610425107)

Add the service principal you created in the last step as a member of the workspace.

![how to add service principal as a member of powerbi workspace](https://support.optisigns.com/hc/article_attachments/32860569093139)

---

## Authenticating OptiSigns via Service Principal

In order to authenticate your Power BI on OptiSigns via service principal, you’ll need four pieces of information:

1. Name of the service principal
2. Application (client) ID
3. Directory (tenant) ID
4. Application (client) secret

Since we’ve already created an Entra app in Azure, we already have access to the first three pieces of information. These can be found under **App Registrations** back in Azure.

![where to find app registration information in microsoft azure](https://support.optisigns.com/hc/article_attachments/32860569095571)

In this example, the values have been blurred, but on your Azure portal, these should be visible.

The only piece of information you won’t have is the client secret. To get that, click **Manage → Certificates & Secrets → Client Secrets → New Client Secret**

**![how to create new client secret in microsoft azure](https://support.optisigns.com/hc/article_attachments/32860569099411)**

Next, set the **Description** and **Expiry**, then click **Add**.

![how to add a client secret](https://support.optisigns.com/hc/article_attachments/32860569100947)

The **Value** present is the last piece of information you need.

Now, head into the OptiSigns app. Click your **Profile name → More → Integrations.**

![where to find integrations tab in optisigns](https://support.optisigns.com/hc/article_attachments/32860610434451)

A screen like the one below will appear. Click **Add Azure Service Principal.**

![how to add service principal in optisigns](https://support.optisigns.com/hc/article_attachments/32860569109011)

When the popup appears, collect the information mentioned above from Microsoft Azure and input it into OptiSigns. The values match up like this:

![inputting all the powerbi service principal information into optisigns](https://support.optisigns.com/hc/article_attachments/32860610442771)

Once all the information is input correctly, hit **Save**. Now your Service Principal is saved to the OptiSigns portal.

---

## Getting Power BI onto a Screen

Now we’ll need to configure your Power BI asset in OptiSigns for use with your screens.

In the OptiSigns portal, go to **Files/Assets → Apps → Power BI**

**![how to find powerbi app in optisigns](https://support.optisigns.com/hc/article_attachments/32860569116691)**

Check **Use Service Principal** and select the service principal you set up in the last step, or whichever service principal you want to use.

|  |
| --- |
| **NOTE:** Using a service principal, the Power BI Dashboard URL link needs to include the actual **workspace (group)** ID instead of me. |

**![powerbi app information in optisigns](https://support.optisigns.com/hc/article_attachments/32860610472339)**

Finally, input the URL of whatever report you want to share. Name the app whatever you like, then hit **Preview** to view your report.

**![preview of powerbi app running in optisigns](https://support.optisigns.com/hc/article_attachments/32860610476307)**

Hit **Save**, then this Power BI app will exist as an asset. It can be pushed to any of your screens individually, scheduled, or added to a Playlist.

### **That’s all!**

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
