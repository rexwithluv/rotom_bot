from telegram.ext import ContextTypes

from .scrapers.mediamarkt import get_iphone_stock
from .scrapers.sergas import check_cupo_medico_sergas


async def medico_job(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.bot_data.get("config").chat_id
    resultado = await check_cupo_medico_sergas()

    if resultado != context.bot_data.get("cupo_medico"):
        await context.bot.send_message(chat_id=chat_id, text=resultado)
        context.bot_data["cupo_medico"] = resultado


async def iphone_job(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.bot_data.get("config").chat_id
    resultado = await get_iphone_stock()

    if resultado != context.bot_data.get("iphone_stock"):
        await context.bot.send_message(chat_id=chat_id, text=resultado)
        context.bot_data["iphone_stock"] = resultado
