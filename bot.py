# bot.py
import logging
from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN, WEB_APP_URL

# Включаем логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_id = update.effective_chat.id

    # Опционально: можно передать параметры в Mini App через start_param
    # Например, user ID или другие данные (в кодировке base64 или простой строкой)
    start_param = f"user_id={user.id}"

    # Формируем URL Mini App с параметром
    web_app_url = f"{WEB_APP_URL}?start_param={start_param}"

    # Создаем кнопку с Web App
    from telegram import InlineKeyboardMarkup, InlineKeyboardButton
    keyboard = [
        [
            InlineKeyboardButton(
                text="Открыть Mini App 🚀",
                web_app=WebAppInfo(url=web_app_url)
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Привет, {user.first_name}! Нажми кнопку ниже, чтобы открыть Mini App:",
        reply_markup=reply_markup
    )

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    logger.info("Бот запущен и готов к работе с Mini Apps!")
    application.run_polling()

if __name__ == "__main__":
    main()