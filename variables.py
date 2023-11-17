import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6887245348:AAG-WoxzXXXRgEuOpASVfd7Zzu2SLRHBrvo")

API_ID = int(os.environ.get("API_ID", "28625475"))

API_HASH = os.environ.get("API_HASH", "da4894b36ca60168ba283519ed551606")

PICS = os.environ.get("PICS", "https://telegra.ph/file/916286a7d8652606ce806.jpg").split()

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1720819569').split()]

DB_URL = os.environ.get("DB_URL", "mongodb+srv://dohoj11515:f5VibAbQ4LVHpQ5n@cluster0.h3s7s7p.mongodb.net/?retryWrites=true&w=majority")

DB_NAME = os.environ.get("DB_NAME", "tg-multi-bot")

RemoveBG_API = os.environ.get("RemoveBG_API", "")

FORCE_SUB = os.environ.get("FORCE_SUB", None)           

HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")
 
log_channel = environ.get("LOG_CHANNEL")

LOG_CHANNEL = int(log_channel) if log_channel and id_pattern.search(log_channel) else None

LOG_TEXT = """<i><u>👁️‍🗨️USER DETAILS</u>

○ ID : <code>{id}</code>
○ DC : <code>{dc_id}</code>
○ First Name : <code>{first_name}<code>
○ UserName : @{username}

By = {bot}</i>"""












