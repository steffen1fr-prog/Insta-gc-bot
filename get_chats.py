from instagrapi import Client
import os

USERNAME = os.getenv("INSTA_USER")
PASSWORD = os.getenv("INSTA_PASS")

cl = Client()
cl.login(USERNAME, PASSWORD)

chats = cl.direct_threads(amount=5)
for chat in chats:
    print(chat.id, chat.users)
