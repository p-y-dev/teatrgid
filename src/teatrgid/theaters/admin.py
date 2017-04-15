from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Theaters
from ..admin import AdminModelWithCity


class TheatersAdmin(SortableAdminMixin, AdminModelWithCity):
    exclude = "publication_date",

    list_display = "name", "city",


admin.site.register(Theaters, TheatersAdmin)
