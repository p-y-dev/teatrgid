from django import forms
from django.contrib import admin

from .models import ThirdpartyResources
from ..admin import AdminModelWithCity


class ThirdpartyResourcesForm(forms.ModelForm):
    model = ThirdpartyResources
    fields = "__all__"


class ThirdpartyResourcesAdmin(AdminModelWithCity):
    exclude = "",
    list_display = "name", "city",
    form = ThirdpartyResourcesForm

admin.site.register(ThirdpartyResources, ThirdpartyResourcesAdmin)