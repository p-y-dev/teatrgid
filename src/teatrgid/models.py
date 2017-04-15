from django.db import models
from datetime import datetime
from autoslug import AutoSlugField
from teatrgid.general_information.models import ListCity


class GeneralModel(models.Model):
    class Meta:
        abstract = True

    thumbnail = models.ImageField(
        verbose_name="Миниатюра",
        upload_to='img/thumbnail/',
    )

    name = models.CharField(
        verbose_name="Название",
        max_length=120
    )

    city = models.ForeignKey(
        ListCity,
        verbose_name="Город",
        blank=True
    )

    publication_date = models.DateTimeField(
        verbose_name="Дата публикации",
        default=datetime.now,
        blank=True
    )

    slug = AutoSlugField(
        verbose_name='Slug',
        populate_from="name",
        unique=True,
        blank=True
    )

    def __str__(self):
        return self.name


class SortGeneralModel(GeneralModel):
    class Meta(object):
        abstract = True

    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)