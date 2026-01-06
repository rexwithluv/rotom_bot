from telegram.ext import ContextTypes

from .scrapers.mediamarkt import get_iphone_stock
from .scrapers.sergas import check_cupo_medico_sergas


async def medico_job(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    resultado = await check_cupo_medico_sergas()
    await context.bot.send_message(chat_id=chat_id, text=resultado)


async def iphone_job(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    resultado = await get_iphone_stock()
    await context.bot.send_message(chat_id=chat_id, text=resultado)
