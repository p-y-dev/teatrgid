from django.db import models
from teatrgid.models import SortGeneralModel


class Person(SortGeneralModel):
    class Meta:
        abstract = True

    name = models.CharField(
        verbose_name="Имя",
        max_length=120
    )


class Actors(Person):
    class Meta:
        verbose_name_plural = "Актеры"
        verbose_name = "Актер"
        ordering = ('-my_order',)


class Directors(Person):
    class Meta:
        verbose_name_plural = "Режиссеры"
        verbose_name = "Режиссер"
        ordering = ('-my_order',)
