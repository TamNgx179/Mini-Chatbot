# Folder Level Permissions

Article URL: https://support.optisigns.com/hc/en-us/articles/360044600474-Folder-Level-Permissions
Article ID: 360044600474
Last Updated: 2025-09-10T15:02:26Z

### In this article, we'll explain Folder Level Permissions in detail and how to grant desired users and Teams proper access.

- [Change Folder Permissions](#Permissions)
  - [Restricting or Granting Access by User or Team](#RestrictingGranting)
  - [Folder Security by Team](#ByTeam)
  - [Folder Sharing](#Sharing)
- [Playlist and Schedule Specific Permissions](#Playlist&amp;Schedule)

Folder permission options give account Admins access to granular permissions structuring. It provides many options for controlling and managing who has access to what content.

Best of all, it can be used on any folder within OptiSigns: Screens, Files/Assets, Playlists, or Schedules.

Here are some key features:

- All Owners and Admins can see all folders. Only Users are restricted. See [**Managing User Roles**](https://support.optisigns.com/hc/en-us/articles/360046356113-Advanced-Security-Managing-User-Roles) for more information on User Roles.
- If you have folders and content set up before activating the Folder Security feature:
  - After activation, all users will still be able to see all folders. You can then tighten security by applying permissions to various folders.
- Security permissions cannot be set at the asset level

Let's get started.

|  |
| --- |
| **NOTE** |
| Folder Permissions options are only available with a [**Pro Plus subscription or higher**](https://www.optisigns.com/pricing). |

---

## Change Folder Permissions

To apply Folder Security settings, you'll need to create a folder. Folder permissions can be set during folder creation, or after a Folder is made.

|  |
| --- |
| **IMPORTANT** |
| Anything dealing with Folder Security is specific to users with **Owner**, **Super Admin**, or **Admin** permissions within OptiSigns. These roles are managed by your organization. |

When creating a **New Folder**, simply click **Advanced** to open up the Folder Security options:

![New folder folder-security](https://support.optisigns.com/hc/article_attachments/44602796060691)

For an existing folder, click the **Three Dots** **→ Change Permissions** option.

![change permission on screen folder](https://support.optisigns.com/hc/article_attachments/44602802531219)

This will open the **Change Security** popup, where the options are identical to the Advanced options when making a new folder.

![change security permission folder](https://support.optisigns.com/hc/article_attachments/44602796064787)

A few important notes:

- Any folders created inside a folder will automatically inherit its permissions. However, if you’ve already created a folder and then change the parent folder permissions, those child folders will not inherit them.
- OptiSigns uses a top-down setup, meaning that the highest-level folders will need the most Teams with permissions.
  - See our [**User Management Example**](https://support.optisigns.com/hc/en-us/articles/43657735780627-User-Management-Example-Chain-Restaurant-or-Retail-Store-with-Multiple-Locations) for a more complete explanation

### Restricting or Granting Access by User or Team

By default, access is granted to everyone on the Team which created the folder. You will see a greyed out box, which signifies **permissions which cannot be changed**. In this case, because the Default Team is the team which created/is creating this folder, it will need at least some level of access to it.

We can provide more specific permissions or restrictions, however, by deleting the **Everyone on this team** permission.

![new folder everyone on this team x](https://support.optisigns.com/hc/article_attachments/44602802533523)

Clicking the **blank area** allows you to add a new permission.

![new folder permission options](https://support.optisigns.com/hc/article_attachments/44602796071443)

As you can see, as the account owner or Super Admin, we have a lot of options. We can give access to everyone on the account, everyone on the team, only Team Admins, individual users, or other teams.

|  |
| --- |
| **IMPORTANT** |
| Users which appear here are ***only users registered on the current team**.* Other users on other teams will not appear. |

In this case, we'll grant access to our samurai friend Sanjuro here.

![new folder added user](https://support.optisigns.com/hc/article_attachments/44602796072595)

In terms of permissions, this means:

- All Super Admins have access to this folder;
- All Team Admins for the Default Team have access to this folder;
- The User, Kuwabatake Sanjuro, has Edit and View access to this folder;
  - This can be further restricted by unclicking the **Edit** option - this will only allow the User to view the content.
  - Having **Edit** selected but not **View** will allow the User to upload content to the folder, but not see what is inside.
- No other User, team member, or member of any other team ***will even see*** this folder.

### Folder Security by Team

As a Super Admin, we can change what Team view we are using at any time. This is also the process Team Admins will use to create Folder Security.

As a Super Admin, your current Team view can be seen next to your username, in the upper right corner of the screen. To change Team views, open up your User tab. Navigate to **Team**, then select another team from the list.

![](https://support.optisigns.com/hc/article_attachments/44602796075155)

In this case, we'll select the **Cosmos Space Center** team. We will then be viewing OptiSigns as an Admin of the Cosmos Space Center team, and this will be reflected next to your username.

![](https://support.optisigns.com/hc/article_attachments/44602796078483)

Looking at an existing Folder, we can see that, as an Admin of the Cosmos Space Center team, we have only limited ability to change the permissions of a folder created by another team:

![](https://support.optisigns.com/hc/article_attachments/44602796080659)

All we can do here is restrict access of the Users ***within our own Team*** to this folder.  
  
However, if we create a New Folder, we have the same options as we had before.

![](https://support.optisigns.com/hc/article_attachments/44602796083731)

We'll create another folder and restrict access to a certain user:

![](https://support.optisigns.com/hc/article_attachments/44602802552979)

This folder we've created will appear below, as long as we're in the Cosmos Space Center team view:

![firefox_vhms9zcYWs.jpg](https://support.optisigns.com/hc/article_attachments/44602796089235)

If we switch back to the Default Team (or any other Team without required permissions), we will not see the Cosmos Space Center team's folder, even as a Super Admin.

![](https://support.optisigns.com/hc/article_attachments/44602796090259)

### Folder Sharing

Folders can be shared across teams with specific Users, groups, or outside users. This is done in the same way as something like Google Docs.

To do this, see our guide on [**Sharing Playlists and Folders.**](https://support.optisigns.com/hc/en-us/articles/21708242980755-How-to-Share-Playlist-and-Folder-with-External-Users)

---

## Playlist and Schedule Specific Permissions

When dealing with Playlists and Schedules, there are some specific nuances.

#### Playlist-Specific:

**Example:** A Playlist is created using assets from several folders with various permissions.

- Anyone with access to all these folders will be able to see all the assets or sub-playlists they can see.
- Users with only partial access ***will only see the assets or sub-playlists they have access to.***
- Playlist Total Time will always display the ***full duration,*** including invisible assets or sub-playlists:

  ![](https://support.optisigns.com/hc/article_attachments/44602802557331)
- A warning message will display for Users stating "There are items in this schedule you do not have access to"

#### Schedule-Specific:

**Example:** A screen has a playlist or asset scheduled that is not accessible to all users.

- Anyone with access to this playlist or asset will be able to see the schedule
- Users without the proper permissions will see that something is scheduled, but will not be able to select it (grayed-out). It will display as a "Non-accessible item" instead of the name of the asset or playlist.
- A warning message will display for Users stating "There are items in this schedule that you do not have access to"

### That's all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
