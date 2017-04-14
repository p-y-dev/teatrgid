from django.contrib import admin
from .models import Performance
from ..admin import AdminModelWithCity


class PerformanceAdmin(AdminModelWithCity):
    exclude = "publication_date",

    list_display = "name", "city",


admin.site.register(Performance, PerformanceAdmin)
