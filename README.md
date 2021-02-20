# TestCEC_django

Тестовое Задание. backend часть (frontend часть на https://github.com/SergeiTabinaev/TestCEC_react) 

Todo лист с выбором категорий и авторизацией и регистрацией(jwt токены).

Использованы следующие технологии: Django REST framework. PostgresSQL

Как использовать: 

Клонировать репозиторий git clone ссылка_сгенерированная_в_вашем_репозитории 

Создать виртуальное окружение python -m venv venv 

Активировать виртуальное окружение 

В файле .env прописать конект к БД. сделать миграции: manage.py migrate, manage.py migrate. 

Cоздать суперпользователя: manage.py createsuperuser

Устанавливить зависимости: pip install -r reqы.txt 

Запустить сервер python manage.py runserver 

Открыть http://127.0.0.1:8000/swagger/

)создать пользователя(auth/users post запрос) 

)войти (auth/jwt/create)

)категории и таски - там все просто
