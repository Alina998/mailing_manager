from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    user_country = models.CharField(max_length=56, blank=True, null=True)
    user_photo = models.ImageField(
        upload_to="users/photo", blank=True, null=True, verbose_name="Фото", help_text="Загрузите фото"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.email
