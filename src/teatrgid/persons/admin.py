from django.contrib import admin
from .models import Actors, Directors
from ..admin import AdminSortModelWithCity


class PersonAdmin(AdminSortModelWithCity):
    exclude = "publication_date",

    list_display = "name", "city",


class ActorsAdmin(PersonAdmin):
    pass


class DirectorsAdmin(PersonAdmin):
    pass


admin.site.register(Actors, ActorsAdmin)
admin.site.register(Directors, DirectorsAdmin)