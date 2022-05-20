## Жизненный цикл 

0. Пока проект развивается версии не фиксирую - поэтому нужно посматривать на конфиг автосгенеренный.
1. Создал директорию app, положил туда Dockerfile, requirements. Снаружи композ.
2. `docker-compose run -u $UID:$(id -g $UID) app django-admin startproject project .`
3. `docker-compose run -u $UID:$(id -g $UID) app python manage.py startapp main`
4. Сеттинги оформляем в виде пакета, грепаем `project.settings` и меняем на `project.settings.main`
5. Модели меняем `docker-compose run -u $UID:$(id -g $UID) app python manage.py makemigrations`


## Разработка

Интерпритатор на основе композа сервиса app

`docker-compose build`

`docker-compose up`

Проверка линтером

`docker-compose run -u $UID:$(id -g $UID) app flake8`

Фиксим импорты для линтера

`docker-compose run -u $UID:$(id -g $UID) app isort .`



## Старт

`docker-compose up`
... или в фоне
`docker-compose up -d`

`docker-compose run app python manage.py migrate`

`docker-compose run app python manage.py createsuperuser`

Админка по адресу `http://localhost:8000/admin/`
api по адресу `http://localhost:8000/schema/swagger/`

## TODO

0. авторизация более продвинутая
1. try asgi
2. try psycopg3
3. react
4. logging
5. new user
