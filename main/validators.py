from rest_framework import serializers


WORDS_URL = ['https://www.youtube.com/', 'www.youtube.com']

def UrlValidator(value):
    if value.lower() not in WORDS_URL:
        raise serializers.ValidationError("Нельзя использовать ссылки на сторонние ресурсы, кроме 'youtube.com'")


# POST: http://localhost:8000/lessons/create/

{
    "name": "Django DRF",
    "description": "основные концепции и инструменты Django REST framework (DRF) для разработки мощных и масштабируемых RESTful API.",
    "course": "Профессия Python разработчик 3.0",
    "link_video": "https://www.youtube.com/"
}