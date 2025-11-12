from flask import Flask
from threading import Thread
import os
import logging
from telegram.ext import Application, CommandHandler

# إعداد Flask مع البوت
app = Flask(__name__)
bot_application = None

# إعداد البوت
def setup_bot():
    global bot_application
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not TOKEN:
        logging.error("❌ لم يتم تعيين TELEGRAM_BOT_TOKEN")
        return
    
    bot_application = Application.builder().token(TOKEN).build()
    
    async def start(update, context):
        user = update.effective_user
        await update.message.reply_html(f"مرحباً {user.mention_html()}! 👋")
    
    async def help_command(update, context):
        await update.message.reply_text("🔍 الأوامر: /start, /help")
    
    bot_application.add_handler(CommandHandler("start", start))
    bot_application.add_handler(CommandHandler("help", help_command))
    
    # تشغيل البوت في thread منفصل
    def run_bot():
        bot_application.run_polling()
    
    bot_thread = Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()

@app.route('/')
def home():
    return "🤖 البوت يعمل بنجاح!"

@app.route('/health')
def health():
    return "✅ OK"

if __name__ == '__main__':
    setup_bot()
    app.run(host='0.0.0.0', port=5000)
