from django import forms
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from teatrgid.forms import TinyMCEInput
from teatrgid.theaters.models import Theaters
from teatrgid.persons.models import Actors, Directors

from .models import GeneralModel


class ModelForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCEInput, required=True, label="Контент")

    class Meta:
        model = GeneralModel
        fields = "__all__"


class AdminModelWithCity(admin.ModelAdmin):

    form = ModelForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "theater":
            kwargs["queryset"] = Theaters.objects.filter(city=request.user.city)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == "actors":
                kwargs["queryset"] = Actors.objects.filter(city=request.user.city)
            elif db_field.name == "directors":
                kwargs["queryset"] = Directors.objects.filter(city=request.user.city)

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


class AdminSortModelWithCity(SortableAdminMixin, AdminModelWithCity):
    pass
