from django.db import models
from django.contrib.auth.models import User

from autoslug import AutoSlugField


class ListObj(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        verbose_name="Название",
        max_length=60,
    )

    slug = AutoSlugField(
        verbose_name='Slug',
        populate_from="name",
        unique=True,
        blank=True
    )

    def __str__(self):
        return self.name


class City(models.Model):
    class Meta:
        verbose_name_plural = "Города"


class ListCity(ListObj):
    class Meta:
        verbose_name_plural = "Список Городов"

    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Genres(models.Model):
    class Meta:
        verbose_name_plural = "Театральные жанры"


class ListGenres(ListObj):
    class Meta:
        verbose_name_plural = "Список жанров"

    genres = models.ForeignKey(Genres, on_delete=models.CASCADE)


class AgeRestrictions(models.Model):
    class Meta:
        verbose_name_plural = "Возрастные ограничения"


class ListAgeRestrictions(ListObj):
    class Meta:
        verbose_name_plural = "Список возрастных ограничений"

    age = models.PositiveIntegerField(
        verbose_name="Возраст",
    )

    age_restrictions = models.ForeignKey(AgeRestrictions, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    city = models.ForeignKey(ListCity, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
