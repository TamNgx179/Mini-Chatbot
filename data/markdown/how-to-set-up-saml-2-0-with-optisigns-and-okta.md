# How to set up SAML 2.0  with OptiSigns and Okta

Article URL: https://support.optisigns.com/hc/en-us/articles/4404590815635-How-to-set-up-SAML-2-0-with-OptiSigns-and-Okta
Article ID: 4404590815635
Last Updated: 2026-06-08T15:02:21Z

With Pro Plus and Enterprise plans, you can configure SAML 2.0 with OptiSigns via Okta.

Assuming you already using Okta for identity management. If you have not used Okta, it is the leading identity management platform, you can learn more [here](https://www.okta.com/intro-to-okta/).

### **Set up OptiSigns & Okta:**

**First, you need to do some setup in OptiSigns:**

If you don't have a subdomain yet, you can set up one by going to:  
<https://app.optisigns.com/app/s/branding-settings>

Fill in the subdomain field and click Activate. After that, you can use this subdomain for "  
You can also map your domain like digitalsigns.yourcompany.com by following this [article](https://support.optisigns.com/hc/en-us/articles/1500000480302).

This will be the URL that you can share with your users so they can log in to use the app, once integration has set up. In our example, we will use <https://advanced.optisigns.net/>

![](https://support.optisigns.com/hc/article_attachments/43875570896659)

Next, go to the SAML Single Sign On setting page:

<https://app.optisigns.com/app/s/saml-settings>

Click Enable SAML SSO.

The settings are:

- Enable Username & Password login: Allow users to also log in with username/password. It’s recommended to disable it once integration is all done. As Admin/Owner, it's recommended that you keep at least 1 account with a password log in, in case there's issues, you can always log back in from app.optisigns.com to reconfigure.
- Enable User Creation: If users are authenticated, but do not exist in OptiSigns, they will be created in OptiSigns. You should enable this, because you likely already assign/approve users/groups to use OptiSigns, unless for some reason you want to be very strict and want to review the roles of users before they can start using OptiSigns.
- Enable User Override: Every time a user logs in, if their group assignment has changed on SAML, OptiSigns will update, and override new profile settings.
- Note the "Single Sign On URL" and "Audience URI (SP Entity ID) URL", you will need this to use in Okta later.

![](https://support.optisigns.com/hc/article_attachments/28207766414227)

**Next, add OptiSigns as an App to your Okta account:**

Log in to your Okta account as admin -> Application

Or go to: <https://optisigns-admin.okta.com/admin/apps/active>

Click Create App Integration

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4404598581779)

Select SAML 2.0

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4404590829203)

Enter App name: OptiSigns

If you want to upload a logo, you can use our logo [here](https://download.optisignsapp.com/marketing/optisigns-logo.png).

Click Next

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/4404590844691)

In "Single sign-in URL" and "Audience URI (SP Entity ID)", these are the URL that you have in <https://app.optisigns.com/app/s/saml-settings>  
Check "Use this for Recipient URL and Destination URLs"

Click Next.

![](https://support.optisigns.com/hc/article_attachments/52406311133459)

![](https://support.optisigns.com/hc/article_attachments/28207766417811)

The last step is just informational for Okta to know how you are using the app.

Select "I'm an Okta customer adding an internal app" as OptiSigns is now an internal app in your organization.

Click Next.

![mceclip8.png](https://support.optisigns.com/hc/article_attachments/4404615741075)

Then click "View Setup Instruction"

Copy these 3 fields and paste into OptiSigns' SAML config page:

- Identity Provider Single Sign-On ULR -> OptiSigns: SAML 2.0 Endpoint (HTTP)
- Identity Provider Issuer -> OptiSigns: Identity Provider Issuer
- X.509 Certificate -> OptiSigns: Public Certificate

![okta-config.png](https://support.optisigns.com/hc/article_attachments/4404615786259)

Lastly, set the "Sign In Button label", this is the text of the button you want your users to see in their login portal. Use something descriptive like "Log in with Okta" "Sign in with SSO" or something your user is familiar with.

![okta-config-2.png](https://support.optisigns.com/hc/article_attachments/4404615885331)

Click Save

Now your login portal & integration are all setup.

Next, you need to assign users, and groups that can use OptiSigns.

#### **Assign & map users, and groups from Okta to OptiSigns**

It's not required, but recommended to create groups of users to be assigned, and map to OptiSigns Roles, and Teams so they will automatically have the right role & group.

**IMPORTANT NOTE: If you don't configure this, all users will be assigned User Role & Default Team (screenshot see below)**

To configure how OptiSigns should map the user groups to OptiSigns Roles by going to: <https://app.optisigns.com/app/s/saml-settings>

Scroll to Advanced Settings and create a mapping.  
Group Name (group names in Okta), Role (role in OptiSigns) mapping.   
![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4404820186003)

It's best practice to create a group name prefix with Optisigns- and map to OptiSigns like below:

- optisigns-admins (SAML group) -> OptiSigns role: Admin
- optisigns-users (SAML group) -> OptiSigns role: Users
- optisigns-custom-role (SAML group) -> OptiSigns custom role that you create

**How to handle Unmapped users/groups:**

You can map the "Unmapped users/group" to No Team (Disabled)

This way they will receive an error when trying to log in and will have to reach out to Admins to get the correct teams, and roles assigned. This can be used as a safeguard, in case some users accidentally got assigned OptiSigns app but not the right groups.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/4404812977171)

Note that if you map a SAML group to a Team and then delete the team, it will result in new user being mapped to No Team and will have to contact you to be assigned to a team to use the app.

Next, go to your Okta Admin portal. Click Applications -> OptiSigns.

![mceclip11.png](https://support.optisigns.com/hc/article_attachments/4404615820691)

Click Assign -> People or Groups to use this app. You can also configure your user to request to use the app, but that's beyond the scope of this article.

![mceclip12.png](https://support.optisigns.com/hc/article_attachments/4404615832339)

You can set up group mapping by going to General -> SAML settings

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/4404762241811)

Click Next:

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/4404767623827)

Creating these mappings will pass information to OptiSigns on the user's Name and Groups.

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/4404762334611)

The "Attribute Statement" and "Group Attribute Statement" are corresponding to OptiSigns <https://app.optisigns.com/app/s/saml-settings>

OptiSigns accept firstName, lastName, and group by default, but if you change these in Okta, you will need to match it here as well.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/4404812916115)

**Additional Note:**

If you want your user to login to the OptiSigns portal via OKTA portal, Okta does not support the IDP that is initiated. It will use the Bookmark App on Okta, You can follow this article to set up the Bookmark app: <https://support.okta.com/help/s/article/How-do-you-create-a-bookmark-app?language=en_US>

#### **I've made it into my OptiSigns account, but don't seem to have all the side menu options I'm used to. What’s going on?**

It's likely you've signed on through your Branded Portal, using a URL similar to this one:

```auto
https://app.optisigns.com/signIn/<accountId>
```

You'll first need to find your OptiSigns Account ID. To do this, simply find a paired screen, and hit **Edit** **→** **Advanced** **→** **More**.

![edit screen advanced more](https://support.optisigns.com/hc/article_attachments/38962229904659)

Click **Device Info:**

![info button edit screen](https://support.optisigns.com/hc/article_attachments/38962229906835)

Find the **"accountId"** number, then write it down somewhere. You'll be needing it soon.

![](https://support.optisigns.com/hc/article_attachments/38962235455635)

Now copy the following URL, being sure to substitute your account ID where appropriate:

```auto
https://app.optisigns.com/signIn/<accountId>
```

Now you'll want to set this URL up as an Okta bookmark. You can follow this article to set up the Bookmark app: <https://support.okta.com/help/s/article/How-do-you-create-a-bookmark-app?language=en_US>

### **That's it!**

You have configured SAML 2.0 for OptiSigns with Okta.

Now your users can log in using the subdomain that you configured (in this case it was <https://advanced.optisigns.net/signIn>).

You can share the URL with your users and they can log in with their SSO credentials.

If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
