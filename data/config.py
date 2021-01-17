import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

ip = os.getenv("ip")

# PGUSER = os.getenv("PGUSER")
# PGPASSWORD = os.getenv("PGPASSWORD")


# chanels = [-1001244090631]

admins = [
    os.getenv("ADMIN_ID"),
]

# allowed_users = [
# ]


# PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN")
