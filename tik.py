import telebot
import requests

token = "6274564703:AAH6kuzF0bCucpE2ZQ78hLYffdguYbPX2Mc" # توكن البوت الخاص بك

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
            bot.reply_to(message,"مرحبا بك في بوت ألحمدي لتنزيل مقاطع التيك تؤك ارسل رابط الفيديو الان🥳. مطؤر البوت:@MOH_ALHAMDI")

@bot.message_handler(func=lambda brok:True)
def Url(message):
    try:
        msgg = bot.send_message(message.chat.id, "*جاري التحميل ...🤔*",parse_mode="markdown")
        msg = message.text
        url = requests.get(f'https://tikwm.com/api/?url={msg}').json()
        music = url['data']['music']
        region = url['data']['region']
        tit = url['data']['title']
        vid = url['data']['play']
        ava = url['data']['author']['avatar']
        name = url['data']['music_info']['author']
        time = url['data']['duration']
        sh = url['data']['share_count']
        com = url['data']['comment_count']
        wat = url['data']['play_count']
        bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
        bot.send_photo(message.chat.id, ava, caption=f'- اسم الحساب : *{name}*\n - دوله الحساب : *{region}*\n\n- عدد مرات المشاهدة : *{wat}*\n- عدد التعليقات : *{com}*\n- عدد مرات المشاركة : *{sh}*\n- طول الفيديو : *{time}*', parse_mode="markdown")
        btn = telebot.types.InlineKeyboardMarkup().add(telebot.types.InlineKeyboardButton('تحميل الصوت', url=music))
        bot.send_video(message.chat.id, vid, caption=f"{tit}", reply_markup=btn)
    except:
        bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
        bot.reply_to(message, 'حدث خطأ أثناء تحميل الفيديو :(')

print('run')
bot.infinity_polling()