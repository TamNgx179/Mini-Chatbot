# Silent Installation process for OptiSigns Player on Windows

Article URL: https://support.optisigns.com/hc/en-us/articles/15861880059283-Silent-Installation-process-for-OptiSigns-Player-on-Windows
Article ID: 15861880059283
Last Updated: 2025-08-29T18:51:22Z

By default, when you install the OptiSigns Windows player on your Windows device, it will be installed on your default user profile.   
  
If you want to do the silent install in another folder instead of the default user profile. This will be helpful for looking for mass provisioning on Windows and deploying with a prebuilt Windows image.

You can follow this article.

1. Search the **Command Prompt** and **Run as administrator**

![](https://support.optisigns.com/hc/article_attachments/15861776979603)

2. Move the OptiSigns exe file to the folder.

3. Run or go to your folder

```
cd c:\temp
```

or

```
cd c:\[Your Folder Name]
```

4. Run or install the OptiSigns in your folder

```
"OptiSigns Digital Signage Setup 5.6.4" /S /D="c:\temp\optisigns"
```

or

```
"OptiSigns Digital Signage Setup 5.6.4" /S /D="c:\[Your Folder Name]\optisigns"
```

![](https://support.optisigns.com/hc/article_attachments/15912711216275)

Then it will install in that folder.

If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)
