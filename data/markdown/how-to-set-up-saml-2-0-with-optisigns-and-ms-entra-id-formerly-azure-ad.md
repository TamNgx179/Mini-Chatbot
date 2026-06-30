# How to Set Up SAML 2.0 with OptiSigns and MS Entra ID (formerly Azure AD)

Article URL: https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD
Article ID: 4407252213395
Last Updated: 2026-02-05T20:23:47Z

### In this article, we will provide a step-by-step guide to setting up SAML 2.0 with Microsoft Entra ID for use with OptiSigns.

- [Set Up OptiSigns Subdomain and SAML SSO Settings](#Subdomain)
  - [Setting up a Custom Subdomain](#CustomSubdomain)
  - [Setting up SAML SSO Settings](#SAMLssoSettings)
- [Add OptiSigns as an App in Azure Portal](#EntraIDPortal)
- [Assign and Map Users and Groups from Azure to OptiSigns (OPTIONAL)](#AssignMap)
  - [How to Handle Unmapped Users and Groups (OPTIONAL)](#Unmapped)
  - [Managing Attributes & Claims in Microsoft Azure (OPTIONAL)](#AttributesClaims)
    - [Creating Group Claims (OPTIONAL)](#GroupClaims)
    - [Customizing Claims for Use with OptiSigns (OPTIONAL)](#UserClaims)
- [Setting Up OptiSigns Login to Appear in Office.com (OPTIONAL)](#Office.com)
- [Frequently Asked Questions](#FAQs)

|  |
| --- |
| **NOTE:** This feature is available to **Pro Plus**, **Engage**, and **Enterprise** plan users. |

SAML (Security Assertion Markup Language) 2.0 allows a single authorization to access multiple systems. This can be configured to allow easy access to OptiSigns digital signage through your Microsoft Entra ID. Entra ID will act as the IDP (Identity Provider), with OptiSigns will work as the SP (Service Provider).

---

## Set Up OptiSigns Subdomain and SAML SSO Settings

To begin, you’ll need to perform some functions within the OptiSigns app, including:

- Creating a Custom Subdomain
- Setting up SAML SSO Settings

Now, let’s begin.

### Setting up a Custom Subdomain

First, ensure you have an OptiSigns subdomain. This can be obtained by going to the [Branding Settings](https://app.optisigns.com/app/s/branding-settings) page.

Fill in the subdomain field and click **Activate**. Now you can use this subdomain for a variety of functions, including SAML setup. You can also map your domain by following our article on [Custom Domain mapping](https://support.optisigns.com/hc/en-us/articles/1500000480302-Advanced-Custom-Domain-mapping).

This subdomain will be the URL to share with your users so they can log in to use the app after integration has been set up.

For this example, we will use <https://optisignsdemo-ad.optisigns.net/> as our URL.

### Setting up SAML SSO Settings

Go to the SAML Single Sign-On Setting Page:

![go to saml single sign on page](https://support.optisigns.com/hc/article_attachments/37186635027731)

Now enable **Enable SAML SSO**. There should be a green checkmark next to the option. This will expand the options available to you.

![saml sso settings checklist](https://support.optisigns.com/hc/article_attachments/37186682762387)

The other settings are:

- **Enable Username & Password Login -** Allow users to also log in with username/password. We recommend disabling this once integration is finished. As Admin/Owner, it’s recommended to keep at least 1 account with a password login in case there are issues. You can use this account to login directly to the app to reconfigure if necessary.
- **Enable User Creation -** If users are authenticated but do not exist in OptiSigns, they will be created in the OptiSigns app. We recommend enabling this unless you wish to be extremely strict and want to review the roles of users before they can start using OptiSigns.
- **Enable User Override -** Every time a user logs in, OptiSigns will check their group assignment. If it has changed on SAML, OptiSigns will update their permissions within the app.

Next, note your **Single Sign On URL** and **Audience URI (SP Entity ID) URL**. You will need to use these later.

![](https://support.optisigns.com/hc/article_attachments/37186635040403)

---

## Add OptiSigns as an App in Microsoft Entra ID Portal

Log in to your Microsoft Azure portal as an administrator, then navigate to **Enterprise Applications**.

Click **New Application**.

![creating new enterprise application ms azure](https://support.optisigns.com/hc/article_attachments/37186682790803)

Select **Create your application**. This pops up a sidebar on the right. Inside, input “OptiSigns” as the name of the app, and choose **Integrate any other application you don’t find in the gallery (Non-gallery)**. Finally, hit **Create**.

![create own application ms azure](https://support.optisigns.com/hc/article_attachments/37186682801427)

This will take a moment, but you’ll eventually be brought to an Overview screen.

Click **Set up single sign on.**

![setting up single sign on ms azure](https://support.optisigns.com/hc/article_attachments/37186682808851)

Click **SAML**. This will begin the setup of SAML-based Sign-on.

![saml ms azure](https://support.optisigns.com/hc/article_attachments/37186635065235)

Here, click **Edit** in the Basic SAML Configuration section. This is where you should provide the Single Sign On URL and SP Entity ID you got [in the last step](#SAMLssoSettings).

![basic saml configuration](https://support.optisigns.com/hc/article_attachments/37186635074707)

Place the Single Sign On URL under **Reply URL** and the SP Entity ID under **Identifier**.

![identifier and reply URL saml config ms azure](https://support.optisigns.com/hc/article_attachments/37186682845331)

Next, note the next two sections: **SAML Certificates** and **Set up OptiSigns**. You’ll need to obtain three key pieces of information:

1. Certificate (Base64)
2. Login URL
3. Microsoft Entra Identifier

![three key pieces of information ms azure](https://support.optisigns.com/hc/article_attachments/37186682850067)

These will need to be maintained within the OptiSigns app, in the SAML SSO Settings page.

Now go back to your OptiSigns account and input these three pieces of information in the following places:

1. **Login URL** should go under **SAML 2.0 Endpoint (HTTP)**
2. **Microsoft Entra Identifier** should go under **Identity Provider Issuer**
3. The content of the downloaded **Certificate (Base64)** should be pasted under **Public Certificate**.

![setup SAML authentication optisigns](https://support.optisigns.com/hc/article_attachments/37186682855955)

With this, your login portal and integration are all set up. If this is all you need, you’re done. If you’d like to manage users, groups, and teams, keep reading.

---

## Assign and Map Users and Groups from Azure to OptiSigns (OPTIONAL)

We highly recommend creating groups of users to be assigned within Azure to be automatically mapped to OptiSigns with the correct role and group.

|  |
| --- |
| **NOTE:** Without configuring this, all users will be assigned User Role and Default Team. You will have to manually change their roles and teams within the OptiSigns app. |

Head back to the [SAML settings page](https://app.optisigns.com/app/s/saml-settings) within OptiSigns. Scroll to **Advanced Settings** and you should see this:

![group mapping optisigns](https://support.optisigns.com/hc/article_attachments/37186635103379)

By default, unmapped users/groups become Users within the Default Team in OptiSigns. To link OptiSigns to Azure, either create a new mapping by clicking **Add** or edit one of the existing Group mappings.

The “Group Name” within OptiSigns corresponds to the “Object ID” within Azure. To find this information, go to your Azure Portal and select **Groups**.

![groups tab ms azure](https://support.optisigns.com/hc/article_attachments/37186682869779)

Your Object ID can be found here for each group you’ve created.

![groups with object id noted](https://support.optisigns.com/hc/article_attachments/37186635118611)

This Object ID should be input into the Group Name field within OptiSigns. However, we recommend creating a group specifically for OptiSigns with an OptiSigns- prefix and map these to OptiSigns like this:

- optisigns-admins (SAML group) → OptiSigns role: Admin
- optisigns-users (SAML group) → OptiSigns role: Users
- optisigns-custom-role (SAML group) → OptiSigns custom role that you create

Once finished, it should resemble this:

![filled out group mapping optisigns](https://support.optisigns.com/hc/article_attachments/37186682886547)

You can create as many groups and roles as you like.

### How to Handle Unmapped Users and Groups

You may wish to map the “Unmapped users/groups” section to **No Team (Disable)**. This way, they will receive an error message when trying to login in and will have to reach out to Admins to get the correct team and role assigned. This is a useful safeguard in case certain users accidentally get assigned the OptiSigns app but not the correct group.

![unmapped users/groups with no team selected](https://support.optisigns.com/hc/article_attachments/37186635129363)

|  |
| --- |
| **NOTE:** If you map an SAML group to a Team, then delete the Team, it will result in new users being mapped to No Team. They will have to contact you to be assigned to a team in order to use the app. |

### Managing Attributes & Claims in Microsoft Azure

Editing the Attributes & Claims in Microsoft Azure can give you even more control over the Users added to the group, and is a valuable tool.

To begin, go to the Azure portal. Click **Enterprise Applications** → **OptiSigns** → **Single sign-on**. Scroll down to Section 2: User Attributes & Claims. This is where you maintain the mapping of these attributes.

![user attributes and claims ms azure](https://support.optisigns.com/hc/article_attachments/37186682899603)

Within this section, there are two main things to customize:

- Group Claims
- User Attributes

We’ll walk you through each.

#### Creating Group Claims for Use with OptiSigns

To create a Group Claim, first hit **Add a group claim**:

![add group claim ms azure](https://support.optisigns.com/hc/article_attachments/37186682904595)

When you create a Group:

1. Select **Groups assigned to the application** under “Which groups associated with the user should be returned in the claim?”
2. (Optional) Input the name “groups” in the “Customize the name of the group claim” and leave the Namespace section blank.

![group claim settings ms azure](https://support.optisigns.com/hc/article_attachments/37186635155987)  
That’s all for creating Group claims.

#### Customizing User Claims for Use with OptiSigns

These mappings will pass information to OptiSigns on the user’s Name and Group:

![managing user claims ms azure](https://support.optisigns.com/hc/article_attachments/37186635162003)

The Claim names are, by default, represented by a URL. The Type will be given as SAML, with the Value corresponding to identifying information about the user, including:

- user.givenname
- user.groups (only if setup - see above section)
- user.mail
- user.userprincipalname
- user.surname

These Claim names correspond to this section under **Advanced Settings** on the SAML SSO Settings page:

![advanced settings optisigns saml sso settings page](https://support.optisigns.com/hc/article_attachments/37186635168659)

OptiSigns accepts First Names, Last Names, and Groups by default.

These values correspond to the **Namespace** of the claim. So, in other words, if the Value corresponding to the firstName (user.givenname) is a URL, you will have to paste the entire URL into OptiSigns. It is possible, however, to change the Namespace to something more manageable.

In Azure, click on any of these claims to Manage them.

![ms azure manage claims](https://support.optisigns.com/hc/article_attachments/37186635174931)

To eliminate the URL, simply delete it from the Namespace field, then hit **Save**.

![eliminate URL ms azure claim](https://support.optisigns.com/hc/article_attachments/37186635182483)

This will replace the URL in the Namespace with the Name. This is a much easier piece of information to manage.

![claims after removing url ms azure](https://support.optisigns.com/hc/article_attachments/37186635189523)

These can now be mapped, like so:

![proper user mapping in optisigns example](https://support.optisigns.com/hc/article_attachments/37186635199123)

Finally, go to the **Users and groups** section within Azure and assign your groups to the OptiSigns Enterprise app.

![add user/group](https://support.optisigns.com/hc/article_attachments/37186682960019)

---

## Setting Up OptiSigns Login to Appear in Office.com

It’s often convenient to have the OptiSigns app appear as a clickable option on your company’s Office.com portal.

To set this up, you'll first need to find your OptiSigns Account ID. To do this, simply find a paired screen, and hit **Edit** **→** **Advanced** **→** **More**.

![edit screen advanced more](https://support.optisigns.com/hc/article_attachments/38825933298579)

Click **Device Info:**

![info button edit screen](https://support.optisigns.com/hc/article_attachments/38825917033875)

Find the **"accountId"** number, then write it down somewhere. You'll be needing it soon.

![](https://support.optisigns.com/hc/article_attachments/38825917043475)

Now copy the following URL, being sure to substitute your account ID where appropriate:

```auto
https://app.optisigns.com/signIn/<accountId>
```

Next, head back to your Azure portal, and go to **SAML-based Sign-on**. Once there, find **Basic SAML Configuration** and hit **Edit.** This will open up a sidebar. Simply paste/type your URL into the **Sign on URL (Optional)** and **Relay State** (Optional) fields.

![](https://support.optisigns.com/hc/article_attachments/38838224681235)

This will allow the OptiSigns app to appear in your Microsoft Office portal. This will also provide the full range of options for your side menu.

![optisigns app in ms office portal](https://support.optisigns.com/hc/article_attachments/37186635219219)

---

## Frequently Asked Questions

Here, we’ll answer some of the most common questions we get around this topic.

#### **I Got this Error Message. Help?**

Unable to process request due to missing initial state. This may happen if browser sessionStorage is inaccessible or accidentally cleared. Some specific scenarios are - 1) Using IDP-Initiated SAML SSO. 2) Using signInWithRedirect in a storage-partitioned browser environment.

![optisigns common error message](https://support.optisigns.com/hc/article_attachments/37186635223443)

This error appears for one of two reasons:

1. The wrong URL was input. This is frequently (https://auth.optisigns.com/\_\_/auth/handler)
2. The user has tried to access the OptiSigns portal from Office.com without setting up SAML SSO in Microsoft Azure correctly.

The easiest way to solve this problem is to login through your branded URL.

![branded url example](https://support.optisigns.com/hc/article_attachments/37186682989075)

This will be unique to your organization. For more information, follow the steps outlined in the “Add OptiSigns as an App in Microsoft Entra ID Portal” section.

#### **It’s Saying I Don’t Belong to a Team/Group. How Can I Fix This?**

This error has to do with group mapping. To start, follow all the steps outlined in the “Assign and Map Users and Groups” section above.

![team/group error message](https://support.optisigns.com/hc/article_attachments/37188678189203)

If you’re still having trouble, check your Group names. In Azure, that’s Object ID:

![ms azure groups tab object id](https://support.optisigns.com/hc/article_attachments/37186635239699)

Check the desired User’s Attributes & Claims and make sure their Group name is assigned as **Groups assigned to the application**.

**![group claims error fix](https://support.optisigns.com/hc/article_attachments/37186635254803)**

Next, check if the Claim has been set up properly:

![proper claims names ms azure](https://support.optisigns.com/hc/article_attachments/37186683011731)

The above values should match these within the OptiSigns portal:

![proper claims names optisigns](https://support.optisigns.com/hc/article_attachments/37186683017875)

Finally, make sure the user and group have been added to the application within MS Azure:

![user and group added to app within ms azure](https://support.optisigns.com/hc/article_attachments/37186635286419)

This should resolve the issue.

#### **I've made it into my OptiSigns account, but don't seem to have all the side menu options I'm used to. What’s going on?**

It's likely you've signed on through your Branded Portal, using a URL similar to this one:

```auto
https://app.optisigns.com/signIn/<accountId>
```

Go ahead and follow the steps outlined [**here**](#Office.com) and this issue should resolve itself.

### **That's all!**

You have configured SAML 2.0 for OptiSigns with Microsoft Entra.

You can share the URL with your users and they can log in with their SSO credentials.

If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at support@optisigns.com
