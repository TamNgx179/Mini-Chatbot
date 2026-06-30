# Generate & Manage OptiSigns API Key

Article URL: https://support.optisigns.com/hc/en-us/articles/4414563797139-Generate-Manage-OptiSigns-API-Key
Article ID: 4414563797139
Last Updated: 2025-09-04T18:50:38Z

In order to use the API, you will need first get an API key. To get an API key, you can either use the link below, or click the **API Keys** button in the side menu of account management on the OptiSigns portal.

<https://app.optisigns.com/app/s/apikeys>

### 

### Create API Key

1. Click the **New API Key** button  
![optisigns new api key button](https://support.optisigns.com/hc/article_attachments/37490053477523)

2. Enter the API Key name, and select the scopes and permissions for the API key.  
![optisigns new api key setup](https://support.optisigns.com/hc/article_attachments/37490069231507)

3. Save the API key safely, the key will be used the access your account through API.

![optisigns api key token example](https://support.optisigns.com/hc/article_attachments/36565780216211)

### Use API Key

To use the API key, put it in the HTTP request header following this format.

Authorization: Bearer YOUR\_KEY\_HERE

In the OptiSigns GraphQL playground, you will be able to query your data if the API key is successfully added.

![optisigns graphql playground api key input](https://support.optisigns.com/hc/article_attachments/37490069240083)

**Previous Article - [Introduction](https://support.optisigns.com/hc/en-us/articles/4414552808467-Introduction)**

**Next Article - [Get Started](https://support.optisigns.com/hc/en-us/articles/4414563863827-Get-Started)**
