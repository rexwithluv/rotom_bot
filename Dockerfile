FROM ghcr.io/astral-sh/uv:alpine

WORKDIR /app

COPY . /app

RUN uv sync

CMD [ "uv", "run", "main.py" ]