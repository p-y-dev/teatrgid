from django.contrib import admin
from teatrgid.theaters.models import Theaters


class AdminModelWithCity(admin.ModelAdmin):

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == "theaters":
                kwargs["queryset"] = Theaters.objects.filter(city=request.user.city)

        return super().formfield_for_manytomany(db_field, request, **kwargs)

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
        if not change and not request.user.is_superuser:
            obj.city = request.user.city

        super().save_model(request, obj, form, change)
