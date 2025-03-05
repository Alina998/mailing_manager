import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore

from mailing_app.models import Mailing, MailingAttempt

logger = logging.getLogger(__name__)


# def my_job():
#     print('Hello')


def send_mailing_job():
    mailings = Mailing.objects.filter(status="запущена")
    for mailing in mailings:
        for recipient in mailing.recipient_list.all():
            try:
                send_mail(
                    mailing.letter.subject,
                    mailing.letter.letter,
                    "alina.pastaeva@yandex.ru",
                    [recipient.email],
                    fail_silently=False,
                )
                MailingAttempt.objects.create(mailing=mailing, status="Успешно", response="Письмо отправлено")
            except Exception as e:
                MailingAttempt.objects.create(mailing=mailing, status="Не успешно", response=str(e))
                logger.error(f"Ошибка при отправке письма {recipient.email} для рассылки {mailing.id}: {str(e)}")


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            send_mailing_job,
            trigger=CronTrigger(second="*/10"),
            id="send_mailing_job",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Запуск задачи отправки рассылки..")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
