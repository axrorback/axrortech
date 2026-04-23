FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    curl \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml uv.lock* ./

RUN uv sync --frozen --no-dev

COPY . .

RUN mkdir -p /app/staticfiles
RUN mkdir -p /app/media

EXPOSE 8000

CMD [
    "uv",
    "run",
    "gunicorn",
    "config.asgi:application",
    "-k",
    "uvicorn.workers.UvicornWorker",
    "--bind",
    "0.0.0.0:8000"
]