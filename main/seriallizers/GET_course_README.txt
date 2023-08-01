class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор представление модели Course"""

    # вывод всех уроков для курса.
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

    # метод вывода количества уроков для курса.
    lessons_count = serializers.SerializerMethodField()

[
    {
        "name": "Профессия Python разработчик 3.0",
        "description": "Основы backend-разработки",
        "lessons": [
            {
                "id": 4,
                "name": "Django",
                "description": "Основы веба",
                "course": "Профессия Python разработчик 3.0",
                "user": null
            },
            {
                "id": 1,
                "name": "Введение в программирование",
                "description": "Введение в профессию и основы алгоритмизации",
                "course": "Профессия Python разработчик 3.0",
                "user": null
            },
            {
                "id": 2,
                "name": "Основы синтаксиса",
                "description": "Оператор if. Переменная типа bool. Операторы сравнения",
                "course": "Профессия Python разработчик 3.0",
                "user": null
            },
            {
                "id": 3,
                "name": "Списки и циклы",
                "description": "Цикл for. Совмещаем цикл и условие",
                "course": "Профессия Python разработчик 3.0",
                "user": null
            }
        ],
        "lessons_count": 4
    }
]