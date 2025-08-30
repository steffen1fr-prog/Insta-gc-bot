import instagrapi
from instagrapi import Client

import os

USERNAME = os.getenv("INSTA_USER")
PASSWORD = os.getenv("INSTA_PASS")
GC_THREAD_ID = os.getenv("GC_THREAD_ID")

cl = Client()
cl.login(USERNAME, PASSWORD)

def send_welcome_message(username):
    message = f"Welcome to the group, {username}! 🎉"
    cl.direct_send(message, [GC_THREAD_ID])

# Example use
# send_welcome_message("new_member_username")
