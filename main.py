import logging

from telegram.ext import Application, ApplicationBuilder, CommandHandler

from src.commands import get_chat_id, get_mediamarkt, get_medico
from src.configuration import Configuration
from src.jobs import iphone_job, medico_job

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
config = Configuration("config.toml")


async def post_init(application: Application) -> None:
    msg: str = "¡Hola! Ya estoy online :)"
    await application.bot.send_message(chat_id=config.chat_id, text=msg)
    logger.info(msg)


def main() -> None:
    logger.info("Cargando configuración y arrancando el bot...")

    bot_token: str = config.bot_token
    job_interval: int = config.job_interval

    app = ApplicationBuilder().token(bot_token).post_init(post_init).build()
    app.bot_data["config"] = config

    app.add_handler(CommandHandler("chat_id", get_chat_id))
    app.add_handler(CommandHandler("medico", get_medico))
    app.add_handler(CommandHandler("iphone", get_mediamarkt))

    job_queue = app.job_queue

    logger.info(f"Programando jobs con un intervalo de {job_interval} segundos.")
    job_queue.run_repeating(medico_job, first=30, interval=job_interval)
    job_queue.run_repeating(iphone_job, first=30, interval=job_interval)

    app.run_polling()


if __name__ == "__main__":
    main()
