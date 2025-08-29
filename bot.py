from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo Dyera! Bot ini akan bantu kamu terhubung ke Strava. Ketik /connect untuk mulai.")

async def connect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    # Ganti dengan URL login Strava milikmu
    auth_url = f"https://www.strava.com/oauth/authorize?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=https://yourdomain.com/callback&scope=activity:read_all"
    await update.message.reply_text(f"Klik untuk login ke Strava: {auth_url}")

app = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("connect", connect))

app.run_polling()
