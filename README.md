# 1. Клонируем
- git clone (link for repo)

# 2. Создать виртуальное окружение
- python3 -m venv .venv

# 3. Установить зависимости
- pip install -r requirements.txt

# 4. Активировать виртуальное окружение
- Для Windows -> .venv\Scripts\activate
- Для Linux -> source .venv/bin/activate

# 5. Подготовить минрацию
- python manage.py makemigrations

# 6. Запустить миграцию
- python manage.py migrate

# 7. Создать аккаунт суперпользователя
- python manage.py createsuperuser

# 8. Запустить сервер
- python manage.py runserver
