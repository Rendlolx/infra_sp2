# API YaMDb
## _Проект для обмена данными с сервисом YaMDb через API_
## Описание:
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.
Запросы к API начинаются с
```sh
/api/v1/
```
## Установка:
1. Клонируйте репозиторий, перейдите в него:
```sh
git clone git@github.com:Rendlolx/api_yamdb.git
cd api_yamdb
```
2. Создайте и откройте файл ```.env``` с переменными оккружения:
```sh
cd infra
touch .env
```
3. Заполните ```.env``` файл, к примеру вот так:
```sh
DB_ENGINE=django.db.backends.postgresql
или
echo DB_ENGINE=django.db.backends.postgresql >> .env (For Linux/MacOS)

DB_NAME=postgres
или
echo DB_NAME=postgres >> .env (For Linux/MacOS)

POSTGRES_USER=postgres
или
echo POSTGRES_USER=postgres >> .env (For Linux/MacOS)

POSTGRES_PASSWORD=postgres
или
echo POSTGRES_PASSWORD=postgres >> .env (For Linux/MacOS)

DB_HOST=db
или
echo DB_HOST=db >> .env (For Linux/MacOS)

DB_PORT=5432
или
echo DB_PORT=5432 >> .env (For Linux/MacOS)

SECRET_KEY = "p&l%385148kslhtyn^##a1)ilz@4zqj=rq&agdol^##zgl9(vs"
или
echo SECRET_KEY = "p&l%385148kslhtyn^##a1)ilz@4zqj=rq&agdol^##zgl9(vs" >> .env (For Linux/MacOS)

DEBUG = False
или
echo DEBUG = False >> .env (For Linux/MacOS)
```
4. Установка и запуск приложения (Загрузив контейнер web из DockerHub):
```sh
docker-compose up -d
```
5. Примените миграции, создайте суперпользователя, сбор статики и заполните БД:
```sh
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

docker-compose exec web python manage.py collectstatic --no-input 

docker-compose exec web python manage.py loaddata fixtures.json
```

## Документация:
Более подробно с возможностями API можно ознакомиться в документации по адресу (После запуска проекта): 
```sh
http://127.0.0.1:8000/redoc/
```
