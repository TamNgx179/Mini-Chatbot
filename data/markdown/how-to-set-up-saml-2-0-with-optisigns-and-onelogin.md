# How to set up SAML 2.0 with OptiSigns and OneLogin

Article URL: https://support.optisigns.com/hc/en-us/articles/4407386819731-How-to-set-up-SAML-2-0-with-OptiSigns-and-OneLogin
Article ID: 4407386819731
Last Updated: 2025-09-04T13:48:07Z

With Pro Plus and Enterprise plan, you can configure SAML 2.0 with OptiSigns via OneLogin.

OneLogin will be acting as the IDP (Identify Provider), and OptiSigns will be working as the SP(Service Provider).

### **Set up OptiSigns & OneLogin:**

**First you need to do some set up in OptiSigns:**

If you don't have a sub domain yet, you can set up one by going to:  
<https://app.optisigns.com/app/s/branding-settings>

Fill in subdomain field and click Activate. After that you can use this sub domain for "  
You can also map your own domain like digitalsigns.yourcompany.com by following this [article](https://support.optisigns.com/hc/en-us/articles/1500000480302).

This will be the URL that you can share with your users so they can log in to use the app, once integration has set up. In our example we will use <https://advanced.optisigns.net/>

![mceclip13.png](https://support.optisigns.com/hc/article_attachments/19053401939731)

Next go to SAML Single Sign On setting page:

<https://app.optisigns.com/app/s/saml-settings>

Click Enable SAML SSO.

The settings are:

- Enable Username & Password login: Allow users to also log in with username/password. It’s recommended to disable once integration is all done. As Admin/Owner, it's recommended that you keep at least 1 account with password log in, in case there's issues, you can always log back in from app.optisigns.com to reconfigure.
- Enable User Creation: If users are authenticated, but do not exist in OptiSigns, they will be created in OptiSigns. You should enable this, because you likely already assign/approve users/groups to use OptiSigns, unless for some reason you want to be very strict and want to review roles of users before they can start using OptiSigns.
- Enable User Override: Every time a user logs in, if their group assignment have changed on SAML, OptiSigns will update, override new profile settings.
- Note the "Single Sign On URL" and "Audience URI (SP Entity ID) URL", you will need this to use in OneLogin later.

![](https://support.optisigns.com/hc/article_attachments/19053301304083)

**Next, add OptiSigns as an App in your OneLogin admin portal:**

Log in to your OneLogin portal as admin -> Applications

Click Add app

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4407386965907)

On the next page, search for "SAML" in the search box, and then select the "SAML Custom Connector (Advanced)".

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4407387031315)

Enter "OptiSigns" in the display name, then click Save. You can also upload the OptiSigns logo here as well.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/4407392839187)

After saving, go to the configuration page. This is where you should provide the Single Sign On URL, and SP Entity ID you get from your OptiSigns SAML SSO setting.

- SP Entity ID from OptiSigns SAML SSO setting should be put under **Audience (EntityID)** and **Login URL**.
- Single Sign On URL from OptiSigns SAML SSO setting should be put under **Recipient**, **ACS URL validator,** and **ACS URL**.
- Change the **SAML initiator** to the **Service Provider**

![](https://support.optisigns.com/hc/article_attachments/19053399114899)

Then go to the SSO page. Get these 3 highlighted information, these need to be maintained in the OptiSigns SAML SSO settings. After clicking View Details of the certificate, you can find the encoded content of the certificate, this will be needed in the next step.

![](https://support.optisigns.com/hc/article_attachments/19053348948883)

Go back to your OptiSigns account maintain above mentioned 3 fields, and save it.

Put the SAML 2.0 endpoint from OneLogin under the SAML 2.0 Endpoint.

Put the Issuer URL from OneLogin under Identity Provider Issuer.

Put the content from base64 encoded x509 certificate under Public Certificate.

![](https://support.optisigns.com/hc/article_attachments/19053330062483)

Now your login portal & integration are all setup.

#### **Assign & map users, and groups from OneLogin to OptiSigns**

It's not required, but recommended to create groups of users to be assigned, and map to OptiSigns Roles, and Teams so they will automatically have the right role & group.

**IMPORTANT NOTE: If you don't configure this, all users will be assigned User Role & Default Team (screenshot see below)**

To configure how OptiSigns should map the user groups to OptiSigns Roles by going to: <https://app.optisigns.com/app/s/saml-settings>

Scroll to Advanced Settings and create a mapping.  
Group Name (roles assigned to the user from OneLogin), Role (role in OptiSigns) mapping.   
![mceclip9.png](https://support.optisigns.com/hc/article_attachments/4407387515155)

It's best practice to create a group specifically for OptiSigns with name prefix with OptiSigns- and map to OptiSigns like below:

- optisigns-admins (SAML group) -> OptiSigns role: Admin
- optisigns-users (SAML group) -> OptiSigns role: Users
- optisigns-custom-role (SAML group) -> OptiSigns custom role that you create

**How to handle Unmapped users/groups:**

You can map the "Unmapped users/group" to No Team (Disabled)

This way they will receive an error when trying to log in and will have to reach out to Admins to get correct teams, and roles assigned. This can be used as a safeguard, in case some users accidentally get assigned OptiSigns app but not the right groups.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/19053410145299)

Note that if you map a SAML group to a Team and then delete the team, it will result in the new user being mapped to No Team and will have to contact you to be assigned to a team to use the app.

Next, go to your OneLogin portal. Go to the parameters page of the OptiSigns application. This is where you maintain the mapping of the attributes.

Create new custom parameters here by clicking the + icon. Currently, OptiSigns support attributes mapping of first name, last name, and group. You can set the customer parameter name to the same default attribute name used on OptiSigns, and then assign it to the corresponding values from OneLogin.

These mappings will pass information to OptiSigns on the user's Name and Group.

![mceclip7.png](https://support.optisigns.com/hc/article_attachments/4407387440147)

The parameter names are corresponding to OptiSigns

<https://app.optisigns.com/app/s/saml-settings>

OptiSigns accept firstName, lastName, and group by default. Instead of setting the parameter names to the default attribute name used on OptiSigns,  you can also change the attribute name on OptiSigns to match the parameter names you defined on OneLogin as well.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/19053401940243)

### **That's it!**

You have configured SAML 2.0 for OptiSigns with OneLogin.

Now your users can log in using the subdomain that you configured (in this case it was <https://advanced.optisigns.net/signIn>).

You can share the URL with your users and they can log in with their SSO credentials.

If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
