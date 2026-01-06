FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libnss3 \
    libnspr4 \
    libgbm1 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project

RUN uv run playwright install chromium --with-deps

COPY . .

CMD [ "uv", "run", "main.py" ]