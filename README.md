# Zavarka39 - Интернет магазин китайского чая

Добро пожаловать в Zavarka39 - ваш источник качественного китайского чая. Этот проект представляет собой интернет-магазин, разработанный с использованием технологий Docker, Django, Gunicorn, Celery, Pillow и Flower.

## Требования

- Docker
- Docker Compose

## Запуск проекта

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/mist3s/django_shop_v2.git
    ```

2. Перейдите в каталог проекта:

    ```bash
    cd django_shop_v2
    ```

3. Запустите контейнеры с помощью Docker Compose:

    ```bash
    docker-compose up -d
    ```

    Это создаст и запустит контейнеры Django, RabbitMQ, Celery, Flower и Nginx.

4. Откройте веб-браузер и перейдите по адресу http://localhost:8000 для доступа к интернет-магазину, а также по адресу http://localhost:5555 для мониторинга Celery с использованием Flower.

## Остановка проекта

1. Остановите контейнеры:

    ```bash
    docker-compose down
    ```

## Структура проекта

- `backend/`: Django-приложение и настройки проекта.
- `nginx/`: Конфигурация Nginx для проксирования запросов к Django и Flower.
- `docker-compose.yml`: Файл настройки Docker Compose с определением сервисов и объемов данных.

## Используемый стек

- Docker
- Django 4.2.7
- Gunicorn 20.1.0
- Celery 5.3.1
- Pillow 10.1.0
- Flower 2.0.1

## Автор

Андрей Иванов
