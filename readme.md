# Bot for tracking exam

When preparing for the exam (especially self-study), it is important to monitor the process. The Telegram bot was created for this very purpose. With the help of the bot, you can monitor the process. You can analyze the results. You enter daily logs into the bot (via the /log command). The bot saves them. You can get a weekly report (maybe in a diagram) and analyze them. In addition, the bot can send daily reports to a specific channel. For many, tracking them while studying (for example, for me) gives a better result, you need to add your friends to a specific channel, make the bot an admin to the channel. The bot will send daily logs to your friends via the channel.

In the future, I plan to add a few more features. But of course, this is not a promise, I may not do anything. But you can make it yourself, download and use it

### install and run

```
git clone https://github.com/mehmonov/examlog.git
cd examlog

python3 -m venv env
pip install -r req.txt
```
and .env.example rename ->  .env(write variables)

maybe running with server read - > _deploy/read.md
