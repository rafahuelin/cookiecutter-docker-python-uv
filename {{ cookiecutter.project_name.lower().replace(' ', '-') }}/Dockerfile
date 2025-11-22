FROM python:{{cookiecutter._supported_python_versions[cookiecutter.python_version].latest}}-slim-bookworm AS lock

COPY --from=ghcr.io/astral-sh/uv:{{cookiecutter._uv_version}} /uv /uvx /usr/local/bin/

COPY pyproject.toml ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv lock

FROM python:{{cookiecutter._supported_python_versions[cookiecutter.python_version].latest}}-{{cookiecutter._debian_variant}} AS base

COPY --from=ghcr.io/astral-sh/uv:{{cookiecutter._uv_version}} /uv /uvx /usr/local/bin/

COPY pyproject.toml uv.lock ./

ENV UV_PROJECT_ENVIRONMENT="/usr/local/" \
    PYTHONPATH="/app/src" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

WORKDIR /app

COPY . .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

FROM base AS dev

ARG USER
ARG UID
ARG GID

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --group dev

# Install tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    git \
    openssh-client \
    libglib2.0-0 \
    libx11-6 \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user with matching UID/GID and grant sudo access
RUN groupadd -g $GID -o $USER && \
    useradd -ms /bin/bash -u $UID -g $GID $USER && \
    usermod -aG sudo $USER && \
    echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Change ownership of the app, bin and python directory global Python directories
RUN chown -R $USER:$USER /app /usr/local/bin /usr/local/lib/python{{cookiecutter.python_version}} /usr/local/lib/python{{cookiecutter.python_version}}/site-packages

USER $USER

WORKDIR /app


FROM base AS prod

USER root

RUN chown -R root:root /app /usr/local/bin /usr/local/lib/python{{cookiecutter.python_version}} /usr/local/lib/python{{cookiecutter.python_version}}/site-packages

RUN useradd -ms /bin/bash app

USER app

WORKDIR /app

CMD ["python", "/app/src/main.py"]