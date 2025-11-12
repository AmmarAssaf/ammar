from flask import Flask
import os
import logging
from telegram.ext import Application, CommandHandler
import asyncio
import threading

app = Flask(__name__)

def run_bot():
    """تشغيل البوت في thread منفصل"""
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN غير موجود")
        return
    
    try:
        # إنشاء تطبيق البوت
        application = Application.builder().token(TOKEN).build()
        
        async def start(update, context):
            user = update.effective_user
            await update.message.reply_html(f"مرحباً {user.mention_html()}! ✅ البوت يعمل على Render!")
        
        async def help_command(update, context):
            await update.message.reply_text("🔍 الأوامر المتاحة:\n/start - بدء التشغيل\n/help - المساعدة")
        
        async def test(update, context):
            await update.message.reply_text("🎉 الاختبار ناجح! البوت يعمل بشكل صحيح")
        
        # إضافة handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("test", test))
        
        print("🤖 بدء تشغيل البوت...")
        
        # تشغيل البوت
        application.run_polling()
        
    except Exception as e:
        print(f"❌ خطأ في البوت: {e}")

# بدء البوت عند تشغيل السكريبت
bot_thread = threading.Thread(target=run_bot)
bot_thread.daemon = True
bot_thread.start()

@app.route('/')
def home():
    return """
    <h1>🤖 بوت تيليجرام يعمل بنجاح!</h1>
    <p>البوت يعمل على Render. اذهب إلى تيليجرام وجرب الأوامر:</p>
    <ul>
        <li><code>/start</code></li>
        <li><code>/help</code></li>
        <li><code>/test</code></li>
    </ul>
    """

@app.route('/ping')
def ping():
    return "✅ البوت نشط"

@app.route('/health')
def health():
    token_exists = os.getenv('TELEGRAM_BOT_TOKEN') is not None
    return f"الحالة: {'✅ جاهز' if token_exists else '❌ يحتاج توكن'}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
