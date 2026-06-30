# How to set up SAML 2.0 with OptiSigns and OneLogin(Shibboleth)

Article URL: https://support.optisigns.com/hc/en-us/articles/4407476403859-How-to-set-up-SAML-2-0-with-OptiSigns-and-OneLogin-Shibboleth
Article ID: 4407476403859
Last Updated: 2025-09-02T20:38:51Z

With Pro Plus and Enterprise plans, you can configure SAML 2.0 with OptiSigns via OneLogin using Shibboleth. Shibboleth is based on SAML, the setup of the authentication using the Shibboleth connector on OneLogin will be similar to the normal SAML connector.

OneLogin will be acting as the IDP (Identity Provider), and OptiSigns will be working as the SP(Service Provider).

### **Set up OptiSigns & OneLogin:**

**First, you need to do some setup in OptiSigns:**

If you don't have a subdomain yet, you can set up one by going to:  
<https://app.optisigns.com/app/s/branding-settings>

Fill in the subdomain field and click Activate. After that, you can use this subdomain for "  
You can also map your own domain like digitalsigns.yourcompany.com by following this [article](https://support.optisigns.com/hc/en-us/articles/1500000480302).

This will be the URL that you can share with your users so they can log in to use the app, once integration has set up. In our example, we will use <https://advanced.optisigns.net/>

![mceclip13.png](https://support.optisigns.com/hc/article_attachments/21286528904211)

Next, go to the SAML Single Sign On setting page:

<https://app.optisigns.com/app/s/saml-settings>

Click Enable SAML SSO.

The settings are:

- Enable Username & Password login: Allow users to also log in with username/password. It’s recommended to disable it once the integration is all done. As Admin/Owner, it's recommended that you keep at least 1 account with a password login, in case there are issues, you can always log back in from app.optisigns.com to reconfigure.
- Enable User Creation: If users are authenticated, but do not exist in OptiSigns, they will be created in OptiSigns. You should enable this, because you likely already assign/approve users/groups to use OptiSigns, unless for some reason you want to be very strict and want to review the roles of users before they can start using OptiSigns.
- Enable User Override: Every time a user logs in, if their group assignment has changed on SAML, OptiSigns will update, and override new profile settings.
- Note the "Single Sign On URL" and "Audience URI (SP Entity ID) URL", you will need this to use in OneLogin later.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/21286544103571)

**Next, add OptiSigns as an App in your OneLogin admin portal:**

Log in to your OneLogin portal as admin -> Applications

Click Add app

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/4407476998035)

On the next page, search for "SAML" in the search box, and then select the "SAML Custom Connector (SP Shibboleth)".

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4407468255507)

Enter "OptiSigns" in the display name, then click Save. You can also upload the OptiSigns logo here as well.

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4407476590867)

After saving, go to the configuration page. This is where you should provide the Single Sign On URL, and SP Entity ID you get from your OptiSigns SAML SSO setting.

SP Entity ID from OptiSigns SAML SSO setting should be put under the Login URL.

Single Sign On URL from OptiSigns SAML SSO setting should be put under ACS URL and ACS URL validator. Please remember to escape the special character in the ACS URL validator.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/4407476626451)

Then go to the SSO page. Get these 3 highlighted information, these need to be maintained in the OptiSigns SAML SSO settings. After clicking View Details of the certificate, you can find the encoded content of the certificate, this will be needed in the next step.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/4407476684179)

Go back to your OptiSigns account maintain above mentioned 3 fields, and save it.

Put the SAML 2.0 endpoint from OneLogin under the SAML 2.0 Endpoint.

Put the Issuer URL from OneLogin under Identity Provider Issuer.

Put the content from base64 encoded x509 certificate under Public Certificate.

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/21286544110099)

Now your login portal & integration are all set up.

#### **Assign & map users, and groups from OneLogin to OptiSigns**

It's not required, but recommended to create groups of users to be assigned, and map to OptiSigns Roles, and Teams so they will automatically have the right role & group.

**IMPORTANT NOTE: If you don't configure this, all users will be assigned User Role & Default Team (screenshot see below)**

To configure how OptiSigns should map the user groups to OptiSigns Roles by going to: <https://app.optisigns.com/app/s/saml-settings>

Scroll to Advanced Settings and create a mapping.  
Group Name (roles assigned to the user from OneLogin), Role (role in OptiSigns) mapping.   
![mceclip9.png](https://support.optisigns.com/hc/article_attachments/21286528943635)

It's best practice to create a group specifically for OptiSigns with name prefix with optisigns- and map to OptiSigns like below:

- optisigns-admins (SAML group) -> OptiSigns role: Admin
- optisigns-users (SAML group) -> OptiSigns role: Users
- optisigns-custom-role (SAML group) -> OptiSigns custom role that you create

**How to handle Unmapped users/groups:**

You can map the "Unmapped users/group" to No Team (Disabled)

This way they will receive an error when trying to log in and will have to reach out to Admins to get correct teams, and roles assigned. This can be used as a safeguard, in case some users accidentally got assigned OptiSigns app but not the right groups.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/26504504778259)

Note that if you map a SAML group to a Team and then delete the team, it will result in the new user being mapped to No Team and will have to contact you to be assigned to a team to use the app.

Next, go to your OneLogin portal. Go to the parameters page of the OptiSigns application. This is where you maintain the mapping of the attributes.

Create new custom parameters here by clicking the + icon. Currently, OptiSigns support attributes mapping of first name, last name, and group. You can set the customer parameter name to the same default attribute name used on OptiSigns, and then assign it to the corresponding values from OneLogin.

Shibboleth has many predefined standard attributes. In this case, the givenName can be mapped to firstName on OptiSigns, and the surname can be mapped to lastName on OptiSigns.

These mappings will pass information to OptiSigns on the user's Name and Group.

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/4407468380563)

The parameter names are corresponding to OptiSigns

<https://app.optisigns.com/app/s/saml-settings>

OptiSigns accept firstName, lastName, and group by default. Instead of setting the parameter names to the default attribute name used on OptiSigns,  you can also change the attribute name on OptiSigns to match the parameter names you defined on OneLogin as well.

Shibboleth uses standard namespace and id for the predefined standard attributes. In the case of names, the id should be used in the attributes mapping on OptiSigns.

firstName (givenName) : urn:oid:2.5.4.42

lastName (surname):urn:oid:2.5.4.4

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/4407468403219)

### **That's it!**

You have configured SAML 2.0 for OptiSigns with OneLogin using the Shibboleth connector.

Now your users can log in using the subdomain that you configured (in this case it was <https://advanced.optisigns.net/signIn>).

You can share the URL with your users and they can log in with their SSO credentials.

If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
