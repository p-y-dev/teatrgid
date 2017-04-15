from django.db import models
from teatrgid.models import SortGeneralModel


class Theaters(SortGeneralModel):
    class Meta:
        verbose_name_plural = "Театры"
        verbose_name = "Театр"
        ordering = ('my_order',)



