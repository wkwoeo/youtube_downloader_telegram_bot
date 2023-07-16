#By @N0040
#Channel @B3kkk

import requests, os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
try:
	import yt_dlp
except:
	os.system("pip install yt_dlp")
	import yt_dlp
api_id = 24061150 # Here Api Id 
api_hash = "bf318d5d543dab16b4a34e37b46db087" # Here Api Hash 
bot_token = "6232454530:AAGwVyhkV1sdBKwmAZWKo82iqMEDOlHfixw" # Here Bot Token 
app = Client("iiu", api_id=api_id,api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start") & filters.private)
def start(client, message):
    message.reply(f"مرحباً يا {message.from_user.mention} !\n› هذا البوت لتحميل مقاطع الفيديو من اليوتيوب\n› فقط قم بارسال الرابط.  مطؤر البوت:@MOH_ALHAMDI", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("قناه المطؤر", url="https://t.me/alhamditecnoo")]]))
@app.on_message(filters.text & filters.private)
async def download(client, message):
     EnyWeb = message.text 
     Me = message.from_user.mention
     x = await message.reply("🔍 بحث....🤔")
     try:
       Media = yt_dlp.YoutubeDL({'format': 'best[ext=mp4]'}).extract_info(EnyWeb, False)["url"]
     except Exception as e:
        await x.delete()
        print(e)
        return await message.reply("› رابط خطأ 🤬")
     try:
        caption = f"**تم صنعه بواسطة {Me}**"
        await message.reply_audio(
             Media,
             caption=caption
        )
        await x.delete()
     except Exception as e:
        print(e)
        await x.delete()
        return await message.reply("هناك خطاء  !")

print("Wait........")
app.run()
print("Bot is run")
    
#By @N0040
#Channel @B3kkk  