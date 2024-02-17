# Yatube Final Api

## Описание
Yatube — это платформа для блогов. API Yatube предоставляет разнообразные методы взаимодействия, позволяющие пользователям управлять своими блогами, комментариями и подписками.

## Используемые библиотеки
- Django==3.2.16
- pytest==6.2.4
- pytest-pythonpath==0.7.3
- pytest-django==4.4.0
- djangorestframework==3.12.4
- djangorestframework-simplejwt==4.7.2
- Pillow==9.3.0
- PyJWT==2.1.0
- requests==2.26.0

## Установка

Следуйте этим шагам, чтобы установить проект на вашей локальной машине:

1. Клонируйте репозиторий:
    ```
    git clone https://github.com/DmitryBurmagin/api_final_yatube.git
    ```

2. Перейдите в директорию проекта:
    ```
    cd api_final_yatube
    ```

3. Создайте виртуальное окружение и активируйте его:
    ```
    python3 -m venv env
    source env/bin/activate
    ```

4. Установите зависимости:
    ```
    pip install -r requirements.txt
    ```

5. Примените миграции:
    ```
    python manage.py migrate
    ```

6. Запустите сервер Django:
    ```
    python manage.py runserver
    ```

## Примеры использования

В Yatube API вы можете создавать посты, комментарии, группы (только админ), и подписываться на других пользователей. Вот некоторые примеры маршрутов, которые вы можете использовать:

- Создание поста: `http://127.0.0.1:8000/api/v1/posts/`
- Создание группы: `http://127.0.0.1:8000/api/v1/groups/`
- Создание комментария к посту: `http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/`
- Подписка на пользователя: `http://127.0.0.1:8000/api/v1/follow/`

Примеры использования `curl` для создания поста, добавления комментария и подписки на пользователя:

1. **Создание поста:**
    ```
    curl --location 'http://127.0.0.1:8000/api/v1/posts/' \
    --header 'Authorization: Bearer {token}' \
    --header 'Content-Type: application/json' \
    --data '{"text": "string"}'
    ```
    Ответ:
    ```json
    {
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
    }
    ```

2. **Добавление комментария:**
    ```
    curl --location 'http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/' \
    --header 'Authorization: Bearer {token}' \
    --header 'Content-Type: application/json' \
    --data '{"text": "string"}'
    ```
    Ответ:
    ```json
    {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
    }
    ```

3. **Подписка на пользователя:**
    ```
    curl --location 'http://127.0.0.1:8000/api/v1/follow/' \
    --header 'Authorization: Bearer {token}' \
    --header 'Content-Type: application/json' \
    --data '{"following": "string"}'
    ```
    Ответ:
    ```json
    {
    "user": "string",
    "following": "string"
    }
    ```

## Автор
Этот проект является форком оригинального проекта Yatube, созданного в Яндекс Практикум. Форк создан Дмитрием Бурмагиным.
