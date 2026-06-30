# Samsung Tizen TVs Troubleshooting Guide

Article URL: https://support.optisigns.com/hc/en-us/articles/28424138317971-Samsung-Tizen-TVs-Troubleshooting-Guide
Article ID: 28424138317971
Last Updated: 2026-01-12T16:10:54Z

### **IMPORTANT NOTE:**

While OptiSigns app is available on Samsung Tizen app store, we still recommend using a dedicated player like our [OptiStick Player](https://links.optisigns.com/szzk) for these reasons:

- Samsung Tizen does not allow apps to autostart, include Digital Signage app like OptiSigns, so not really suitable for digital signage unless your team can turn on/off TV every day as part of their schedule
- Low local storage, usually only a few hundreds MBs available. It's good for streaming Youtube, Netflix, but for Digital Signage you want your content to be downloaded and cached locally to ensure playback even when there’s network interruption and save bandwidths.
- OptiSigns app are not available on some Samsung TV models and regions

In short, if you want to play small simple playlist with couple of images, videos, weather apps, and don't mind manually launching the app when Samsung TV powered on. You can continue to install OptiSigns app on Samsung TV.

## **Troubleshooting guide:**

#### **Content not playing:**

- Samsung TVs have very limited local storage, make sure your playlist is less than 15 items, or less than 150MB total.
- Video not playing: OptiSigns app download video to play locally (to ensure offline playback and save bandwidths), large video files may not play well on your Samsung TV, due to limited local storage above. If you playing a lot of video, please consider [OptiSigns Android Player](https://links.optisigns.com/szzk) it comes with 16GB storage.

#### **Cannot find OptiSigns on Samsung app store:**

- If you are in the US and cannot find OptiSigns on the app store, your model is very likely not supported, please consider a dedicated player like [OptiSigns Android Player.](https://links.optisigns.com/szzk)

#### **Networking:**

- This test will resolve most of the networking issues:
  - Try mobile hotspot
  - Try different network (bring the device home or to another location with better WiFi)
- Check other app like Youtube make sure it can connect to internet
- If Youtube is playing and OptiSigns app has issue, you could be behind a fire wall.
  - If you have firewalls, make sure our [servers are whitelisted](https://support.optisigns.com/hc/en-us/articles/360047275934-Whitelist-OptiSigns-IP-addresses-ports)

**Factory Reset:**

Lastly, you can try [Factory Reset & Diagnostic guide form Samsung](https://www.samsung.com/us/support/answer/ANS00077524/).

## Specific Model Limitations:

#### SSSP 10 (Tizen 6.5)

The "Seamless Video Playback" feature released for these models can cause screen glitches. Seamless playback is meant to play videos back-to-back without the screen ever going black in between.

Here are a few known workarounds:

- Keep all videos encoded in h264, but ensure the resolution for all videos are the same.
  - In other words, don't switch between HD (1980x1080) and 4K (3840x2160) videos.
- Re-encode all videos to h265 (we recommend [**Handbrake**](https://handbrake.fr/)for this). This way, all the videos can keep their resolution.
