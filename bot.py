import os
import logging
from telegram.ext import Application, CommandHandler

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        f"مرحباً {user.mention_html()}! 🎉\n"
        f"البوت يعمل بنجاح على Render!"
    )

async def help_command(update, context):
    await update.message.reply_text("🔍 استخدم /start لبدء المحادثة")

async def test(update, context):
    await update.message.reply_text("✅ الاختبار ناجح! البوت يعمل!")

def main():
    if not TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN غير موجود")
        return
    
    try:
        application = Application.builder().token(TOKEN).build()
        
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("test", test))
        
        print("🚀 بدء تشغيل البوت...")
        print("✅ البوت يعمل ويستمع للرسائل!")
        
        application.run_polling()
        
    except Exception as e:
        print(f"❌ خطأ: {e}")

if __name__ == '__main__':
    main()
