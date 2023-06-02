from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/71ba33c1ebbfcb15d90ab.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/5cec76ca0466630e0b4db.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Gruop_Shetakan")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ChanallBots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5739996356").split()))


FAILED = "https://telegra.ph/file/53a98c2a8e16390e35843.jpg"
