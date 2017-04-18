from django.db import models
from datetime import datetime

from ..models import GeneralModel, Gallery
from ..general_information.models import ListGenres, ListAgeRestrictions
from ..theaters.models import Theaters
from ..persons.models import Actors, Directors


class PerformanceReviews(models.Model):
    class Meta:
        verbose_name_plural = "Отзывы"
        verbose_name = "Отзывы"
        ordering = "-publication_date",

    publication_date = models.DateTimeField(
        verbose_name="Дата публикации",
        default=datetime.now,
        blank=True
    )


class PerformanceGallery(Gallery):
    performance = models.ForeignKey("Performance", on_delete=models.CASCADE)


class DatesEvent(models.Model):
    class Meta:
        verbose_name_plural = "Даты проведения"
        verbose_name = "Даты проведения"
        ordering = "date_time",

    date_time = models.DateTimeField(
        verbose_name="Дата и время",
        blank=True,
    )

    duration = models.TimeField(
        verbose_name="Продолжительность",
        blank=True,
    )

    is_intermission = models.BooleanField(
        verbose_name="Есть антракт?",
        default=False
    )

    count_intermission = models.PositiveIntegerField(
        verbose_name="Количество антрактов",
        blank=True,
        default=0
    )

    performance = models.ForeignKey("Performance", on_delete=models.CASCADE)


class Performance(GeneralModel):
    class Meta:
        verbose_name_plural = "Спектакли"
        verbose_name = "Спектакль"

    genres = models.ManyToManyField(
        ListGenres,
        verbose_name="Жанры",
    )

    age_restrictions = models.ForeignKey(
        ListAgeRestrictions,
        verbose_name="Возастное ограничение",
        default=""
    )

    theater = models.ForeignKey(
        Theaters,
        verbose_name="Театры",
        default=""
    )

    actors = models.ManyToManyField(
        Actors,
        verbose_name="Актеры",
        default=""
    )

    directors = models.ManyToManyField(
        Directors,
        verbose_name="Режиссеры",
        default=""
    )

    link_order = models.CharField(
        verbose_name="Ссылка на покупку билетов",
        max_length=240,
        default=""
    )

    rating = models.FloatField(
        verbose_name="Рейтинг",
        default=0
    )

    reviews = models.ManyToManyField(
        PerformanceReviews,
        verbose_name="Отзывы"
    )

    top_today = models.BooleanField(
        verbose_name="Выводить в топ сегодня?",
        default=False
    )

    top_soon = models.BooleanField(
        verbose_name="Выводить в топ скоро?",
        default=False
    )
