from django.contrib import admin

from .models import Performance, PerformanceGallery, DatesEvent
from ..admin import AdminModelWithCity


class PerformanceGalleryInline(admin.TabularInline):
    model = PerformanceGallery


class DatesEventInline(admin.TabularInline):
    model = DatesEvent


class PerformanceAdmin(AdminModelWithCity):
    exclude = "publication_date", "reviews",

    list_display = "name", "city",

    inlines = [
        PerformanceGalleryInline,
        DatesEventInline
    ]

admin.site.register(Performance, PerformanceAdmin)
