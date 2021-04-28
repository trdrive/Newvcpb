from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

bot = Client(
    "my_account",
    api_id=4810065,
    api_hash="01d3d24dcbbfba7189ee7c506f1a0fdb"
    bot_token="1790128013:AAHhLr4RmrXHbBqUf7pMd3vG3C-bd3PYdYQ"
    plugins={"root": "handlers"}
)

if __name__ == "__main__":
    bot.run()
