from django.db import models
from django.conf import settings


class Recipient(models.Model):
    email = models.CharField(max_length=100, verbose_name='E-mail')
    name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.CharField(max_length=500, verbose_name='Комментарий')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipients', null=False,
                              default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'


class Letter(models.Model):
    subject = models.CharField(max_length=100, verbose_name='Тема письма')
    letter = models.CharField(max_length=10000, verbose_name='Содержание письма')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='letters', null=False,
                              default=1)


class Mailing(models.Model):
    mail_status = [
        ('завершена', 'Завершена'),
        ('создана', 'Создана'),
        ('запущена', 'Запущена'),
    ]
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата первой отправки')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата окончания отправки')
    status = models.CharField(max_length=100, verbose_name='Статус рассылки', help_text='Выберите статус рассылки', choices=mail_status)
    letter = models.ForeignKey(Letter, on_delete=models.SET_NULL, verbose_name='Сообщение', help_text='Выберите сообщение для рассылки', null=True, blank=True)
    recipient_list = models.ManyToManyField(Recipient)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mailings', null=False,
                              default=1)


    def __str__(self):
        return f"{self.status} - {self.letter.subject if self.letter else 'Без темы'}"

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ('Успешно', 'Успешно'),
        ('Не успешно', 'Не успешно'),
    ]

    attempt_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    response = models.TextField()
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)

    def __str__(self):
        return f"Attempt for {self.mailing} at {self.attempt_time}"