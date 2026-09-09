# Для ядра нужно чтобы было одинаково для переиспользования слоев
FROM python:3.12.2

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY deploy/requirements.txt /tmp/requirements.txt
RUN uv pip install --system --no-cache --requirement /tmp/requirements.txt
