from django.apps import AppConfig
# from django_apscheduler.jobstores import DjangoJobStore
# from apscheduler.schedulers.background import BackgroundScheduler
# from mailing_app.tasks import send_mailing_job

class MailingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing_app'

    # def ready(self):
    #     if self.scheduler is None:
    #         self.scheduler = BackgroundScheduler()
    #         self.scheduler.add_jobstore(DjangoJobStore(), "default")
    #         self.scheduler.add_job(send_mailing_job, 'interval', minutes=1)  # запускаем каждую минуту
    #         self.scheduler.start()
