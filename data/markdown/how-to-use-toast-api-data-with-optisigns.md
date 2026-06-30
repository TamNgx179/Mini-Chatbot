# How to use Toast API data with OptiSigns

Article URL: https://support.optisigns.com/hc/en-us/articles/31113088917907-How-to-use-Toast-API-data-with-OptiSigns
Article ID: 31113088917907
Last Updated: 2025-09-02T20:24:12Z

### Toast is one of the most common Point-of-Sale systems in North America. In this article, we'll explain how to set up API integration between your Toast system and OptiSigns.

- [Step 1: Preparation](#Step1)
- [Step 2: Authentication to Toast API](#Step2)
- [Step 3: Call the API to Get the Required Data from Toast](#Step3)
- [Step 4: Build the DMB Designer with OptiSync](#Step4)

Toast provides an API for users to integrate POS data with other systems. With OptiSync, building auto-updating digital menu boards from your Toast API's data is simple.

Toast API requires a dynamically generated authentication token to be supplied with every API call, unlike many other POS systems that use a static API key. This adds some complexity to the integration that other POS systems don't have. However, using OptiSigns' API request and OptiSync, these added complexities are no trouble at all.

In this article, we'll provide a step-by-step guide on how to integrate your Toast API using OptiSigns API request, and how to create a DMB using OptiSync. Below are the high level steps we will follow:

1. Get required information from Toast portal

2. Get the Authentication Token from Toast (Inside Pre-Request step)

3. Call the API to get the required data from Toast

4. Use Toast API data to build DMB in designer with OptiSync

---

## Step 1: Preparation

To get started with integrating a Toast API with OptiSigns, we need the following information from the Toast system:

- *toast-api-hostname*
- clientId
- clientSecret
- userAccessType

Refer to Toast's Documentation [here](https://doc.toasttab.com/doc/devguide/portalHowToBuildAToastIntegration.html) for further details.

|  |
| --- |
| **NOTE** |
| In order to use Toast's API to read data, this requires **[Toast Standard API access](https://doc.toasttab.com/doc/devguide/devApiAccessUserGuide.html).**This usually comes with an additional charge (to Toast) of $25/month per location. |

---

## Step 2: Authentication for Toast API

For Toast API authentication, we will first need to pass the POST request to get the authentication token. The authentication token is then used to pass in the API request to get the data from Toast menus, orders etc.

This authentication process will be handled using Pre-request processing with OptiSigns' API request. For more information about Pre-request processing and API requests in general, please check [here](https://support.optisigns.com/hc/en-us/articles/22875592994195).

In the Pre-request processing stage, the OptiSigns API calls the authentication API to get the necessary token, and sets it to the context of the API request.

In this example, the token is set to the context variable "authorization". When the API request is made, it will be able to use the authentication token. Below is a screenshot of this example in practice.

![](https://support.optisigns.com/hc/article_attachments/31870675893011)

Use this code snippet (with the data obtained earlier filling in the "xxx"s) to

```
const body = {  
"clientId": "xxx",  
"clientSecret": "xxx",  
"userAccessType": "xxx"  
};  
const {data, headers} = await os.postRequest("https://[toast-api-hostname]/authentication/v1/authentication/login", body );  
const token = os.getValue(data.token.accessToken);  
os.context.set("authorization", os.getValue(token));
```

---

## Step 3: Call the API to get the required data from Toast

Now we'll use the authorization token we received in Pre-request processing and pass it to the actual API call header.

In the Header tab, create two parameters with the following values:

**authorization** Bearer {{authorization}}

**Toast-Restaurant-External-ID**

You can get the **Toast-Restaurant-External-ID value** from Toast Portal. This is the specific restaurant Id you want to get data for.

![](https://support.optisigns.com/hc/article_attachments/31870675894035)

Now put the desired API URL from which you want to get data. In this example we have used the following API to get the menus

- - <https://ws-api.toasttab.com/menus/v2/menus>

The final request will look something like this:

![](https://support.optisigns.com/hc/article_attachments/31870675898515)

You can enable this request and save the API. Click **Run Test**.

You should receive a *(200 OK)* response, with data returning from the API. This means the API request has successfully contacted Toast and is transferring data.

![](https://support.optisigns.com/hc/article_attachments/31870683910291)

---

## Step 4: Build Digital Menu Board in Designer with OptiSync

Now that your API request data source is ready for use, you can build your DMB using Designer with OptiSync. OptiSync allows you to map the API data to an element in the designer, either text or images. Using Repeaters, this data can be used to build out multiple item menus, and you're also able to define how you'd like to handle sold-out items, specials, and more.

For a step-by-step guide and more examples, please see our article on [Building Digital Menu Boards Using OptiSync](https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync).

## That's all!

You have successfully retrieved data from Toast and displayed it on the screens using OptiSigns.
