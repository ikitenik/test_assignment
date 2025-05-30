# Используем официальный образ Ubuntu 24.04
FROM ubuntu:24.04 AS builder-image

# Избегаем зависания сборки из-за пользовательских запросов
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.12 python3.12-dev python3.12-venv python3-pip python3-wheel build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Создаем и активируем виртуальное окружение
RUN python3.12 -m venv /home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"

# Устанавливаем зависимости
COPY ./req.txt .
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r req.txt

FROM ubuntu:24.04 AS runner-image
RUN apt-get update && apt-get install --no-install-recommends -y python3.12 python3-venv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home myuser
COPY --from=builder-image /home/myuser/venv /home/myuser/venv
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chmod -R 777 /home/myuser

USER myuser
RUN mkdir /home/myuser/code
WORKDIR /home/myuser/code
COPY . .

EXPOSE 8000

# Убедимся, что все сообщения всегда доходят до консоли
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Активируем виртуальное окружение
ENV VIRTUAL_ENV=/home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]