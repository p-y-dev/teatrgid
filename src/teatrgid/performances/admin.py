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

    def clean_top_today(self):
        top_today_state = self.cleaned_data['top_today']
        top_soon_state = self.cleaned_data['top_today']
        name_performance = self.cleaned_data['name']

        # performances = RequestsPerformances(self.request.user.city)
        # performances.request_performance_today(datetime.now())
        # performances.get_top_today()
        # count_top_today = performances.last_q.count()
        #
        # is_top = False
        # for top_today_performance in performances.last_q:
        #     if name_performance == top_today_performance.name:
        #         is_top = True
        #         break
        #
        # if is_top and top_soon_state:
        #     raise forms.ValidationError(
        #         "'топ сегодня' и 'топ скоро' не могут быть активны одновременно"
        #     )
        #
        # if count_top_today >= 3 and top_today_state:
        #     if is_top:
        #         return top_today_state
        #
        #     raise forms.ValidationError(
        #         "В 'топ сегодня' могут быть максимум 3 спектакля. " + \
        #         "Сейчас в топе следующие спектакли (" + performances.display_name() + ")"
        #     )
        #
        return top_today_state


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
