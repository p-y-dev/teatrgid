from django.db import models
from teatrgid.models import GeneralModel
from ..general_information.models import ListGenres


class Performance(GeneralModel):
    class Meta:
        verbose_name_plural = "Спектакли"
        verbose_name = "Спектакль"
        ordering = ("-publication_date",)

    genres = models.ManyToManyField(
        ListGenres,
        verbose_name="Жанры",
    )
