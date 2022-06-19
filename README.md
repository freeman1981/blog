## Жизненный цикл 

0. Пока проект развивается версии не фиксирую - поэтому нужно посматривать на конфиг автосгенеренный.
1. Создал директорию app, положил туда Dockerfile, requirements. Снаружи композ.
2. `docker-compose run -u $UID:$(id -g $UID) app django-admin startproject project .`
3. `docker-compose run -u $UID:$(id -g $UID) app ./manage.py startapp main`
4. Сеттинги оформляем в виде пакета, грепаем `project.settings` и меняем на `project.settings.main`
5. Модели меняем `docker-compose run -u $UID:$(id -g $UID) app ./manage.py makemigrations`


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

`docker-compose run app ./manage.py migrate`

Чтобы избежать утомительного заполнения данными таблиц для локального тестирования, используем `dumpdata` по мере необходимости
`docker-compose run -u $UID:$(id -g $UID) app ./manage.py dumpdata -o mydata.json.gz`
`sudo tar -zcvf app/media.tar.gz app/media`

... а потом
`docker-compose run -u $UID:$(id -g $UID) app ./manage.py loaddata mydata`
`tar -zxvf app/media.tar.gz`


`docker-compose run app ./manage.py createsuperuser`

Админка по адресу `http://localhost:8000/admin/`
api по адресу `http://localhost:8000/schema/swagger/`

## TODO

0. авторизация более продвинутая
1. try asgi
2. try psycopg3
3. logging
