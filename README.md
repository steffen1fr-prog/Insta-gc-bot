# Instagram GC Welcome Bot

This bot automatically sends a welcome message to new members in your Instagram group chat.

## Files
- `bot.py` : Main bot code
- `requirements.txt` : Dependencies
- `Procfile` : For deployment on Heroku/Railway
- `get_chats.py` : To fetch your group chat IDs

## Setup
1. Upload these files to your GitHub repo.
2. Connect repo to Railway/Heroku.
3. Set environment variables:
   - `INSTA_USER` : Your Instagram username
   - `INSTA_PASS` : Your Instagram password
   - `GC_THREAD_ID` : The group chat thread ID

4. Deploy 🚀
