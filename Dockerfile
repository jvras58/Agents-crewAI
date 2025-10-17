FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

RUN groupadd --system --gid 999 nonroot \
 && useradd --system --gid 999 --uid 999 --create-home nonroot

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1

ENV UV_LINK_MODE=copy

# Use a writable cache directory inside the image to avoid buildkit writing to /root
ENV UV_CACHE_DIR=/app/.cache/uv

# Ensure cache dir exists
RUN mkdir -p /app/.cache/uv

COPY uv.lock pyproject.toml /app/
RUN uv sync --locked --no-install-project --no-dev

COPY . /app
RUN uv sync --locked --no-dev

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT []

RUN chown -R nonroot:nonroot /app

USER nonroot

EXPOSE 8000

CMD ["uv", "run", "fastapi", "run", "app/startup.py", "--host", "0.0.0.0", "--port", "8000"]
