from telegram.ext import Application, CommandHandler
import os
import logging
import asyncio

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not TOKEN:
    logger.error("❌ لم يتم تعيين TELEGRAM_BOT_TOKEN")
    logger.error("⏳ تأكد من تعيين المتغير في إعدادات Render")
    exit(1)

async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        f"مرحباً {user.mention_html()}! 👋\n"
        f"البوت يعمل بنجاح على Render! 🎉"
    )

async def help_command(update, context):
    await update.message.reply_text(
        "🔍 الأوامر المتاحة:\n"
        "/start - بدء التشغيل\n"
        "/help - المساعدة"
    )

def main():
    try:
        application = Application.builder().token(TOKEN).build()
        
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        
        logger.info("🚀 بدء تشغيل البوت على Render...")
        print("✅ البوت يبدأ التشغيل!")
        
        # تشغيل البوت
        application.run_polling()
        
    except Exception as e:
        logger.error(f"❌ خطأ: {e}")
        exit(1)

if __name__ == '__main__':
    main()
