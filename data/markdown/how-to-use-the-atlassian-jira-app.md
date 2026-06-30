# How to use the Atlassian JIRA app

Article URL: https://support.optisigns.com/hc/en-us/articles/360037416494-How-to-use-the-Atlassian-JIRA-app
Article ID: 360037416494
Last Updated: 2025-08-28T20:12:13Z

### Jira is a popular project management tool that helps teams plan, track, release, and support work. Let's go through how to set this app integration up!

**What you'll need:**

- Jira project or dashboard
- Keyboard and mouse

---

In your Jira account, navigate to the page of the project or private dashboard that you'd like to display. Copy the direct URL.

![Jira dashboard with the URL pointed at](https://support.optisigns.com/hc/article_attachments/35838410787219)

Next, log in to [OptiSigns portal](https://app.optisigns.com/app/screenManagement) and navigate to the files/assets page. Click Apps and search for Jira.

![Jira app within OptiSigns](https://support.optisigns.com/hc/article_attachments/35838410792595)

Here, you'll input certain information to create the asset:

![Jira app settings when setting it up in OptiSigns](https://support.optisigns.com/hc/article_attachments/35838425274899)

- **Name:** Any name you'd like to give the asset for internal organizational purposes only.
- **Type:** Either URL or Embed code.
- **URL/Embed Code:** The direct link or code of the project or dashboard that you'd like to display.
- **Update Interval:** The duration of time between updates. (Default: 600 seconds).

For "Sign In" settings, you will have to provide you log in so OptiSigns can easily log in for you. When your app is pushed to the screen, OptiSigns will use this information to automatically login to your account to display the URL/Embed code given:

- **Master Password:** By default, OptiSigns will encrypt the whole script with OptiSigns private key to protect your script, especially username, password in the script. You can add another protection layer by entering a Master Password. If you enter Master Password here, at each device, you will need to enter that Master Password one time in OptiSigns app so it can decrypt the content.
- **Username/Email:** The email or username for the account you're using.
- **Password:** The password for the account you're using.

Finally, click "**Save**".

### Verification Code

When you push your Jira asset to your screen for the first time, Jira will send a verification code to your email. You will need to input this code into the asset pushed to your screen.

For this, you will need a **keyboard and mouse**connected to your device to input this. Afterward, Jira will recognize your device and not ask you to do this again.

[According to Jira](https://community.atlassian.com/t5/Jira-questions/Stop-asking-me-for-email-verification/qaq-p/1646087), this is for security purposes so Jira can register the device to your account.

---

## Troubleshooting

- If your dashboard is public, it may display as empty. Making your dashboard private will allow OptiSigns to properly run the login script.
