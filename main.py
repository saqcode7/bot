from telegram.ext import Updater, CommandHandler
from flask import Flask
import os
import threading

TOKEN = os.environ.get('TELEGRAM_TOKEN')  # سيتم أخذ التوكن من متغيرات البيئة

# جزء Flask لإنشاء خادم ويب
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=3000)

# جزء بوت تليجرام
def start(update, context):
    update.message.reply_text('مرحباً! البوت يعمل على Glitch 🚀')

def main():
    # تشغيل Flask في thread منفصل
    threading.Thread(target=run_flask).start()
    
    # تشغيل بوت تليجرام
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
