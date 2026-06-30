# User Management Example - Chain Restaurant or Retail Store with Multiple Locations

Article URL: https://support.optisigns.com/hc/en-us/articles/43657735780627-User-Management-Example-Chain-Restaurant-or-Retail-Store-with-Multiple-Locations
Article ID: 43657735780627
Last Updated: 2025-08-28T19:28:55Z

### In this article, we’ll share some best practices for setting up your OptiSigns portal if you have many screens and multiple locations.

- [Identifying the Need](#Identifying)
- [Folder and Screen Organization](#Organization)
- [Creating Teams](#CreatingTeams)
- [Set Up Folder-Level Security](#FolderLevelSecurity)
  - [Complete Folder-Level Security Example](#SecurityExample)
- [Branding and Enforcing Brand Guidelines (Optional)](#Branding)
- [Adding Users via SAML SSO, or Directly Through OptiSigns](#AddingUsers)

Using OptiSigns, it’s possible to create a sophisticated setup for your OptiSigns portal to manage users, permissions, and screens. Securely configuring the OptiSigns portal to your needs during the initial onboarding process can save time and prevent issues down the line.

|  |
| --- |
| **NOTE** |
| These User Management options discussed here are only available to [**Pro Plus subscribers or above**](https://www.optisigns.com/pricing)**.** |

Here, we’ll be providing a practical example of how a restaurant chain might use OptiSigns. In the course of this article, we’ll:

- Create a network of folders to organize our screens based on location;
- Work with the [**Teams feature**](https://support.optisigns.com/hc/en-us/articles/360034883113-Working-with-Teams-and-Security-Levels)to create the appropriate user organizational structure;
- Use [**Folder Level Security**](https://support.optisigns.com/hc/en-us/articles/360044600474-Advanced-Security-Folder-Level-Security)to restrict to certain users based on their team;
- Create [**Custom Branding**](https://support.optisigns.com/hc/en-us/articles/1500000485202-Custom-Branding-Settings) for the OptiSigns portal,and [**Enforce Brand Guidelines**](https://support.optisigns.com/hc/en-us/articles/42313875427859-Brand-Kit-and-Enforcing-Brand-Guidelines)across your teams
- Fold OptiSigns access into a corporate **SSO** structure

|  |
| --- |
| **IMPORTANT** |
| This article applies to **Account Owners** and **Super Admins**. The steps laid out here cannot be undertaken by anyone with lower permissions (Admin, User, etc.). |

---

## Identifying the Need

The first step to organizing your portal is knowing what kind of management structure you want in place for your digital signage.

Do you want a centrally managed solution, where the end users have no or limited control over the content for their signs? Do you want a large number of independently functioning end users, with total control over their content? Do you want something in between? Identifying how you want your account users to interact with the platform is the first step in this process, and will be critical for the setup.

In this example, we’ll be using a centrally managed system, but with some degree of local control. We want:

- Organization of screens to mirror our corporate structure
- End users to be able to manage their own screens and upload their own content
- To provide content for all our end users that they are required to display (i.e. large scale promotions, brand identity displays, etc.).
  - For this, we’ll assume several layers of management. For example, you may have national, regional, or local promotions. You might not want a promotion targeting Boston to appear in Dallas, for instance.
- To enforce brand guidelines

With our needs identified, we can begin.

---

## Folder and Screen Organization

How you choose to organize your screens will depend on your needs, but there are many ways it can be done.

In our example, we will focus on location. This is the single most common way we have seen our customers set up OptiSigns. That said, you can organize however works best to you.

For our hypothetical chain restaurant or retail store, we will create an internal folder structure to mirror the corporate organizational structure. So, in this case, that is **Region → State → City/Sub-region → Store Location/Number.** We’ll create nested sub-folders corresponding to these values. When set up, it will look something like this:

#### **Top Level:**

**![top level folders for default team](https://support.optisigns.com/hc/article_attachments/43657735752211)**

#### **Screen Level:**

![screen level display showing nesting](https://support.optisigns.com/hc/article_attachments/43658114517651)

Note the level of nesting we’ve set up. The reason for this? Each of these folders can be granted different levels of permissions. We’ll set that up soon.

For the rest of this example, we’ll be focusing on a single store: the **Cosmos Space Center**, with the following nesting:

- **Pacific -** Region
  - **California -** State
    - **Los Angeles** - City/Sub-region
      - **Cosmos Space Center** - Store Location
        - Screens at this location will be placed in this folder.

We want to ensure only the proper users can access the screens and content for this location. We also want to make sure that any local, state, or regional managers can provide content as needed.

---

## Creating Teams

Before we can do that, we’ll need to set up our Teams. Teams act like a bucket where users can be assigned based on the level of permissions we want them to have. With our folders set up, it becomes easier to see what Teams we’ll want to create, but you can also start with this step and set up the folders later. For more information, see our article on [**Teams and Security Levels**](https://support.optisigns.com/hc/en-us/articles/360034883113-Working-with-Teams-and-Security-Levels).

In this example, we’ll want to create a Team for each store location. In addition, we’ll want to set up a Team for any managers of the Los Angeles City/Subregion; California state; and Pacific Region. We’ll then use Folder permissions to restrict access to each nested folder to the appropriate Team. By doing this, only the Account Owner and Super Admins will have access to the full structure.

|  |
| --- |
| **IMPORTANT NOTE** |
| For increased centralization, you can remove Teams at various levels. If you want a 100% centrally managed system with no input outside your IT department, you can skip this step entirely. OptiSigns is extremely flexible and can be configured to any structure you like. |

To get started, go to **Account Members** under your user profile.

![access account members for teams creation](https://support.optisigns.com/hc/article_attachments/43657783477523)

You’ll see the **Default Team**, which for now should only consist of the Account Owner. The Default Team is typically reserved for central management, and people within this team will be able to see the entire organizational structure. In this example, our Default Team will represent the national level, able to view all screens across our company. They will also be responsible for adding any new screens and moving them between teams as needed.

To continue, click **Add Team**.

![default team and add team](https://support.optisigns.com/hc/article_attachments/43657783478291)

The following screen will appear:

![add team screen with info filled in](https://support.optisigns.com/hc/article_attachments/43657735756179)

Here, we’ve named the team after the region, which will be managing all screens in the region. We’ve also written a short description of the team's purpose. We’ll set up the “Number of screens limit” later, once all our screens are set up.

|  |
| --- |
| **IMPORTANT NOTE** |
| There are no such things as “Sub-Teams” in OptiSigns. While it is possible to provide regional managers (in our example) access to all the screens or content under their purview, they WILL NOT be able to manage their users in kind. This can only be done by Super Admins, who can manage Users across teams. Set up your teams accordingly. |

Now we’ll proceed to create all our Teams. A basic setup might look something like this:

![teams setup with admins and users](https://support.optisigns.com/hc/article_attachments/43657735756435)  
A bit about User Roles before we continue:

- **Owner / Super Admin** -Have full access to all teams. Can create teams and access billing. Capable of inviting users to teams, managing all screens, and resetting passwords across multiple teams.
- **Admin** - Has full access to an individual team. Can invite users to the team, manage the number of screens available per team, and reset passwords for other users.
- **User** - Can create, edit, and delete all content within the folders they have access to. Can add or remove screens.

The others, we don’t need to worry about for this example. For more on User Roles, see our article on [**Managing User Roles**](https://support.optisigns.com/hc/en-us/articles/360046356113-Advanced-Security-Managing-User-Roles).

For this example, we’ve given Admin access to all our regional and local managers, as well as the store manager. A User has been added to the store as well, who will be able to add content and edit the screens only within that store.

|  |
| --- |
| **NOTE** |
| If you plan to add Users to the platform via SSO, you may skip this step. We’ve created the users above for demonstration purposes. |

Finally, ***Refresh your browser***. You’ll need to do this before the next step.

---

## Set Up Folder-Level Security

Now that we’ve made our Teams, it’s time to set up Folder Level security. We only want to grant access to screens that the users on the Team will actually use, and no more.

To do this, go to your **Screens** tab. Find the Folder you want to set permissions for. In this case, we’ll start with the **Pacific** folder at the top of the structure. Click the **Three Dots →  Change Permissions:**

![find change permission tab on folder](https://support.optisigns.com/hc/article_attachments/43657783484051)

The **Change Security** screen will appear. Click underneath where it says “Everyone on this team” and a list of Teams will appear. In our example, we’ll choose the **Pacific Region** team.

![how to change security permissions](https://support.optisigns.com/hc/article_attachments/43657783485715)

Now only the Pacific Region Team and the Default Team will have access to this folder. You can also choose whether to make this Folder and its subfolders Editable or View-only:

![edit and view permissions for folder](https://support.optisigns.com/hc/article_attachments/43657783486099)

Any folders created inside a folder will automatically inherit its permissions. However, if you’ve already created a folder and then change the parent folder permissions, those child folders will not inherit them.

### Complete Folder-Level Security Example

OptiSigns uses a top-down setup, meaning that the highest-level folders will need the most Teams with permissions.

To illustrate this, let’s go back to our example. Here is a partial nested setup:

![complete folder nesting setup](https://support.optisigns.com/hc/article_attachments/43657735762323)

Each layer will require fewer and fewer permissions. For example, here is the permission structure we’d want for the **Pacific** folder:

![regional level folder permissions example](https://support.optisigns.com/hc/article_attachments/43657783490451)

Note how ***every Team operating in the region*** has permissions for this folder.

As we go deeper into the nesting, we can eliminate teams that do not need certain permissions. For example, here are the Teams needing **California** folder permissions:

![state level folder security example](https://support.optisigns.com/hc/article_attachments/43657735765779)

Notice how we’ve filtered out the other State-level teams. This means that members of the Oregon or Washington teams will be able to enter the Pacific folder, but would ***not even see*** the California one.

Going a step further, here are the City/County level permissions we’d want on the **Los Angeles** folder:

![city level folder security example](https://support.optisigns.com/hc/article_attachments/43657783497363)

Here, we’ve filtered out Eagle Mountain (the other city-level team we’ve set up), but kept all the teams corresponding to Los Angeles area store locations. Going down to the **Cosmos Space Center** folder will complete the picture:

![store location folder security example](https://support.optisigns.com/hc/article_attachments/43657783497875)

All the other store locations have been filtered out. If we were to look at another store location, we’d exchange the Cosmos Space Center team for the team corresponding to that store. This way, the people assigned to the lowest level teams will only have access to the single folder that applies to them, but members of “higher level” teams will be able to see all the stores in their respective level.

|  |
| --- |
| **NOTE** |
| Another option: it is possible to restrict folder access to users within the Default Team. This is a good option if you want your regional managers to have more access. |

This can be applied across OptiSigns, and it is possible to create similar nesting within the **Files/Assets**, **Playlists**, and **Schedules** area of the Portal:

![add folder in files/assets area](https://support.optisigns.com/hc/article_attachments/43657735771923)

![add folders in playlist and schedule area](https://support.optisigns.com/hc/article_attachments/43657783499411)

For simplicity, we recommend mirroring the same setup in each of these areas. This way, higher-level teams can share content, playlists, or schedules with many lower-level teams, but lower-level teams cannot share with each other.

Lastly, when creating a New Folder, these permissions can be set by clicking the **Advanced** button:

![new folder advanced opened](https://support.optisigns.com/hc/article_attachments/43657783500051)

---

## Branding and Enforcing Brand Guidelines (Optional)

There are two parts to enforcing brand guidelines in OptiSigns: creating a branded portal, and enforcing brand guidelines on created content.

We have articles on each of these topics that explore them in more detail:

- [**Custom Branding Settings**](https://support.optisigns.com/hc/en-us/articles/1500000485202-Custom-Branding-Settings)
- [**Brand Kit and Enforcing Brand Guidelines**](https://support.optisigns.com/hc/en-us/articles/42313875427859-Brand-Kit-and-Enforcing-Brand-Guidelines)

Once configured, you’re ready to invite users.

---

## Adding Users: Via SSO, or Directly Via OptiSigns

To add users via OptiSigns, go back to where you created the Teams. You can **Add** or **Invite** users from here. See [**Managing User Roles**](https://support.optisigns.com/hc/en-us/articles/360046356113-Advanced-Security-Managing-User-Roles)for more information.

However, for our example, our hypothetical restaurant chain wants to enforce SSO via SAML.

To do this, go to our [**SSO & SAML**](https://support.optisigns.com/hc/en-us/sections/26319189062803-SSO-SAML)section and follow the appropriate article. We highly recommend reading our [**SAML best practices**](https://support.optisigns.com/hc/en-us/articles/4407128433299-SAML-integration-strategy-best-practice)article, as well.

### That’s all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
