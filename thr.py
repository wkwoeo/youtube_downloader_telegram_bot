import telebot
import requests
token = "6006226341:AAHDUb9LMuCTfAA7mryRm9ikXWYj2eZB_kY"#token
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    
            if message.chat.type == "private":
                ch = "alhamditecnoo"
                idu = message.chat.id
                join = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{ch}&user_id={idu}").text
                if '"status":"left"' in join:
                    bot.send_message(message.chat.id,f"🚸| عذرا عزيزي\n🔰| عليك الاشتراك بقناة البوت\nلتتمكن من استخدامه\n- https://t.me/{ch}\n‼️| اشترك ثم ارسل /start",disable_web_page_preview="true")
                else:
                	
                	bot.reply_to(message,"🥳مرحبا بك في بوت ألحمدي لتنزيل مقاطع الفيديو من تطبيق ثريدز&Threadsارسل رابط الفيديو. المطؤر:@MOH_ALHAMDI")

headers = {
    'authority': 'savevideofrom.me',
    'content-type': 'application/x-www-form-urlencoded',
}

@bot.message_handler(regexp='.threads.net/')
def tre(message):
    try:
    	bot.send_chat_action(message.chat.id,action='upload_video')
    	data = {
    	'url': message.text,
    	}
    	response = requests.post('https://savevideofrom.me/wp-json/aio-dl/video-data/',headers=headers, data=data).json()
    	ti = response['title']
    	aa = response['medias'][1]['url']
    	bot.send_video(message.chat.id,aa,caption=f'{ti}')
    	
    except:
    	bot.reply_to(message,'خطاء...ارسل رابط فيديو ')

# تذكرو مصدري 
'''
مبرمج الملف - @BRoK8
قناتي - @Crrazy_8
''' 
     
print('run')
bot.infinity_polling()
