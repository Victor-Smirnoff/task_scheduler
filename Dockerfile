# Используем официальный образ Python как базовый
FROM python:3.12-slim as base

# Многослойный билд: использование базового образа для разработки
FROM base AS dev

# Устанавливаем переменную окружения, чтобы Python не сохранял файлы .pyc
ENV PYTHONUNBUFFERED 1

# Устанавливаем переменную окружения, чтобы Python сразу сбрасывал буфер вывода (важно для логов в Docker)
ENV PYTHONDONTWRITEBYTECODE 1

# Обновляем pip и создаем виртуальное окружение
RUN set -ex \
    && mkdir /venv \
    && pip --no-cache-dir install -U pip \
    && python -m venv /venv

# Копируем файл requirements.txt в контейнер
COPY ./requirements.txt /app/

# Копируем файл requirements.dev.txt в контейнер
COPY ./requirements.dev.txt /app/

# Устанавливаем зависимости
RUN set -ex \
    && /venv/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && /venv/bin/pip install --no-cache-dir -r /app/requirements.dev.txt

FROM base
# Копируем виртуальное окружение из образа dev
COPY --from=dev /venv /venv

# Копируем весь проект в рабочую директорию контейнера
COPY ./src /app

# Устанавливаем рабочую директорию
WORKDIR /app
