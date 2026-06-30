# Advanced Security: Managing User Roles

Article URL: https://support.optisigns.com/hc/en-us/articles/360046356113-Advanced-Security-Managing-User-Roles
Article ID: 360046356113
Last Updated: 2026-02-04T16:01:54Z

### In this article, we will go over the ability to manage user roles in OptiSigns for improved security.

- [Accessing User Management](#Accessing)
- [Default User Roles](#Default)
- [Creating New User Roles](#Creating)
- [Adding or Inviting Users](#AddingorInviting)
- [Managing Users](#Managing)

|  |
| --- |
| **NOTE** |
| Role Security is only available to **Pro Plus** plan subscribers or above. |

With OptiSigns, it's possible to control User access by granting various roles. Roles can be assigned, and custom roles created to provide more granular control of user security. For example, you may want someone to contribute content, but not add new screens.

---

## Accessing User Management

User roles can be managed by the **Account Owner**, or Super Admin. They can be accessed through the **Account Members** tab under your User Profile:

![mceclip0.jpg](https://support.optisigns.com/hc/article_attachments/38720525740691)

You'll see a list of Users and Teams. By default, it will only be the Owner (Super Admin) in the Default Team.

![mceclip1.jpg](https://support.optisigns.com/hc/article_attachments/38720509819027)

From here, you are able to:

- **Add -** Adds users directly.
- **Invite** - Sends invite to users. Most helpful if your company uses SSO.
- **Manage Roles** - Allows creation of custom roles and allows management of created roles
- **Manage Members** - Controls the members within this Team.

For more on Teams, see our article on [**Working with Teams and Security Levels**](https://support.optisigns.com/hc/en-us/articles/360034883113-Working-with-Teams-and-Security-Levels)**.** For now, we will continue our discussion of User Roles.

---

## Default User Roles

By default, there are 7 roles:

- **Owner -** Can delete accounts, manage default team, create teams, access billing, invite users to teams, manage any and all screens, and reset passwords across multiple teams.
- **Super Admin** - Has full access to all teams. Can create teams and access billing. Capable of inviting users to teams, managing all screens, and resetting passwords across multiple teams.
- **Admin -** Has full access to an individual team. Can invite users to the team, manage the number of screens available per team, and reset passwords for other users.
- **User** - Can create, edit, and delete all content within the folders they have access to. Can add or remove screens.
- **Content Proposal -** Can create new files and assets, and propose changes to playlists. Cannot add or remove screens.
- **Content Approval -** Similar to User, but can review and approve content change proposals. Can add or remove screens.
- **Read Only -** Can only view folders they have access to.

Here's what each will look like in a single team:

![mceclip5.jpg](https://support.optisigns.com/hc/article_attachments/38720525745043)

It's possible to create custom roles, as well.

---

## Creating New User Roles

To create a custom role, hit the **Manage Roles** button:

![mceclip7.jpg](https://support.optisigns.com/hc/article_attachments/38720784822035)

When first getting started, you will have no custom roles created. To make one, hit **New Role**.

![mceclip8.jpg](https://support.optisigns.com/hc/article_attachments/38720784824083)

You'll see this somewhat intimidating screen:

![mceclip9.jpg](https://support.optisigns.com/hc/article_attachments/38720784826003)

The **Name** refers to the name of the role (i.e. Admin, User, etc.). The other options control what sorts of access the Role has.

In this example, we'll be creating a custom role called Designer. We want the Designer to be able to create and upload content, but have no access to screens, playlists or schedules. This role would be one we'd consider for an outside contractor or someone we view as a slight security risk.

![mceclip12.jpg](https://support.optisigns.com/hc/article_attachments/38720784827923)

Once you've given the appropriate permissions to the role and named it, hit **Save**.

You'll now see a list of Managed Roles. In this example, we've only created one, but if you create more they will all appear here.

![mceclip13.jpg](https://support.optisigns.com/hc/article_attachments/38720784829715)

Role permissions can be easily checked by hitting the small carrot next to the role name:

![mceclip14.jpg](https://support.optisigns.com/hc/article_attachments/38720784834067)

Now, any user given this role will have these permissions.

---

## Adding or Inviting Users

Now that you've created the custom roles you'll want for your team, you'll need to actually give them access to the OptiSigns platform in their assigned role. This can be done in two ways:

1. **Adding** them directly to OptiSigns
2. **Inviting** them via email

These users can be set up to be either individuals, or a Job Title within your company.

To Add a user directly, hit the **Add** button.

![mceclip6.jpg](https://support.optisigns.com/hc/article_attachments/38720525755667)

You'll see this screen. Here, you can input user information, including First Name, Last Name, Email, and Role. You can automatically generate a password, then allow the user to change it once they log in.

![mceclip15.jpg](https://support.optisigns.com/hc/article_attachments/38720768955411)

The Roles can be selected from a drop-down. The options include the 6 default roles and any custom roles you've made.

![mceclip16.jpg](https://support.optisigns.com/hc/article_attachments/38720784838419)

Once the information has been put in successfully, you'll see a confirmation:

![mceclip17.jpg](https://support.optisigns.com/hc/article_attachments/38720784847379)

These login credentials can be sent directly to an email address.

Inviting users is a very similar process. To begin, hit the **Invite** button.

![mceclip19.jpg](https://support.optisigns.com/hc/article_attachments/38720784851347)

The difference here is that account information will need to be set up by the end user.

![mceclip18.jpg](https://support.optisigns.com/hc/article_attachments/38720768965523)

This is most useful for SSO setups.

If you're wanting to add users via SAML SSO, please see the [**SSO & SAML section**](https://support.optisigns.com/hc/en-us/sections/26319189062803-SSO-SAML) of our Knowledge Base.

---

## Managing Users

The Manage Members tab allows you to quickly reassign user roles and teams across your entire account.

![mceclip20.jpg](https://support.optisigns.com/hc/article_attachments/38720768970771)

From here, you can add or remove users from teams, and quickly change their roles. By default, it displays only users who have an account but are not in the current team.

![mceclip21.jpg](https://support.optisigns.com/hc/article_attachments/38720784856339)

As you can see, we have the option to add our additional account to this team, and define its role. New users can be Added or Invited from here, as well.

If you want to manage all accounts at once, hit **Show All Members**.

![mceclip23.jpg](https://support.optisigns.com/hc/article_attachments/38720768973843)

Now these members can be removed from this Team, and have their user permissions changed.

### That's all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
