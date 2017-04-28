from django.db import models
from ..general_information.models import ListCity


class CurrentResourcesClass(models.Model):
    class Meta:
        abstract = True

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


class ThirdpartyResources(CurrentResourcesClass):
    class Meta:
        verbose_name_plural = "Сторонние ресуры"
        verbose_name = "Сторонние ресуры"


class Advertising(CurrentResourcesClass):
    class Meta:
        verbose_name_plural = "Реклама"
        verbose_name = "Реклама"
