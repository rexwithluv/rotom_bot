from .scrapers.sergas import check_cupo_medico_sergas
from telegram.ext import ContextTypes


async def medico_job(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    resultado = await check_cupo_medico_sergas()
    await context.bot.send_message(chat_id=chat_id, text=resultado)
