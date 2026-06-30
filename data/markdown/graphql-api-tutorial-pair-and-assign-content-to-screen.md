# GraphQL API Tutorial: Pair and Assign Content to Screen

Article URL: https://support.optisigns.com/hc/en-us/articles/4414553099667-GraphQL-API-Tutorial-Pair-and-Assign-Content-to-Screen
Article ID: 4414553099667
Last Updated: 2025-09-04T18:53:07Z

In this tutorial, we will walk through how to get a new screen paired and assign content making it ready to use through the API. Generally, it involves 2 steps.  Firstly, you will need to get the screen paired to your account. Then you will need to update the screen to rename it, and assign the content to be played on the screen.

#### **1. Pair screen**

To pair a screen, you will need to use the pairDevice mutation. And supply the pairing code you get from the screen as a arguments in the payload. If it runs successfully, it will return the requested data from the server, and an id will be assigned to the screen. This id will be needed in the next step to rename and assign the content to the screen.

```json
mutation {  
  pairDevice(payload:{pairingCode:"3JRKC8"}){  
          _id,  
          deviceName,  
          UUID,  
          pairingCode,  
          currentType,  
          currentAssetId,  
          localAppVersion  
  }  
}
```

![](https://support.optisigns.com/hc/article_attachments/36564341500819)

#### **2. Rename the paired screen and assign asset/playlist to the screen**

To change the screen name or change the content assigned to the screen, you can use the updateDevice mutation. You will need to supply the screen id retrieved from the above step, and specify how you would like to change the device in the payload.

```json
mutation {  
  updateDevice(_id:"6682d6d553fca60012953e17",payload: {deviceName: "GraphAPI Test",  
    currentType: ASSET,  
    currentAssetId: "uRQynMhDsJ6QY35Wf",  
    orientation: LANDSCAPE}){  
          _id,  
          deviceName,  
          UUID,  
          pairingCode,  
          currentType,  
          currentAssetId,  
          localAppVersion  
  }  
}
```

![](https://support.optisigns.com/hc/article_attachments/36564341502611)

To assign a playlist to the screen, it is about the same as assign asset to screen. Just need to change the currentType to PLAYLIST, and supply the playlist id.

```json
mutation {  
  updateDevice(_id:"6126edf99834540019b30ff1",payload: {deviceName: "GraphAPI Test",  
    currentType: PLAYLIST  
    currentAssetId: "d87B9ARKPyH8YYBbs",  
    orientation: LANDSCAPE}){  
          _id,  
          deviceName,  
          UUID,  
          pairingCode,  
          currentType,  
          currentAssetId,  
          localAppVersion  
  }  
}
```

![](https://support.optisigns.com/hc/article_attachments/36564341504915)

**Previous Article - [Get Started](https://support.optisigns.com/hc/en-us/articles/4414563863827-Get-Started)**

**Next Article - [Tutorial: Create, Update, Add, Remove Items from Playlists](https://support.optisigns.com/hc/en-us/articles/4414558295955-Tutorial-Create-Update-Add-Remove-items-from-Playlists)**
