from django.db import models
from ..general_information.models import ListCity


class ThirdpartyResources(models.Model):
    class Meta:
        verbose_name_plural = "Сторонние ресуры"
        verbose_name = "Сторонние ресуры"

    name = models.CharField(
        verbose_name="Название",
        max_length=120
    )

    thumbnail = models.ImageField(
        verbose_name="Миниатюра",
        upload_to='img/thumbnail/',
    )

    link = models.CharField(
        verbose_name="Ссылка на ресурс",
        max_length=120
    )

    city = models.ForeignKey(
        ListCity,
        verbose_name="Город",
        blank=True
    )

    def __str__(self):
        return self.name
