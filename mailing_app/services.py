from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from mailing_app.models import Mailing, MailingAttempt
from datetime import datetime
import os


def send_mailing(mailing_id):
    mailing = Mailing.objects.get(id=mailing_id)
    mailing.status = 'Запущена'
    mailing.save()

    for recipient in mailing.recipients.all():
        try:
            send_mail(
                mailing.message.subject,
                mailing.message.body,
                os.getenv('EMAIL_HOST_USER'),
                [recipient.email],
            )
            MailingAttempt.objects.create(
                mailing=mailing,
                status='Успешно',
                response='Письмо отправлено успешно.'
            )
        except Exception as e:
            MailingAttempt.objects.create(
                mailing=mailing,
                status='Не успешно',
                response=str(e)
            )

    mailing.status = 'Завершена'
    mailing.end_time = datetime.now
    mailing.save()