from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import os, sys


api_id = 16746278
api_hash = "ca3a465d4b961e137addeb2e4f9b6581" 
acaunt = input("    Telefon:    ")
client = TelegramClient(acaunt, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(acaunt)
    client.sign_in(acaunt, input('[+] введите код из смс: '))
    client.disconnect()
client = TelegramClient(acaunt, api_id, api_hash)
print("ok")
client.connect()