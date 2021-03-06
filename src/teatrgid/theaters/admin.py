from django.contrib import admin
from .models import Theaters
from ..admin import AdminSortModelWithCity


class TheatersAdmin(AdminSortModelWithCity):
    exclude = "publication_date",

    list_display = "name", "city",


admin.site.register(Theaters, TheatersAdmin)
