from django.db import models
from datetime import datetime
from autoslug import AutoSlugField
from ..general_information.models import ListCity


class Performance(models.Model):
    class Meta:
        verbose_name_plural = "Спектакли"
        verbose_name = "Спектакль"
        ordering = ("-publication_date",)

    thumbnail = models.ImageField(
        verbose_name="Миниатюра",
        upload_to='img/performances/',
    )

    name = models.CharField(
        verbose_name="Название",
        max_length=120
    )

    city = models.ForeignKey(
        ListCity,
        verbose_name="Город",
        on_delete=models.CASCADE,
        blank=True
    )

    publication_date = models.DateTimeField(
        verbose_name="Дата публикации",
        default=datetime.now,
        blank=True
    )

    slug = AutoSlugField(
        verbose_name='Slug спектакля',
        populate_from="name",
        unique=True,
        blank=True
    )

    def __str__(self):
        return self.name
