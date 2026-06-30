# Animation

Article URL: https://support.optisigns.com/hc/en-us/articles/42305104960147-Animation
Article ID: 42305104960147
Last Updated: 2025-09-02T19:02:02Z

### In this article, we’ll go over how to add Animations to any part of your design.

- [How to Add Animations to Design Elements](https://support.optisigns.com/hc/en-us/articles/undefined#AddAnimations)
  - [Page Animations](#PageAnimations)
  - [Object Animations](#ObjectAnimations)
- [Common Issues with Animations](#CommonIssues)
  - [Preloading Assets to a Playlist](#PreloadingAssets)
  - [Device Performance](#DevicePerformance)

Animations are an effective way to display promotions, announcements, and messages. They draw the human eye with motion, causing people to naturally look toward its source. With Designer, it’s easy to add animations to your designs, bringing them more attention from visitors.

For an intro to using Designer, see our article on [**Getting Started with Designer**](https://support.optisigns.com/hc/en-us/articles/42087942047379-Getting-Started-with-Designer).

---

## How to Add Animations to Design Elements

Selecting the **Animate** button will allow you to add animations to your design elements.

![](https://support.optisigns.com/hc/article_attachments/42305104951699)

This button is also available per element.

Clicking it will open the **Animate** area on the Side Menu:

![](https://support.optisigns.com/hc/article_attachments/42305104952851)

In order to add an animation, you’ll need to select an element to animate. Then, decide whether to use a **Page Animation** or an **Object Animation**.

To demonstrate the differences between the two and how to best use them (together or separately), we’ll use a simple template design, like below:

![](https://support.optisigns.com/hc/article_attachments/42305104953619)

### Page Animations

**Page Animations** will animate in the order it is placed on the list. These also will animate only once, whenever the page loads.

For example, let’s say we want the water on our example template to fly in from the right - to give the appearance of splashing the water bottles.

First, select the element. Then, hit **Animate → Add** under the **Page Animations** section. This will bring up a whole mess of options:

![](https://support.optisigns.com/hc/article_attachments/42305100419987)

**Animation Types:**

- **Fade in**
- **Fade out**
- **Fly in from left**
- **Fly in from right**
- **Fly in from bottom**
- **Fly in from top**
- **Fly out to left**
- **Fly out to right**
- **Fly out to bottom**
- **Fly out to top**
- **Zoom in** - Briefly zooms the element in
- **Zoom out** - Briefly zooms the element out
- **Bounce X** - Bounce the element horizontally
- **Bounce Y** - Bounce the element vertically
- **Flash**
- **Zoom** - Alternates between zooming the element in and out
- **Spin left**
- **Spin right**

While we could provide detailed descriptions of each of these, it’s more fun to play around with them and see how they fit your vision for yourself!

**Animation Timing:**

- **After previous** - Sets the animation to trigger after the previous animation on the list.
- **With previous** - Sets the animation to trigger at the same time as the previous animation.
- **From beginning** - Sets the animation to trigger as soon as the asset loads.

**Delay (sec)** - How long of a delay between the asset loading/previous animation and the animation going off.

**Animation Speed** - Changes how quickly the animation moves.

|  |
| --- |
| **NOTE** |
| To properly utilize Animation Timing, you will need to coordinate your choice with the Delay option.  For example, say we have three page animations, **A, B, and C**.   - A will go first, right when the page loads. No delay is needed. - B is set to "After previous" in order to follow A. Setting a Delay of 1s will cause B to animate 1s ***after*** A animation ends. - C we want to fire at the same time as B. We select "With previous."   - With no delay, this will cause it to fire right as the B animation ends, causing it to look wrong.   - To fix this, we will need to set a delay of 1s (assuming Animation Speed is also 1). This will cause C to fire 1s ***before*** the B animation ends, timing it properly. |

Once an animation is added, more can be created. The list of animations can be reordered via drag and drop:

![](https://support.optisigns.com/hc/article_attachments/42305104954643)

|  |
| --- |
| **NOTE** |
| The order the Animations are dragged in does not override their timing to display. For example, if you have three animations and one is set to display "From Beginning" and you drag it to the bottom of the order, it will still display from the beginning despite being the last in order. Changing the order in the drag-and-drop will not change the Animation Timing setting. |

To create the animation we want, we simply select the different water elements and have them **Fly in from the right**, set to **From beginning** so all the water comes in at once. We can test this by hitting **Play**:

![firefox_sMTs0nNrIC.gif](https://support.optisigns.com/hc/article_attachments/42305104955283)

### Object Animations

**Object Animations** will animate simultaneously, regardless of the order they are placed in. These can also be set up to animate indefinitely (or as long as the asset is shown on the screen).

For example, let’s say we want our screen to stay up for quite some time (over a minute, say). For that, we’ll want to include some additional animation to make sure it doesn’t get stagnant, and to continue to draw people’s attention.

To do this, we’ll draw attention to the Hydration text element by creating an Object Animation.

![](https://support.optisigns.com/hc/article_attachments/42305104955795)

The Object Animations tab is similar to the Page Animations tab, with a few key differences:

**Animation Timing**

- **Delay** - refers to the delay **between** each animation. This includes at the beginning, and on every subsequent animation
- **End Delay** - Refers to the delay **inside** each animation.

**Loop**

- **Indefinitely** - Continually loop the animation until the asset is changed.
- **One Time** - Play the animation upon load in one time.
- **Iterations** - Allows you to specify how many times you’d like the animation to repeat.

|  |
| --- |
| **NOTE for Legacy Designer 1.0 Users** |
| With the recent Designer 2.0 update, we've depreciated multiple object animations on a single element. If you have 2-3 object animations in a 1.0 design, it can still be edited in 2.0. If deleted, however, it will have to be added back in 1.0. Once Designer 1.0 is depreciated, you will only be able to edit or delete these animations. |

Let’s say we want the Hydration text to bounce from side to side, but not too quickly as to be distracting or annoying.

We’ll set the **Delay** to **3 seconds** and then set the **End Delay** to **3 seconds** as well. This will cause the bounce to hang for that amount of time. Last, we’ll set the Loop to **Indefinitely**:

![firefox_yEpdMaig3q.gif](https://support.optisigns.com/hc/article_attachments/42305100424211)

Now, when we put all our animations together, we get a nice quick set of animations at the beginning thanks to our **Page Animations**, followed by a nice loop after thanks to our **Object Animation**. This can be tested with **Play All** or **Preview**:

![firefox_jSVIvqBZbf.gif](https://support.optisigns.com/hc/article_attachments/42305100425363)

|  |
| --- |
| **NOTE** |
| The formula for each Object Animation iteration is as follows:  Delay + Animation Duration + End Delay = 1 Iteration. |

---

## Common Issues with Animations

Now, let’s go over a few common issues you may run into while trying to display your animations on a screen.

### Preloading Assets in Playlist

This feature allows a more seamless appearance by loading assets prior to showing onscreen. This lessens the likelihood of your signage hanging for a second or two as the assets are loaded.

OptiSigns will preload your assets 6-8 seconds prior to the asset displaying on the screen. This has the unfortunate effect of potentially skipping your animation, which will display immediately upon loading. To fix this, you can either:

- ***(Recommended**)* Add a 1-3 second delay on your animations to ensure they appear onscreen when this preloading is selected:
- Disable Preload Assets in Playlist. However, this will show a blank screen in-between transitions.

### Device Performance

Running too many animations at once will affect your device’s performance and create a less-than-ideal digital signage experience.

In general, the degree to which this is felt will depend on your device’s performance capabilities. A Roku device, typical smart TV, Amazon FireStick, or other device not purpose built for digital signage is likely to suffer from worse issues. If using one of these devices, we recommend no more than **1 or 2 animations per created asset**.

By contrast, Windows and Linux devices or OptiSigns players can handle significantly higher loads. However, if you see stuttering while using one of these devices, we recommend limiting animations to **3-4 animation per created asset**.

### That’s all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).
