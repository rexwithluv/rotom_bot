from telegram.ext import Application, ApplicationBuilder, CommandHandler

from src.commands import get_chat_id, get_mediamarkt, get_medico
from src.configuration import Configuration
from src.jobs import iphone_job, medico_job

config = Configuration("config.toml")


async def post_init(application: Application) -> None:
    msg: str = "¡Hola! Ya estoy online :)"
    await application.bot.send_message(chat_id=config.chat_id, text=msg)
    print(msg)


if __name__ == "__main__":
    bot_token: str = config.bot_token
    job_interval: int = config.job_interval

    app = ApplicationBuilder().token(config.bot_token).post_init(post_init).build()

    app.add_handler(CommandHandler("chat_id", get_chat_id))
    app.add_handler(CommandHandler("medico", get_medico))
    app.add_handler(CommandHandler("phone", get_mediamarkt))

    job_queue = app.job_queue
    job_queue.run_repeating(medico_job, interval=job_interval, chat_id=config.chat_id)
    job_queue.run_repeating(iphone_job, interval=job_interval, chat_id=config.chat_id)

    app.run_polling()
