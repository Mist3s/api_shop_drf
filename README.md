# Zavarka39 - Интернет магазин китайского чая

Это мой Pet-проект разрабатываемый с целью закрепления и отработки полученных знаний и навыков, в планах написать REST API на базе Django Rest Framework.

## Требования

- Docker
- Docker Compose

## Запуск проекта

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/mist3s/api_shop_drf.git
    ```

2. Перейдите в каталог проекта:

    ```bash
    cd api_shop_drf%0текука
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
- djangorestframework 3.14.0
- Gunicorn 20.1.0
- Celery 5.3.1
- Pillow 10.1.0
- Flower 2.0.1
- pytest 6.2.4
- pytest-django 4.4.0
- pytest-lazy-fixture 0.6.3
- drf-spectacular 0.27.1

## Автор

Python-разработчик [Андрей Иванов](https://github.com/Mist3s)
