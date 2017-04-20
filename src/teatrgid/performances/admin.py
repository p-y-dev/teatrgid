from django import forms
from django.contrib import admin
from datetime import datetime

from .models import Performance, PerformanceGallery, DatesEvent
from .performances import RequestsPerformances
from ..admin import AdminModelWithCity, ModelForm


class PerformanceGalleryInline(admin.TabularInline):
    model = PerformanceGallery


class DatesEventInline(admin.TabularInline):
    model = DatesEvent


class PerformanceAdminForm(ModelForm):
    def current_performance_in_top(self, performances, name_current_performances):
        is_top = False

        for top_today_performance in performances:
            if name_current_performances == top_today_performance.name:
                is_top = True
                return is_top

        return is_top

    def clean_top(self):
        NOT = "not"
        TODAY = "today"
        SOON = "soon"

        top = self.cleaned_data['top']

        if top == NOT:
            return top

        performances = RequestsPerformances(self.request.user.city)
        parameter_distinct = "name"
        name_current_performances = self.cleaned_data['name']

        if top == TODAY:
            performances.request_performance_today(datetime.now())
            performances.get_distinct(parameter_distinct)

            if performances.requests.count() >= 3:

                if self.current_performance_in_top(performances.requests, name_current_performances):
                    return top

                raise forms.ValidationError(
                    "В 'топ сегодня' могут быть максимум 3 спектакля. " + \
                    "Сейчас в топе следующие спектакли (" + performances.display_name() + ")"
                )

        return top


class PerformanceAdmin(AdminModelWithCity):
    exclude = "publication_date", "reviews",

    form = PerformanceAdminForm

    list_display = "name", "city",

    inlines = [
        PerformanceGalleryInline,
        DatesEventInline
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj=obj, **kwargs)
        form.request = request
        return form

admin.site.register(Performance, PerformanceAdmin)
