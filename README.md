# TechStore - Онлайн-магазин электроники

 Настройка окружения
Создайте файл .env в корне:

env
DATABASE_URL=postgresql://user:password@db:5432/techstore
REDIS_URL=redis://redis:6379
SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

 Тестирование
# Запуск тестов
cd backend
pytest

# Запуск с покрытием
pytest --cov=app tests/

Современная платформа электронной коммерции для продажи электроники и гаджетов.

## 🚀 Особенности
- Микросервисная архитектура
- Мультивалютные платежи
- Персонализированные рекомендации
- Международная доставка
- Real-time уведомления

## 🛠 Технологии
- **Backend:** Python 3.11, FastAPI, SQLAlchemy
- **Frontend:** React 18, TypeScript, Tailwind CSS
- **Базы данных:** PostgreSQL, Redis, Elasticsearch
- **Инфраструктура:** Docker, Kubernetes, Nginx

## 📦 Быстрый старт

1. Клонирование репозитория

git clone https://github.com/yourusername/techstore-online.git
cd techstore-online

2. Запуск докер

docker-compose up -d

3. Доступ к приложению

Frontend: http://localhost:3000
Backend API: http://localhost:8000
API документация: http://localhost:8000/docs
Админ-панель: http://localhost:8000/admin
