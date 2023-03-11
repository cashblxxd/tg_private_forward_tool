from telethon.sync import TelegramClient, events
from config import settings


with TelegramClient('MyApp', settings.API_ID, settings.API_HASH) as client:
    for dialog in client.iter_dialogs():
        print('{:>14}: {}'.format(dialog.id, dialog.title))

    client.run_until_disconnected()
