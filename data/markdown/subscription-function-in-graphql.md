# Subscription Function in GraphQL

Article URL: https://support.optisigns.com/hc/en-us/articles/36558469962643-Subscription-Function-in-GraphQL
Article ID: 36558469962643
Last Updated: 2025-09-04T15:00:36Z

Subscriptions are a query type that allows you to be notified when any changes are made to a device, asset, or playlist.

An example might be that you want to be notified of any changes made to your device, be that changing the asset or playlist. This can be done entirely within GraphQL by using queries to find the information about a device, setting up a subscription, then using mutations to alter the device attributes.

### **1. Set Up the Subscription**

```
subscription subscribe($_id:String,$type:OBJECT_TYPES){  
  
  subscribe(_id:$_id,type:$type){  
  
    _id,  
  
    mutation,  
  
    teamId  
  
    type  
  
  }  
  
}
```

**Variables**

```
{"_id":"",  
  
  "type": ""  
  
}
```

![](https://support.optisigns.com/hc/article_attachments/36558469943443)

Note the elements present in the Subscription query. These are the elements it will monitor, and return to you when any of them are changed via Mutation.

When a Subscription is properly input, you should see this on the right side of the GraphQL UI:

![](https://support.optisigns.com/hc/article_attachments/36558442820115)

This means, as long as the Subscription is active, it will report any changes to the item.

### **2. Testing the Subscription**

Here, we have a Mutation script that is changing the name and playlist on the selected device.

```
mutation updateDevice($_id: String!,$payload: UpdateDeviceInput!, $teamId: String){  
  updateDevice(_id:$_id,payload:$payload,teamId:$teamId){  
     _id,  
     deviceName,  
     UUID,  
     pairingCode,  
     currentType,  
     currentAssetId,  
     currentPlaylistId,  
     path,  
     localAppVersion  
  }  
}
```

**Variables**

```
{"_id": "",  
  "payload": {"deviceName": "",  
    "currentType": "",  
    "currentAssetId": “”,  
    "currentPlaylistId": "",  
    "orientation": "LANDSCAPE"  
  }   
} 
```

![](https://support.optisigns.com/hc/article_attachments/36558442824211)

When we perform this Mutation, we can switch over to where our Subscription is Listening and see this:

![](https://support.optisigns.com/hc/article_attachments/36558469955603)

**Previous Article - [Error Handling](https://support.optisigns.com/hc/en-us/articles/4414564078995-Error-Handling)**

**Next Article - [API Reference](https://support.optisigns.com/hc/en-us/articles/4414558392339-API-Reference)**
