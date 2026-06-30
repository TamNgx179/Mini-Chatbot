# Error Handling

Article URL: https://support.optisigns.com/hc/en-us/articles/4414564078995-Error-Handling
Article ID: 4414564078995
Last Updated: 2025-09-11T14:10:24Z

Whenever our server encounters errors while processing a GraphQL operation, it will include an error object in the response. The error object has an error array that contains each error occured. Each error in the array has a message field that contains the error message, and an extensions field that provides additional useful information, including an error code.

When calling the GraphQL API, you will need to check the response for errors instead of the HTTP status. Below are some examples of an error.  
  
![](https://support.optisigns.com/hc/article_attachments/36565574448659)

![](https://support.optisigns.com/hc/article_attachments/36565574450579)

**Previous Article -** [**Pagination**](https://support.optisigns.com/hc/en-us/articles/4414558369811-Pagination)

**Next Article - [Subscription Function in GraphQL](https://support.optisigns.com/hc/en-us/articles/36558469962643-Subscription-Function-in-GraphQL)**
