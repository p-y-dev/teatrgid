from django.contrib import admin
from .models import Performance


class PerformanceAdmin(admin.ModelAdmin):
    exclude = "publication_date",

    list_display = "name", "city",

    def get_exclude(self, request, obj=None):
        exclude = super().get_exclude(request, obj)

        if not request.user.is_superuser:
            exclude += "city",

        return exclude

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(city=request.user.city)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.city = request.user.city

        super().save_model(request, obj, form, change)

admin.site.register(Performance, PerformanceAdmin)
