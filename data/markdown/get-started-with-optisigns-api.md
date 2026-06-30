# Get Started with OptiSigns API

Article URL: https://support.optisigns.com/hc/en-us/articles/4414563863827-Get-Started-with-OptiSigns-API
Article ID: 4414563863827
Last Updated: 2025-11-06T16:52:11Z

The easiest way to get started with the development is to use the provided web-based GraphQL IDE.  You can access it from here.  
<https://graphql-gateway.optisigns.com/graphql>

You also will need API key to provide authorization to your account. You can learn how to get your API key from [here](https://support.optisigns.com/hc/en-us/articles/4414563797139-Generate-Manage-OptiSigns-API-Key).

#### **Query and Mutation**

GraphQL provides two ways than you can interact with your data. Query is used to read or fetch data from the server. Mutation is used to modify or post data to the server.

#### **Fetch the devices**

This query will list all the devices available in your account. You can specify what fields you are interested and get it returned from the result.

```json
query{  
  devices (query : {}) {  
    page{  
      edges{  
        cursor,  
        node{  
          _id,  
          deviceName,  
          UUID,  
          pairingCode,  
          currentType,  
          currentAssetId,  
          currentPlaylistId,  
          localAppVersion,  
        }  
      }  
    }  
  }  
}
```

![](https://support.optisigns.com/hc/article_attachments/36565329200147)

#### **Fetch a specific asset**

If you want to fetch the data following a condition, you can do so by supply an argument. This query will get the asset named "Houston Weather Test" in your account.

```json
query{  
  assets (query : {originalFileName:"Houston Weather Test"}) {  
    page{  
      edges{  
        cursor,  
        node{  
          _id,  
          appType,  
          fileType,  
          name,  
          filename  
        }  
      }  
    }  
  }  
}
```

![](https://support.optisigns.com/hc/article_attachments/36565329203091)

**Previous Article - [Generate and Manage API Key](https://support.optisigns.com/hc/en-us/articles/4414563797139-Generate-Manage-OptiSigns-API-Key)**

**Next Article - [GraphQL API Tutorial: Pair and Assign Content to Screen](https://support.optisigns.com/hc/en-us/articles/4414553099667-GraphQL-API-Tutorial-Pair-and-Assign-Content-to-Screen)**
