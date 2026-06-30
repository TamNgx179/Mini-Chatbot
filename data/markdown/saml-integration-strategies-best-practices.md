# SAML Integration Strategies & Best Practices

Article URL: https://support.optisigns.com/hc/en-us/articles/4407128433299-SAML-Integration-Strategies-Best-Practices
Article ID: 4407128433299
Last Updated: 2026-02-05T20:22:33Z

There are many ways to implement SAML to manage users and access OptiSigns with your IDP.

Here are some high-level best practices with OptiSigns that will help to plan your integration and reduce overhead and manual work later.

This article focuses on integration strategies and approaches. For detailed step-by-step configurations by platform, see one of our guides:

- [SAML SSO with Okta](https://support.optisigns.com/hc/en-us/articles/4404590815635-How-to-set-up-SAML-2-0-with-OptiSigns-and-Okta)
- [SAML SSO with MS Entra ID](https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD)
- [SAML SSO with OneLogin](https://support.optisigns.com/hc/en-us/articles/4407386819731-How-to-set-up-SAML-2-0-with-OptiSigns-and-OneLogin)
- [SAML SSO with OneLogin (Shibboleth)](https://support.optisigns.com/hc/en-us/articles/4407476403859-How-to-set-up-SAML-2-0-with-OptiSigns-and-OneLogin-Shibboleth)
- [SAML SSO with Google Workspace](https://support.optisigns.com/hc/en-us/articles/4407493404307-How-to-set-up-SAML-2-0-with-OptiSigns-and-Google-Workspace)

## **Create a backup Admin account during set up:**

During set up, we recommend leaving Enable Username & Password login, and creating an Admin account with username/password to log back in and config, in case you accidentally lock yourself out by missing assignments of roles or groups.

You can disable this account later once your implementation is completed.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4407128153235)

In this case, you are planning not to use email as the unique identifier for the user, and use a username or employee ID instead. We recommend having this on, so the account owner and admin account will be able to manage the account without interruption, e.g. forgetting the password, or an issue with identifying the provider.

## **Strategies for using SAML:**

#### **1) As an Authentication & Authorization Service (RECOMMENDED)**

SAML can be used to enforce identity verification, but also to enforce user, team, and role mapping in OptiSigns.

With this approach you will map all users to groups in your IDP, and map the IDP groups to OptiSigns teams/roles. When there's a change in IDP (for example, a user is added or changes groups), it will automatically reflect in OptiSigns.

To implement this, check **Enable User Override**. When checked, every time a user logs in using SAML, OptiSigns will check to see if their name or group assignment has changed. It will then enforce that accordingly. If their name or assignment has updated, it will also update OptiSigns.

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4407135779603)

Map all your appropriate groups to roles & teams in OptiSigns.

For example we have 3 groups:

- Marketing West Coast - users responsible for managing screens, content for West region
- Marketing East Coast - user responsible for manage screens, content for East region
- IT Support - Admin that can support both region and do other admin tasks

The mapping should be like below:

|  |  |
| --- | --- |
| **OKTA** | **ENTRA** |
| mceclip3.png | For Entra, your "Group Name" within OptiSigns corresponds to your "Object ID" within Entra. See [our article](https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD#AssignMap) for more information. |

With this set up, let's say a user belongs to Marketing West Coast. You want to move them to Marketing East Coast. Simply update your IDP and move them from West Coast to East Coast. The next time they log in to OptiSigns, that will be reflected and they will belong to the Marketing West Coast team and can only see that content in OptiSigns.

For more on User Management, see our article on [**Teams and Folder Security**](https://support.optisigns.com/hc/en-us/articles/43657735780627-User-Management-Example-Chain-Restaurant-or-Retail-Store-with-Multiple-Locations)in OptiSigns.

#### **2) As Authentication Service Only**

SAML can be used to enforce your MFA, Password policy, and remove users and revoke access to OptiSigns. You can still manage these users and assign them to Teams or Roles. This approach is quick to set up and flexible as you can quickly move users around in OptiSigns. However, when users move around in your IDP, you will have to remember to move them around in OptiSigns as well, if required.

To implement this, uncheck **Enable User Override.**

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/4407136124435)

Going back to our earlier example: when a user moves from Marketing West Coast to Marketing East Coast, you will need to go to OptiSigns and move the user's team assignment, if necessary.

Also if when the user update, change their name, you will have to update OptiSigns as well to keep it in sync.

#### **Enable User Creation:**

We recommend keeping this option checked. When enabled, if users are authenticated and SAML maps the user to a team or role that can use OptiSigns, the user will be created automatically.

If disabled, you will have to create each user first in OptiSigns before they can log in with SAML SSO.

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/4407136156819)

Going back to our old example. Let's say there are 20 users belong to Marketing West Coast group in your IDP, and Marketing West Coast is mapped to the Marketing West Coast team in OptiSigns.

If a user in Marketing West Coast group logs in to OptiSigns, they will be automatically created and can immediately access West Coast Team screens and content.

The other 19 users are not created in OptiSigns until they attempt to log in.

You can also map **Unmapped users/groups** to **No Team (Disable)**. This way, if a user belongs to some other group in your IDP and tries to log in, they will get an error and the user is not created in OptiSigns.

This way you can keep the system clean and only users needing access to the app are replicated.

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/4407136240659)

If you have any questions or need help with SAML integration please feel free to reach out to us at [support@optisigns.com](mailto:support@optisigns.com)
