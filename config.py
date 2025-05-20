import os

API_ID = 25318125

API_HASH = os.environ.get("API_HASH", "b29fb6a928e8b8a3308f8c2d3ba9cfb0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7959445535:AAH6cQtHpNBDfx8b8MGkdrxeM3imLZ1LFHg")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "7376514183"))

LOG = int(os.environ.get("LOG", "1"))

PORT = os.environ.get("PORT", "8080")

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7376514183").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
