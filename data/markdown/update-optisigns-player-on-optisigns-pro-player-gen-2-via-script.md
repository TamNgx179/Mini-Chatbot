# Update OptiSigns player on OptiSigns Pro Player (Gen 2) via script

Article URL: https://support.optisigns.com/hc/en-us/articles/21449362442003-Update-OptiSigns-player-on-OptiSigns-Pro-Player-Gen-2-via-script
Article ID: 21449362442003
Last Updated: 2025-09-02T20:33:55Z

If your Pro Player looks like the image below, read on. If it does not, read on [**Remote Commands for the OptiSigns Pro Player (Gen 3)**](https://support.optisigns.com/hc/en-us/articles/4408658251027-How-to-use-Remote-Command-Execution-Windows-Linux).

![Pro Player.png](https://support.optisigns.com/hc/article_attachments/38310905084947)

## OptiSigns Pro Player Gen 2 Commands

You can install/update OptiSigns player on your OptiSigns Pro Player with 1 command line script:

```
 ~/bin/manual_update.sh 
```

This script will download latest version of OptiSigns AppImage and run it.

You can use our Remote Access feature to access the OptiSigns Pro Player, go to this article & copy the command line and run on the Pi to update. It will save time vs. manually clicking & downloading methods.

Other command line scripts:

- If your TV has color saturation issues, run this command to fix it:  

  ```
  wget -O- https://download.optisignsapp.com/pro-player/change-color-profile.sh | bash 
  ```
- Overwrite the automatic security updates timing

  ```
  bash~/bin/override_upgrade_schedule.sh 23:30
  ```
- To lock the USB port, if you want to lock the device to prevent tampering fully.

  ```
  ~/bin/optisigns-lockusb.sh
  ```
- To unlock the USB port.

  ```
  ~/bin/optisigns-unlockusb.sh
  ```

If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
