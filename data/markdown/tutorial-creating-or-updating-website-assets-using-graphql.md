# Tutorial: Creating or Updating Website Assets Using GraphQL

Article URL: https://support.optisigns.com/hc/en-us/articles/36562094987795-Tutorial-Creating-or-Updating-Website-Assets-Using-GraphQL
Article ID: 36562094987795
Last Updated: 2025-09-04T18:54:21Z

Using GraphQL, it is possible to create a website asset on OptiSigns.

|  |
| --- |
| **NOTE** |
| At this time, this Mutation is primarily used to create or update Website assets. |

**1. Creating a New Website Asset**

To do this, we’ll need to create a specific Mutation:

```
mutation saveAsset ($payload: AssetInput!, $teamId: String)  
{saveAsset (payload:$payload,teamId:$teamId){  
  _id  
  originalFileName  
  webLink  
  webType  
  fileType  
  }  
}
```

**Variables:**

```
{  
  "payload": {  
    "originalFileName": "",  
    "webLink": "",  
    "webType": "",  
    "fileType": ""  
  }  
}
```

![](https://support.optisigns.com/hc/article_attachments/36562094972435)

This Mutation, once run, will create a new asset:

![](https://support.optisigns.com/hc/article_attachments/36562091083539)

This asset can now be assigned to a device, queried for additional information, or added to a playlist or schedule.

**2. Updating Assets**

Updating assets is as simple as running the same Mutation while providing an \_id field. This can be done for any asset type, not just website assets, but we will be using a website asset as an example.

**Variables:**

```
{  
  "payload": {  
    "_id": "",  
    "originalFileName": "",  
    "webLink": "",  
    "webType": "",  
    "fileType": ""  
  }  
}
```

![](https://support.optisigns.com/hc/article_attachments/36562091085843)

**Previous Article - [Tutorial: Create, Update, Add, Remove Items from Playlists](https://support.optisigns.com/hc/en-us/articles/4414558295955-Tutorial-Create-Update-Add-Remove-items-from-Playlists)**

**Next Article - [Tutorial: Creating Schedules and Adding Schedule Items Using GraphQL](https://support.optisigns.com/hc/en-us/articles/36558834998291-Tutorial-Creating-Schedules-and-Adding-Schedule-Items-Using-GraphQL)**
