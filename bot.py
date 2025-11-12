from flask import Flask
import os
import logging
from telegram.ext import Application, CommandHandler
import threading

app = Flask(__name__)

# المتغيرات العالمية
bot_application = None

def init_bot():
    """تهيئة البوت في خيط منفصل"""
    global bot_application
    
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    if not TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN غير موجود")
        return
    
    try:
        bot_application = Application.builder().token(TOKEN).build()
        
        async def start(update, context):
            await update.message.reply_text("✅ البوت يعمل بنجاح!")
        
        async def help_cmd(update, context):
            await update.message.reply_text("الأوامر: /start, /help")
        
        bot_application.add_handler(CommandHandler("start", start))
        bot_application.add_handler(CommandHandler("help", help_cmd))
        
        print("🚀 بدء تشغيل البوت...")
        bot_application.run_polling()
        
    except Exception as e:
        print(f"❌ خطأ: {e}")

# بدء البوت عند التحميل
if os.getenv('TELEGRAM_BOT_TOKEN'):
    bot_thread = threading.Thread(target=init_bot, daemon=True)
    bot_thread.start()
else:
    print("⚠️  TELEGRAM_BOT_TOKEN غير معين - البوت لن يعمل")

@app.route('/')
def home():
    return "🤖 خادم البوت يعمل"

@app.route('/ping')
def ping():
    return "pong"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
