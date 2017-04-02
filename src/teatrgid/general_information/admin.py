from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from teatrgid.general_information.models import City, ListCity, Genres, ListGenres, \
                                                AgeRestrictions, ListAgeRestrictions, UserProfile


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


class AgeRestrictionsAdmin(SingleModelAdmin):
    inlines = [
        ListAgeRestrictionsAdmin,
    ]


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Дополнительная информация'


class CustomUserAdmin(UserAdmin):
    inlines = [
        UserInline,
    ]


admin.site.register(City, CityAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(AgeRestrictions, AgeRestrictionsAdmin)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
