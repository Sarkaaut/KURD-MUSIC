from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "400"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/b18fe3e598295972a774f.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/1227e31aec0891e810516.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/grup_g4njan")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ChanallBots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5789819429").split()))


FAILED = "https://telegra.ph/file/df75144e63c1a1d04da98.jpg"
