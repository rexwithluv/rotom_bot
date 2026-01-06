from telegram.ext import ApplicationBuilder, CommandHandler

from src.configuration import Configuration
from src.commands import get_chat_id, get_medico
from src.jobs import medico_job

config = Configuration("config.toml")


if __name__ == "__main__":
    app = ApplicationBuilder().token(config.bot_token).build()

    app.add_handler(CommandHandler("chat_id", get_chat_id))
    app.add_handler(CommandHandler("medico", get_medico))

    job_queue = app.job_queue
    job_queue.run_repeating(medico_job, interval=30, first=3, chat_id=config.chat_id)

    print("Bot encendido <3")
    app.run_polling()
