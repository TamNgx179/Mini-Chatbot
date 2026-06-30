# How to mix playlists and maintain screen time share with OptiSigns Content Rotation App

Article URL: https://support.optisigns.com/hc/en-us/articles/1500001561861-How-to-mix-playlists-and-maintain-screen-time-share-with-OptiSigns-Content-Rotation-App
Article ID: 1500001561861
Last Updated: 2025-09-02T19:32:41Z

|  |
| --- |
| **Important Note (7/3):** We have recently disabled our Content Rotation App, and we highly recommend using our similar[**Sub-playlist Control feature,**](https://support.optisigns.com/hc/en-us/articles/22474034993043) available in our Pro-Plus and above plans. |

Content Rotation App will allow you to mix content between 2 or more playlists and ensure a distribution of screen time for each playlists.

A real world scenario would be: there are 2 Departments each maintain a playlist: Department A and Department B.  
As Admin, you want both to have 50% of screen time each (i.e. ensure 1 department do not make long content, video and consume all the screen time).

With Content Rotation app, you can

## **Let's jump in and get started:**

First, you will need to have two or more playlists. For more information on how to do that, click [here](https://support.optisigns.com/hc/en-us/articles/28295104605843).

Go to Files/Assets, Click on "App".

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/360100601834)

Click Content Rotation app:

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/1500001706142)

Click Add Playlist to add the playlist you want to rotate, in this example we put 2 playlists: Department A, Department B. You can add as many playlist as you want.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/1500001572662)

- Name: This is the name to organize assets, it will not be shown on the screen.
- Add Playlist:

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/360102767433)

- - Playlist: Select your playlist.
  - Rotate Every\*: 1 means the system will play 1 items on this playlist then move on to next playlist
  - Each Item Duration\*: Set duration for each items, this is required in case one playlist has a very long video for example, this will ensure screen time is still allocated fairly between playlists.

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/1500001572702)

- Enforce each item duration limit: Force each asset's playing time is same as Each Item Duration time. When this is checked, you will need to select how you want to handle when an item's duration is less than "Each item duration":
  - Move to next: If an item's duration is less than "Each item duration", it will move to next
  - Repeat: If an item's duration is less than "Each item duration", it will repeat the same asset until the "Each item duration" is over.

Click Save.  
After Saving, you can Preview the Content Rotation to see how the system mix the playlist.

## **That's all! Congratulation!**

You have added a Content Rotation app.

You can assign the newly created Content Rotation asset to your screen by going to Screens, click Edit screens and assign the asset to screens that you want.

**If you really curious about how the system mix the playlist, you can check out these cases:**

**Case 1**- Enforce each item duration limit = checked + Repeat (This is the default case)   
Playlist A -> 5 items: Rotate A: 1 item - 20s  
A1: 10s  
A2: 20s  
A3: 15s  
A4: 10s  
A5: 50s

Playlist B -> 3 items, Rotate B: 1 item - 20s  
B1: 10s  
B2: 40s  
B3: 5s

Result:  
A1: 20s  
B1: 20s

A2: 20s  
B2: 20s

A3: 20s  
B3: 20s

A4: 20s  
B1: 20s

A5: 20s  
B2 20s

**Case 2**- Enforce each item duration limit = checked + Move to next

Playlist A -> 5 items: Rotate A: 1 item - 20s

A1: 10s  
A2: 20s  
A3: 15s  
A4: 10s  
A5: 50s

Playlist B -> 3 items, Rotate B: 1 item - 20s

B1: 10s  
B2: 40s  
B3: 5s

Result:

A1: 10s  
B1: 10s

A2: 20s  
B2: 20s

A3: 15s  
B3: 5s

A4: 10s  
B1: 10s

A5: 20s  
B2 20s

**Case 3**- Enforce each item duration limit = checked + Repeat

Playlist A -> 5 items: Rotate A: 2 item - 20s

A1: 10s  
A2: 20s  
A3: 15s  
A4: 10s  
A5: 50s

Playlist B -> 3 items, Rotate B: 1 item - 20s

B1: 10s  
B2: 40s  
B3: 5s

Result:

A1: 20s  
A2: 20s  
B1: 20s

A3: 20s  
A4: 20s  
B2: 20s

A5: 20s  
A1: 20s  
B3: 20s

A2: 20s  
A3: 20s  
B1: 20s

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
