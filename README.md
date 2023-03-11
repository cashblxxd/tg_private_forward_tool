# Telegram Private Channels Forwarding Workaround

1. Create an app at [my.telegram.org](my.telegram.org) and insert its `API_ID` and `API_HASH` into `.env`
2. Run `python3 get_chats.py` to look up desired `PRIVATE_CHAT_ID` and `REDIRECT_CHAT_ID` to add them into `.env`
3. `sudo su`
4. `crontab -e`
5. Create a Cron job based on `crontab-e.example`
6. Note that running with `{"id": 0}` will redirect all available messages from private chat. To avoid this, figure out last channel message id and paste it there
7. Done
