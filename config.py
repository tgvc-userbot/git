import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = int(os.getenv("API_ID", "7475191"))
API_HASH = os.getenv("API_HASH", "32dbc9e8368cca754844f77399f6db81")
OWNER_ID = int(os.getenv("OWNER_ID", "1926090919"))
DOWN_PATH = os.getenv("./downloads")
SESSION = os.getenv("SESSION", "AQA81iRNYKnCLPrLBd4THySXcx5Hc-wz8SkauDJVxaGfgxA4Xx2da5SOmdf_9-F7Iyn9RtvlNpTry0RwL8I34mfmrjvKMwEpeBn6yZyEoM7m29Z6l3WDKyrQW3Rdwzvll98drSzFKQyMA-8T42a03wyUOwsFo9kSPi12O_6wiiB0syQFRkF1QbuRuVjstAv9Gpglj1X0Au2-uYdq22z_hDIAOKokj4QAc6PBASYIZRCEylNUAagyhc6usi-tl1WkADcwofJI0HuCOF145SE481RpgIPYLBUp6LZ4F_Yy3KdqxfcwvJipqwHWpxlja4mBEAatHLW6rSr0fXp6THHvjEG1cu_qiwA")
HNDLR = os.getenv("HNDLR", "*")


contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="vcmusic"))
call_py = PyTgCalls(bot)
