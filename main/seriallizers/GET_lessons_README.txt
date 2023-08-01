class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор представление модели Lesson"""

    # название курса вместо цифры
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

# При заполнении БД если между моделями есть связь (ForeighnKey) в поле атрибута (Postman) JSON ставим 1, и
# через метод SlugRelatedField выведется название поля вместо цифры.

[
    {
        "id": 1,
        "name": "Введение в программирование",
        "course": "Профессия Python разработчик 3.0",
        "user": null
    },
    {
        "id": 2,
        "name": "Основы синтаксиса",
        "course": "Профессия Python разработчик 3.0",
        "user": null
    },
    {
        "id": 3,
        "name": "Списки и циклы",
        "course": "Профессия Python разработчик 3.0",
        "user": null
    },
    {
        "id": 4,
        "name": "Строки и словари",
        "course": "Профессия Python разработчик 3.0",
        "user": null
    }
]