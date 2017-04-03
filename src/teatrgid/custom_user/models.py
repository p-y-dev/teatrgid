from django.db import models
from django.contrib.auth.models import AbstractUser

from teatrgid.general_information.models import ListCity


class User(AbstractUser):
    city = models.ForeignKey(ListCity, on_delete=models.CASCADE, null=True, verbose_name="Город")
