from pyrogram import Client, filters

API_ID = 123456
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

app = Client(
    "music-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🎵 Radhe Music Bot चालू है!\n\nगीत चलाने के लिए /play भेजें ❤️")

@app.on_message(filters.command("play"))
async def play(client, message):
    await message.reply("🔍 कृपया वह गाना भेजें, जिसका नाम आप प्ले करना चाहते हैं!")

app.run()
