from telegram.ext import Application, CommandHandler
import os
import logging

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
    await update.message.reply_text('🎉 البوت يعمل بنجاح! أخيراً!')

async def help(update, context):
    await update.message.reply_text('❓ الأوامر: /start, /help')

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    
    logger.info("🚀 Starting bot...")
    print("✅ البوت شغال!")
    application.run_polling()

if __name__ == '__main__':
    main()
