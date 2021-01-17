import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")


chanels = [-1001244090631]

admins = [
    os.getenv("ADMIN_ID"),
]

allowed_users = [
]

ip = os.getenv("ip")


PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN")
