from telegram.ext import Application, CommandHandler
import os
import logging

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not TOKEN:
    logger.error("❌ TOKEN not found")
    raise ValueError("No token provided")

async def start(update, context):
    await update.message.reply_text('✅ البوت يعمل بنجاح!')

async def help(update, context):
    await update.message.reply_text('❓ المساعدة: /start, /help')

def main():
    # النمط الحديث - لا يوجد أي Updater هنا
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    
    logger.info("🚀 Starting bot...")
    application.run_polling()

if __name__ == '__main__':
    main()
