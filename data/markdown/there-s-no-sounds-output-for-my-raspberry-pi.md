# There's no sounds output for my Raspberry Pi

Article URL: https://support.optisigns.com/hc/en-us/articles/360044614514-There-s-no-sounds-output-for-my-Raspberry-Pi
Article ID: 360044614514
Last Updated: 2025-08-28T20:14:25Z

Make sure you setting audio out to the right output.

**Solution 1:**

To change audio output, right click on the audio icon and select the output.

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/360061945813)

If you are using Raspberry Pi 4, as of 3/12/2020 there's some know issues output audio to both HDMI ports. Use the port next to the power input, it works.

**Solution 2:**

Open the **Terminal,** run command line, use this command to switch the audio output to HDMI:

```
amixer cset numid=3 2
```

If output is set to `2`, which is HDMI.  Output to `1` is analogue (headphone jack). Default setting is `0` is automatic.

**Solution 3:**

Open the **Terminal,** run command line.

```
sudo raspi-config
```

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/8571021810579)

Select **System Options**.

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/8570979748499)

Select **Audio**.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/8570950798611)

Select **0HDMI**

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/8570985894931)

Then select **Finish**

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/8570984227731)

After that, run reboot in the command to reboot your Raspberry Pi

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/8570988279571)

If you have feedback on how to make the how-to guides better, please let us know at: [support@optisigns.com](mailto:support@optisigns.com)
