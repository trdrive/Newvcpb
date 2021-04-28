from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

bot = Client(
    "my_account",
    api_id=4810065,
    api_hash=01d3d24dcbbfba7189ee7c506f1a0fdb 
    bot_token=1790128013:AAESIats1yXV3fSb9XPcnjIPfSKCc466JdA
    plugins={"root": "handlers"}
)

if __name__ == "__main__":
    bot.run()
