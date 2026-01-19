import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token bilgisini buraya işledim
TOKEN = "8598557830:AAGW9bE-cBvFfIBQhQ8MKTW483eknYeDRmY"
# Buraya GitHub'da yayınladığın oyunun linkini yazacaksın
WEB_APP_URL = "https://KULLANICI_ADIN.github.io/m-coin-city/" 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    
    # Giriş Mesajı ve Buton
    keyboard = [
        [InlineKeyboardButton("Şehri Yönet 🏗️ (M-City)", web_app_info=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        f"Hoş Geldiniz Sayın Başkan {user_name}! 🏛️\n\n"
        "M-Coin City'nin geleceği sizin ellerinizde.\n"
        "Tıklayın, inşa edin ve en zengin başkan olun!"
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    print("M-Coin City Botu Aktif! Telegram'dan /start yazarak test edebilirsiniz.")
    application.run_polling()