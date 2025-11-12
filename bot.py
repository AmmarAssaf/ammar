from flask import Flask
from threading import Thread
import os
import logging
from telegram.ext import Application, CommandHandler
import asyncio

app = Flask(__name__)

# إعداد البوت
def run_bot():
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not TOKEN:
        logging.error("❌ TELEGRAM_BOT_TOKEN غير موجود")
        return
    
    try:
        # النمط الحديث مع python-telegram-bot 21.0
        application = Application.builder().token(TOKEN).build()
        
        async def start(update, context):
            user = update.effective_user
            await update.message.reply_html(f"مرحباً {user.mention_html()}! ✅ البوت يعمل!")
        
        async def help_command(update, context):
            await update.message.reply_text("🔍 الأوامر: /start, /help")
        
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        
        print("🤖 بدء تشغيل البوت...")
        
        # تشغيل البوت
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        application.run_polling()
        
    except Exception as e:
        print(f"❌ خطأ في البوت: {e}")

# تشغيل البوت في thread منفصل
@app.before_first_request
def start_bot():
    bot_thread = Thread(target=run_bot, daemon=True)
    bot_thread.start()

@app.route('/')
def home():
    return "🤖 البوت يعمل بنجاح!"

@app.route('/ping')
def ping():
    return "pong"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
