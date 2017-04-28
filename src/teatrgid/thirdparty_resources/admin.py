from django import forms
from django.contrib import admin

from .models import ThirdpartyResources, Advertising
from ..admin import AdminModelWithCity


class ThirdpartyResourcesForm(forms.ModelForm):
    model = ThirdpartyResources
    fields = "__all__"


class CurrentAdmin(AdminModelWithCity):
    exclude = "",
    list_display = "name", "city",
    form = ThirdpartyResourcesForm


class ThirdpartyResourcesAdmin(CurrentAdmin):
    pass


class AdvertisingAdmin(CurrentAdmin):
    pass

admin.site.register(ThirdpartyResources, ThirdpartyResourcesAdmin)
admin.site.register(Advertising, AdvertisingAdmin)
