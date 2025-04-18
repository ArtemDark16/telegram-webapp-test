from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# 🔑 Встав свій токен від @BotFather
TOKEN = "1878416749:AAEvBR4RPIHFUDL-8QMAADi6QnbO8vgeEG8"

# 🌐 URL твого WebApp (Render-сервіс)
WEBAPP_URL = "https://telegram-webapp-test.onrender.com"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Відкрити WebApp", web_app=WebAppInfo(url=WEBAPP_URL))]
    ])
    await update.message.reply_text("Привіт! Натисни кнопку нижче:", reply_markup=keyboard)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
