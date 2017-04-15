from django.db import models
from ..models import GeneralModel
from ..general_information.models import ListGenres, ListAgeRestrictions
from ..theaters.models import Theaters


class Performance(GeneralModel):
    class Meta:
        verbose_name_plural = "Спектакли"
        verbose_name = "Спектакль"
        ordering = "-publication_date",

    genres = models.ManyToManyField(
        ListGenres,
        verbose_name="Жанры",
    )

    age_restrictions = models.ForeignKey(
        ListAgeRestrictions,
        verbose_name="Возастное ограничение",
        default=""
    )

    theaters = models.ManyToManyField(
        Theaters,
        verbose_name="Театры",
        default=""
    )

