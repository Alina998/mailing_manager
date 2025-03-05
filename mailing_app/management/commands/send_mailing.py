from django.core.management.base import BaseCommand
from mailing_app.models import Mailing
from mailing_app.services import send_mailing


class Command(BaseCommand):
    help = 'Отправка рассылки по ID'

    def add_arguments(self, parser):
        parser.add_argument('mailing_id', type=int, help='ID рассылки для отправки')

    def handle(self, *args, **kwargs):
        mailing_id = kwargs['mailing_id']
        try:
            send_mailing(mailing_id)
            self.stdout.write(self.style.SUCCESS(f'Рассылка {mailing_id} успешно отправлена!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при отправке рассылки: {str(e)}'))
            
