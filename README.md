# Проект API YaMDb

---

***Проект API YaMDb реализует API для сбора отзывов пользователей на произведения.***

---

## Содержание

- [О проекте](#about)
- [Начало работы](#getting_started)
- [Использование](#usage)
- [Планы](#todo)
- [Использованные средства и технологии](#tools_and_techs)
- [Авторы](#authors)
- [Благодарности](#acknowledgement)

## О проекте<div id="about"></div>

API YaMDb - это проектная работа десятого спринта курса "Python-разработчик" Яндекс.Практикум.

Этот проект реализует API будущего сайта, представляющего собой сервис по работе с произведениями.

Произведения делятся на категории:

- Книги,
- Фильмы,
- Музыка.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти. Из пользовательских оценок формируется усреднённая оценка произведения — рейтинг.

## Начало работы<div id="getting_started"></div>

Для работы с проектом необходимо выполнить действия, описанные ниже.

- Клонировать репозиторий и перейти в него в командной строке:

```sh
git@github.com:iReset/api_yamdb.git   # или
git@github.com:HelloAgni/api_yamdb.git   # или
git@github.com:Valery-VM/api_yamdb.git
cd api_yamdb
```

Создать и активировать виртуальное окружение:

```sh
python -m venv venv   # для Windows или
python3 -m venv venv  # для Linux и Mac

source venv/Scripts/activate   # для Windows или
source venv/bin/activate       # для Linux и Mac
```

Обновить pip и установить зависимости из файла:

```sh
python -m pip install --upgrade pip
pip install -r requirements.txt         # для выполнения или
pip install -r requirements-devel.txt   # для разработки
```

Скопировать файл с переменными окружения,сгенерировать секретный ключ:

```sh
cp .env.sample .env
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

и вставить выданное значение вместо значения параметра ``SECRET_KEY`` в файле ``.env``.

Выполнить миграции и заполнить базу данных:

```sh
python api_yamdb/manage.py migrate
python api_yamdb/manage.py import_data
```

## Использование<div id="usage"></div>

Для работы с API необходимо запустить проект:

```sh
python api_yamdb/manage.py runserver
```

Для получения документации по API необходимо открыть в браузере адрес <http://127.0.0.1/redoc/>.

Затем можно выполнять API-запросы к проекту.

## Использованные средства и технологии<div id="tools_and_techs"></div>

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [DRF Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [VSCode](https://code.visualstudio.com/)
- [Соглашение о коммитах](https://www.conventionalcommits.org/ru/v1.0.0/)

## Авторы<div id="authors"></div>

- [iReset](https://github.com/iReset) — управление пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения через e-mail
- [HelloAgni](https://github.com/HelloAgni) — категории (Categories), жанры (Genres) и произведения (Titles): модели, представления и эндпойнты для них
- [Valery-VM](https://github.com/Valery-VM) — отзывы (Review) и комментарии (Comments): описание моделей, представлений, настройка эндпойнтов, определение прав доступа для запросов, рейтинги произведений

## Благодарности<div id="acknowledgement"></div>

- Спасибо команде Яндекс.Практикум за создание курса
- Спасибо наставникам Денису Московченко, Алексею Михайлову и старшему студенту Антону Базуленкову за терпеливые и подробные разъяснения
- Спасибо куратору Екатерине Чапля за неустанную поддержку и организацию работы
- Спасибо команде когорты 28 за поддержку и сопровождение
- Спасибо однокурсникам когорты 28 за дружную команду
