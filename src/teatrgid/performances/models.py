from django.db import models
from ..models import GeneralModel
from ..general_information.models import ListGenres
from ..general_information.models import ListAgeRestrictions


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
