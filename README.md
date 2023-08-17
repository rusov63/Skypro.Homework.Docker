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
