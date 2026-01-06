from telegram import Update
from telegram.ext import ContextTypes

from .scrapers.mediamarkt import get_iphone_stock
from .scrapers.sergas import check_cupo_medico_sergas


async def get_medico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cupo = await check_cupo_medico_sergas()
    await update.message.reply_text(cupo)


async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Tu Chat ID es: {update.effective_chat.id}")


async def get_mediamarkt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phones = await get_iphone_stock()
    await update.message.reply_text(phones)
