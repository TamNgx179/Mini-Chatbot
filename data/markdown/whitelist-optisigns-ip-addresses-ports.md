# Whitelist OptiSigns IP addresses & ports

Article URL: https://support.optisigns.com/hc/en-us/articles/360047275934-Whitelist-OptiSigns-IP-addresses-ports
Article ID: 360047275934
Last Updated: 2026-06-18T00:48:15Z

If you need to configure the firewall, here is the list of OptiSigns IP addresses and Port to whitelist:

Port: please whitelist HTTPS port 443

IP Address for **OptiSigns**:

- \*.optisigns.com
- api.optisignsapp.com
- api.optisigns.com
- api-prod-2.optisigns.com
- api-prod-3.optisigns.com
- api-prod-4.optisigns.com
- ws-prod-1.optisigns.com
- ws-prod-2.optisigns.com
- ws-prod-3.optisigns.com
- mdm-ws-prod-1.optisigns.com
- mdm-ws-prod-2.optisigns.com
- signagecloud-prd.nyc3.cdn.digitaloceanspaces.com
- smallapp-api.prod.optisignsapp.com
- smallapp.optisigns.com
- download.optisigns-cdn.com
- 52.217.39.148 (File)
- 162.243.189.2 (Files)
- 157.230.201.46 (API)
- 206.189.255.219 (API)
- software-update.optisigns.com (Pro Player OTA update)
- software-download.optisigns.com (Pro Player OTA update)

OptiSigns utilizes Transloadit for **uploading files via the OptiSigns portal**. If you encounter any issues with uploading files, you can resolve this by whitelisting Transloadit's IP address.

- \*.transloadit.com
- \*.\*.transloadit.com
- s3.amazonaws.com
- s3-eu-west-1.amazonaws.com

OptiSigns utilizes Unsplash images in the **Designer app**. If you encounter any issues with using free Unsplash images, you can resolve this by whitelisting Unsplash's IP address.

- plus.unsplash.com
- images.unsplash.com

OptiSigns utilizes RealVNC for **Remote Device Control**. If you use remote control and experience any connection issues with remote control, you can resolve this by whitelisting RealVNC's domain and IP address.

- \*.services.vnc.com

OptiSigns utilizes Sport Pulse for **Sports Feeds**. If you have an issue displaying the sports feed, you can resolve this by whitelisting Sport Pulse's domain.

- sportpulse.app

OptiSigns utilizes Bit.ly for Shortened Links. If you're having trouble accessing links like links.optisigns.com, please whitelist Bit.ly’s IP addresses.

- 67.199.248.13
- 67.199.248.12

Some OptiSigns Apps can fetch your content from a fixed OptiSigns IP address. This helps when your content is behind a firewall or IP allow-list. When you turn on the Static IP option for that content in OptiSigns, we fetch it from the IP below:

- 178.128.134.248

IP Address for **AeriCast**:

- screenshare.aericast.com
- present.aericast.com
- apps-api-prd.aericast.com

**IMPORTANT NOTE:** we use CDN to optimize file distribution to your devices. Some firewalls may block CDNs. If you experiencing issues where your device is online, but when you assign files, it's just a black screen because the device cannot download files. You can contact us at [support@optisigns.com](mailto:support@optisigns.com) to disable the CDN feature for your account. (Note: It requires the Engage or Enterprise Plan)

There's no set of IP addresses for Social Media and some other apps like Facebook, Instagram, YouTube, and Google Calendar, so if you restrict HTTPS access by IP, you may not be able to use those apps.
