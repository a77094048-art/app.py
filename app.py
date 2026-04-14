import telebot
from flask import Flask
import threading

TOKEN = "8788057411:AAFt0eEO19-QVKSchKaIky9raKY11QnVEyQ"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "تم تفعيل لوحة تحكم الجنرال يوسف بنجاح! جاري تجهيز الأزرار...")

@app.route('/')
def hello():
    return "Server is Live!"

def run_bot():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=10000)
