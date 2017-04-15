from django.contrib import admin
from .models import Actors
from ..admin import AdminSortModelWithCity


class ActorsAdmin(AdminSortModelWithCity):
    exclude = "publication_date",

    list_display = "name", "city",


admin.site.register(Actors, ActorsAdmin)