from django.db import models
from teatrgid.models import SortGeneralModel


class Actors(SortGeneralModel):
    class Meta:
        verbose_name_plural = "Актеры"
        verbose_name = "Актер"
        ordering = ('my_order',)

    name = models.CharField(
        verbose_name="Имя",
        max_length=120
    )

