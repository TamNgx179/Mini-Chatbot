# How to set up SAML 2.0 with OptiSigns and Google Workspace

Article URL: https://support.optisigns.com/hc/en-us/articles/4407493404307-How-to-set-up-SAML-2-0-with-OptiSigns-and-Google-Workspace
Article ID: 4407493404307
Last Updated: 2025-09-04T15:06:32Z

With Pro Plus and Enterprise plan, you can configure SAML 2.0 with OptiSigns via Google Workspace. The Google Workspace will be acting as the IDP (Identify Provider), and OptiSigns will be working as the SP(Service Provider).

### **Set up OptiSigns & Google Workspace:**

**First you need to do some set up in OptiSigns:**

If you don't have a sub domain yet, you can set up one by going to:  
<https://app.optisigns.com/app/s/branding-settings>

Fill in subdomain field and click Activate. After that you can use this sub domain for "  
You can also map your own domain like digitalsigns.yourcompany.com by following this [article](https://support.optisigns.com/hc/en-us/articles/1500000480302).

This will be the URL that you can share with your users so they can log in to use the app, once integration has set up. In our example we will use <https://advanced.optisigns.net/>

![mceclip13.png](https://support.optisigns.com/hc/article_attachments/21287201525907)

Next, go to the SAML Single Sign On setting page:

<https://app.optisigns.com/app/s/saml-settings>

Click Enable SAML SSO.

The settings are:

- Enable Username & Password login: Allow users to also log in with username/password. It’s recommended to disable it once the integration is all done. As Admin/Owner, it's recommended that you keep at least 1 account with a password log in, in case there are issues, you can always log back in from app.optisigns.com to reconfigure.
- Enable User Creation: If users are authenticated, but do not exist in OptiSigns, they will be created in OptiSigns. You should enable this, because you likely already assign/approve users/groups to use OptiSigns, unless for some reason you want to be very strict and want to review roles of users before they can start using OptiSigns.
- Enable User Override: Every time a user logs in, if their group assignment have changed on SAML, OptiSigns will update, override new profile settings.
- Note the "Single Sign On URL" and "Audience URI (SP Entity ID) URL", you will need this to use in Google Workspace later.

![](https://support.optisigns.com/hc/article_attachments/21286640961939)

**Next, add OptiSigns as an App in your Google Workspace admin portal:**

Log in to your Google Workspace portal as admin -> Apps -> Web and mobile apps

Click Add app -> Add custom SAML app ![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4407485683475)

In the popup window, enter OptiSigns as the name of the app, you can upload the app icon here as well. Then click continue.

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4407485688467)

The next page will provide the IDP data. Get these 2 highlighted information then click continue, these need to be maintained in the OptiSigns SAML SSO settings later.

![](https://support.optisigns.com/hc/article_attachments/21287044557843)

Next page will be the SP information, this is where you should provide the Single Sign On URL, and SP Entity ID you get from your OptiSigns SAML SSO setting.

SP Entity ID from OptiSigns SAML SSO setting should be put under Entity ID.

Single Sign On URL from OptiSigns SAML SSO setting should be put under ACS URL.

Also, set the Name ID format to Email.

![](https://support.optisigns.com/hc/article_attachments/21286792807699)

The next page is where you maintain the attributes. This step will be explained later in this article. Click Finish, and the app is added to the Google Workspace.

![](https://support.optisigns.com/hc/article_attachments/21286840258963)

After completing the app creation on Google Workspace. You can select the OptiSigns app under the "Web and mobile apps". Click on the OptiSigns app, and note the ID in the URL, that is the SPID that will be needed.

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/4407493347731)

Go back to your OptiSigns account maintain above mentioned 3 fields, and save it.

You can get SSO URL, Entity ID, and Certificate from your Google Workspace.

- Put SSO URL from Google Workspace under SAML 2.0 Endpoint (HTTP).
- Put Entity ID from Google Workspace under Identity Provider Issuer.
- Put the content from the base64 encoded certificate under Public Certificate.

![](https://support.optisigns.com/hc/article_attachments/21287166076819)

Now your login portal & integration are all setup.

#### **Assign & map users, and groups from Google Workspace to OptiSigns**

It's not required, but recommended to create groups of users to be assigned, and map to OptiSigns Roles, and Teams so they will automatically have the right role & group.

**IMPORTANT NOTE: If you don't configure this, all users will be assigned User Role & Default Team (screenshot see below)**

To configure how OptiSigns should map the user groups to OptiSigns Roles by going to: <https://app.optisigns.com/app/s/saml-settings>

Scroll to Advanced Settings and create a mapping.  
Group Name (can use department from Google Workspace), Role (role in OptiSigns) mapping.   
![mceclip8.png](https://support.optisigns.com/hc/article_attachments/4407485832851)

It's best practice to create a group specifically for OptiSigns with name prefix with optisigns- and map to OptiSigns like below:

- optisigns-admins (SAML group) -> OptiSigns role: Admin
- optisigns-users (SAML group) -> OptiSigns role: Users
- optisigns-custom-role (SAML group) -> OptiSigns custom role that you create

**How to handle Unmapped users/groups:**

You can map the "Unmapped users/group" to No Team (Disabled)

This way they will receive an error when trying to log in and will have to reach out to Admins to get correct teams, and roles assigned. This can be used as a safe guard, in case some users accidentally got assigned OptiSigns app but not the right groups.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/21287201539475)

Note that if you map a SAML group to a Team and then delete the team, it will result in new user being mapped to No Team and will have to contact you to be assigned to a team to use the app.

Next, it is time to talk about the attributes mapping. This is the last step when creating the app in Google Workspace.

Currently, OptiSigns support attributes mapping of first name, last name and group. You can define the attribute name in Google Workspace and set it to the same default attributes name used on OptiSigns.

These mappings will pass information to OptiSigns on what's user's Name and Groups.

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/4407485726611)

The "App attributes" are corresponding to OptiSigns

<https://app.optisigns.com/app/s/saml-settings>

OptiSigns accept firstName, lastName, and group by default. Instead of setting the attribute names to the default attribute name used on OptiSigns,  you can also change the attribute name on OptiSigns to match the attribute name you defined on Google Workspace as well.

![mceclip9.png](https://support.optisigns.com/hc/article_attachments/4407485875347)

#### **I've made it into my OptiSigns account, but don't seem to have all the side menu options I'm used to. What’s going on?**

It's likely you've signed on through your Branded Portal, using a URL similar to this one:

```
https://app.optisigns.com/signIn/<accountId>
```

You'll first need to find your OptiSigns Account ID. To do this, simply find a paired screen, and hit **Edit → Advanced → More**.

![edit screen advanced more](https://support.optisigns.com/hc/article_attachments/38962512579219)

Click **Device Info:**

![info button edit screen](https://support.optisigns.com/hc/article_attachments/38962512582675)

Find the **"accountId"** number, then write it down somewhere. You'll be needing it soon.

![](https://support.optisigns.com/hc/article_attachments/38962490259731)

Now copy the following URL, being sure to substitute your account ID where appropriate:

```
https://app.optisigns.com/signIn/<accountId>
```

Then put this URL in your Google Workspace under SSO URL.

### **That's it!**

You have configured SAML 2.0 for OptiSigns with Google Workspace.

Now your users can log in using the subdomain that you configured (in this case it was <https://advanced.optisigns.net/signIn>).

You can share the URL with your users and they can log in with their SSO credentials.

If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
