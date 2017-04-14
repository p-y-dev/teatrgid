from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from ..admin import AdminModelWithCity
from teatrgid.general_information.models import City, ListCity, Genres, ListGenres, \
                                                AgeRestrictions, ListAgeRestrictions


class ListCityAdmin(admin.TabularInline):
    model = ListCity


class ListGenresAdmin(admin.TabularInline):
    model = ListGenres


class ListAgeRestrictionsAdmin(admin.TabularInline):
    model = ListAgeRestrictions


class CityAdmin(SingleModelAdmin):
    inlines = [
        ListCityAdmin,
    ]


class GenresAdmin(SingleModelAdmin):
    inlines = [
        ListGenresAdmin,
    ]


class AgeRestrictionsAdmin(SingleModelAdmin, AdminModelWithCity):
    exclude = "",

    inlines = [
        ListAgeRestrictionsAdmin,
    ]


admin.site.register(City, CityAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(AgeRestrictions, AgeRestrictionsAdmin)
