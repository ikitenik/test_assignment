#!/bin/bash
set -e

echo "🛠️ Применяем миграции..."
python manage.py migrate --noinput

echo "👤 Создаём суперпользователя (если не существует)..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin123")
END

echo "🚀 Запускаем сервер..."
exec "$@"