from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread
import os

TOKEN = os.getenv("TOKEN")  # security better

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is live 24/7 🚀")

bot = ApplicationBuilder().token(TOKEN).build()
bot.add_handler(CommandHandler("start", start))

keep_alive()
bot.run_polling()
