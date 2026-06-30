# Tutorial: Create, Update, Add, Remove items from Playlists

Article URL: https://support.optisigns.com/hc/en-us/articles/4414558295955-Tutorial-Create-Update-Add-Remove-items-from-Playlists
Article ID: 4414558295955
Last Updated: 2025-09-04T19:02:46Z

In this tutorial, we will walk through how to create a playlist and manage the assets assigned to the playlist through the API. Generally, it involves 4 steps.  Firstly, you will need to create a playlist. Secondly, you will need to add content to the playlist. Then you can update the playlist items to change the setting of the playlist items, e.g. change the play duration. Lastly, you can remove the contents from the playlist.

#### **1. Create a playlist**

To create a playlist, you will need to use the savePlaylist mutation. And supply the playlist name as a arguments in the payload. If it runs successfully, it will return the requested data from the server, and an id will be assigned to the playlist. This id will be needed in the next step when assigning contents to the playlist.

```json
mutation {  
  savePlaylist(payload:{name:"demo_playlist"}){  
          _id,  
          name,  
          path,  
          assets{  
            _id,  
          	fileType,  
            filename,  
          	duration,  
          	appType  
          },  
          teamId,  
          tags  
  }  
}
```

![](https://support.optisigns.com/hc/article_attachments/36563851116179)

#### **2. Assign contents to the playlist**

To assign the contents to the playlist, you can use the addPlaylistItems mutation. You will need to supply the playlist id retrieved from the above step, and also provide the asset id in the payload.

```json
mutation {  
  addPlaylistItems(_id:"4Xt7P6eYJGc4bXjR8",payload:{  
    ids: ["uRQynMhDsJ6QY35Wf",  
          "6744ff5add229e00123cf5e6"],  
    pos: 1  
  }){  
          	_id,  
          	fileType,  
          	filename,  
          	duration,  
          	appType  
  }  
}
```

![](https://support.optisigns.com/hc/article_attachments/36563843298579)

#### **3. Change the duration of the content in the playlist**

To change the duration of the assets in the playlist, you can use the updatePlaylistItems mutation. You will need to supply the playlist id retrieved from the above step, and also provide the duration and position of the asset in the playlist that you want to apply the change to in the payload.

```json
mutation {  
  updatePlaylistItems(_id:"4Xt7P6eYJGc4bXjR8",payload:{  
    items:  [{item: {duration:15}, pos: [0,1]}]  
  }){  
            _id,  
            fileType,  
            filename,  
            duration,  
            appType  
  }  
}
```

![](https://support.optisigns.com/hc/article_attachments/36563843301523)

Now, you can see the demo\_playlist is created in the account with the selected assets. And the duration of the items are set to 15 seconds.

![](https://support.optisigns.com/hc/article_attachments/36563843314195)

#### **4. Remove the content from the playlist**

To remove the contents from the playlist, you can use the removePlaylistItems mutation. You will need to supply the playlist id retrieved from the above step, and also provide the position of the asset in the playlist that you want to remove in the payload.

```json
mutation {  
  removePlaylistItems(_id:"d87B9ARKPyH8YYBbs",payload:{pos: [0,1]}){  
            _id,  
            fileType,  
            filename,  
            duration,  
            appType  
  }  
}
```

![](https://support.optisigns.com/hc/article_attachments/36563851134995)

Now you can see, the first 2 assets in the playlist are removed from the playlist.

![](https://support.optisigns.com/hc/article_attachments/36563851142291)

**Previous Article - [Tutorial: Pair and Assign Content to Screen](https://support.optisigns.com/hc/en-us/articles/4414553099667-GraphQL-API-Tutorial-Pair-and-Assign-Content-to-Screen)**

**Next Article - [Tutorial: Creating or Updating Website Assets Using GraphQL](https://support.optisigns.com/hc/en-us/articles/36562094987795-Tutorial-Creating-or-Updating-Website-Assets-Using-GraphQL)**
