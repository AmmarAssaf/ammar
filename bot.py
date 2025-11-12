from flask import Flask
import os
import logging
from telegram.ext import Application, CommandHandler
import asyncio
import threading

app = Flask(__name__)

# متغير لتتبع حالة البوت
bot_started = False

def run_bot():
    """تشغيل البوت بشكل منفصل"""
    global bot_started
    
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN غير موجود")
        return
    
    try:
        print("🔄 محاولة تشغيل البوت...")
        
        # إنشاء تطبيق البوت
        application = Application.builder().token(TOKEN).build()
        
        # تعريف الأوامر
        async def start(update, context):
            user = update.effective_user
            await update.message.reply_html(
                f"مرحباً {user.mention_html()}! 🎉\n"
                f"البوت يعمل بنجاح على Render!"
            )
        
        async def help_command(update, context):
            await update.message.reply_text(
                "🔍 الأوامر المتاحة:\n"
                "/start - بدء التشغيل\n"
                "/help - المساعدة\n"
                "/test - اختبار البوت"
            )
        
        async def test(update, context):
            await update.message.reply_text("✅ الاختبار ناجح! البوت يعمل!")
        
        # إضافة handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("test", test))
        
        print("✅ البوت مهيئ، بدء الاستماع للرسائل...")
        
        # تشغيل البوت
        application.run_polling(drop_pending_updates=True)
        
        bot_started = True
        print("🎉 البوت يعمل ويستمع للرسائل!")
        
    except Exception as e:
        print(f"❌ خطأ في تشغيل البوت: {e}")
        import traceback
        traceback.print_exc()

# بدء البوت عند تشغيل التطبيق
print("🚀 بدء تشغيل التطبيق...")
bot_thread = threading.Thread(target=run_bot, daemon=True)
bot_thread.start()

@app.route('/')
def home():
    global bot_started
    status = "✅ يعمل" if bot_started else "❌ متوقف"
    return f"""
    <h1>🤖 بوت تيليجرام</h1>
    <p>حالة البوت: <strong>{status}</strong></p>
    <p>اذهب إلى تيليجرام وجرب:</p>
    <ul>
        <li><code>/start</code></li>
        <li><code>/help</code></li>
        <li><code>/test</code></li>
    </ul>
    <p><a href="/status">تفاصيل الحالة</a></p>
    """

@app.route('/ping')
def ping():
    return "pong"

@app.route('/status')
def status():
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    token_status = "✅ مضبوط" if TOKEN else "❌ غير موجود"
    return f"""
    <h2>📊 حالة النظام</h2>
    <p>التوكن: {token_status}</p>
    <p>البوت: {'✅ يعمل' if bot_started else '❌ متوقف'}</p>
    <p><a href="/">العودة للرئيسية</a></p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
