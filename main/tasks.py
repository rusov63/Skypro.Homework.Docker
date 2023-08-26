from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail
from main.models import Payment
from main.services import PaymentService
from django.conf import settings

from users.models import User


@shared_task
def send_message_a_course_update(course_title, version, user_email):
    """Отправка письма пользователям об обновлении материалов курса."""

    send_mail(
        subject="Обновление курса!",
        message=f"У курса {course_title} появилось обновление - {version}!",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email]
    )

@shared_task
def check_user():
    now_date = datetime.now()
    one_month_ago = now_date - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago)
    inactive_users.update(is_active=False)
    print(inactive_users)