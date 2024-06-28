from django.core.mail import send_mail
from django.conf import settings


def send_email_for_feedback(email, name):
    send_mail(
        'Сообщение от Сергея Бойцова',
        f'Привет {name}, спасибо за обратную связь,
        в ближайшее время с вами свяжусь',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
