## Модуль 8 от SkyPro. Docker. Для работы используется Linux Manjaro

## 27.2. Docker Compose. Домашние задание
### (ветка 27.2._HW_Docker_Compose)

### Реализовано в проекте:

#### 1. Установлен Docker, docker compose. 
        - sudo pacman -Syu
        - sudo pacman -S docker
            - docker --version
        - sudo pacman -S docker compose 
            - docker-compose --version

#### 2. Создан и описан в корне проекта: Dockerfile, docker-compose.yaml
        - python:3.11-slim-buster

#### 3. Собран образ и запущен контейнер
        - docker-compose build
        - docker-compose up

#### 4. Запуск проекта одной командой
        - docker-compose up -d --build

#### 5. Проверяем проект на работоспособность
        - localhost:8000


__________________________________________________________________________________________________________
## Модуль 7 от SkyPro. Django REST framework

## 24.1 Вьюсеты и дженерики. Домашнее задание 
### (ветка 24.1_HW_ViewSet_Generic)

### Реализовано в проекте:

#### 1. Создан новый Django-проект, настроено виртальное окружение - venv, подключен и настроен - DRF.
        - pip install djangorestframework
        - config.settings.py: INSTALLED_APPS = ['rest_framework',]

#### 2. Создано два приложения - main, users. Созданы следующие модели:
        - Main. Model Course, поля: name, preview, description, user (ForeignKey, settings.AUTH_USER_MODEL)
                Model Lesson, поля: name, description, image, link_video, user (ForeignKey, settings.AUTH_USER_MODEL)

        - Users. Model User, поля: email (unique=True), name, phone, city, avatar.

#### 3. Созданы сериализаторы, CRUD для моделей Course (ViewSets), Lesson (Generic-классы)
        - Сериализаторы: CourseSerializer, LessonSerializer.
        - ViewSets: CourseViewSet
        - Generic: LessonCreateAPIView, LessonRetrieveAPIView, LessonListAPIView, LessonUpdateAPIView, LessonDestroyAPIView

________________________________________________________________________________________________________________________

## 24.2 Сериализаторы. Домашнее задание 
### (ветка 24.2_HW_Сериализаторы)

### Реализовано в проекте:

#### 1. Для модели курса добавлен сериализатор поле вывода количества уроков, и поле вывода уроков
        - lessons_count = serializers.SerializerMethodField()
        - lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

#### 2. Добавлена новая модель Payment (платеж), и поля для модели. В модель через фикстуры добавлены данные.
        - Payment: user, date_payment, paid_course, payment_amount, payment_method, is_paid.
        - python manage.py fill ('data.json')
        - использован метод SlugRelatedField, выведется название поля вместо цифры (смотри GET_lessons_README.txt)

#### 3. Настроена фильтрация для эндпоинтов вывода списка платежей с возможностями:
        - Сортировки по дате оплаты filters.OrderingFilter
        - фильтр по курсу SearchFilter
        - фильтр по способу оплаты filters.SearchFilter

_____________________________________________________________________________________________________________________

## 25.1 Права доступа в DRF. Домашнее задание 
### (ветка 25.1_HW_Права-доступа-в-DRF)

### Реализовано в проекте:

#### 1. Настроена авторизация JWT-авторизация, установлены права доступа для неавторизованных пользователей
        - djangorestframework-simplejwt (JWTAuthentication)
        - rest_framework.permissions.IsAuthenticated

#### 2. Создана группа модераторов с правами: смотреть, редактировать уроки, но без возможности удалять и создавать новые
        - main/permissions.py/IsModerator

#### 3. Созданы права доступа для пользователей которые могут видеть и редактировать только свои уроки.
        - main/permissions.py/IsOwner

_____________________________________________________________________________________________________________________

## 26.1 Документирование и безопасность
### (ветка 26.1_HW_Документирование_и_безопасность)

### Реализовано в проекте:

#### 1. Настроен вывод документации проетка с помощью swagger.
        - http://127.0.0.1:8000/docs/

#### 2. Подключена система оплаты курса через request. Выводится ссылка на оплату товара.
        - https://stripe.com/docs/api.
        - https://checkout.stripe.com/c/pay/cs_test_a1yC2Piv7z0iLcQzupFecqpuz0VNSw2r2j0HHSiSCml7O0WiLo7HYdrPYl#fidkdWxOYHwnPyd1blpxYHZxWjA0S2NgQ2tGND1AMGhVYmxAV00zYzFGd01OUE5BRj1kZlB2Zms3bmpcQWpEdnR3MWNRVENmQnRhYUNPRHZMQGtKcG00ZkZDMXZQMmpTTGt9M0R9c0hRfENONTU1QFR8MndTMicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"

______________________________________________________________________________________________________________________

## 26.2. Celery
### (ветка 26.2_HW_Celery)

### Реализовано в проекте:

#### 1. Настроен проект для работы с Celery, и celery-beat для выполнения последующих задач.
        - config/settings.py
        - config/celery.py
        - config/__init__.py

#### 2.  Добавлена асинхронная рассылка писем пользователям об обновлении материалов курса.
        - main/tasks.py

#### 3. С помощью celery-beat реализована фоновая задача, которая будет проверять пользователей 
#### по дате последнего входа по полю last_login и, если пользователь не заходил более месяца, блокировать его с помощью флага is_active.
        - main/tasks.py
    
    Команда для Windows:
    - при указании обработчика событий необходимо добавить флаг -P eventlet
    - celery -A config worker -l INFO -P eventlet
    - celery -A my_project beat —loglevel=info

    Redis официально не поддерживается в Windows: 
    - Установите WSL2, Ubuntu. Подробности смотрите тут https://redis.io/docs/getting-started/installation/install-redis-on-windows/
    - sudo apt-get update (обновление)
    - sudo service redis-server start
    - redis-cli
    - Проверка работает ли сервер Redis: введите Ping, ответ от сервера: Pong
    - в IDE через командну строку установите redis: pip install redis

        Команда для Unix:
    - redis-cli
