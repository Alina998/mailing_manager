from django.db import models


class Recipient(models.Model):
    email = models.CharField(max_length=100, verbose_name='E-mail', help_text='Введите e-mail получателя')
    name = models.CharField(max_length=100, verbose_name='ФИО', help_text='Введите ФИО получателя')
    comment = models.CharField(max_length=500, verbose_name='Комментарий', help_text='Введите комментарий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'


class Letter(models.Model):
    subject = models.CharField(max_length=100, verbose_name='Тема письма', help_text='Введите тему письма')
    letter = models.CharField(max_length=10000, verbose_name='Содержание письма', help_text='Введите содержание письма')


class Mailing(models.Model):
    mail_status = ['Завершена', 'Создана', 'Запущена']
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата первой отправки')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата окончания отправки')
    status = models.CharField(max_length=100, verbose_name='Статус рассылки', help_text='Выберите статус рассылки', choices=mail_status)
    letter_text = models.ForeignKey(Letter, on_delete=models.SET_NULL, verbose_name='Сообщение', help_text='Выберите сообщение для рассылки', null=True, blank=True)
    recipient_list = models.ManyToManyField(Recipient)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
