import telebot
from flask import Flask
import threading
import time

# التوكن الجديد الخاص بك
TOKEN = "8788057411:AAFt0eEO19-QVKSchKaIky9raKY11QnVEyQ"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# حذف أي اتصالات قديمة معلقة (Webhook Delete)
bot.remove_webhook()
time.sleep(1)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ أهلاً يا جنرال يوسف! السيرفر متصل والتحكم جاهز.")

@app.route('/')
def index():
    return "<h1>Server is Running Successfully!</h1>"

def run_bot():
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    # تشغيل البوت في مسار مستقل
    threading.Thread(target=run_bot).start()
    # تشغيل السيرفر
    app.run(host='0.0.0.0', port=10000)
