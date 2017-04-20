from django.views.generic.base import TemplateView
from .performances.performances import RequestsPerformances

from datetime import datetime


class HomePage(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)

        current_datetime = datetime.now()

        performances = RequestsPerformances(self.request.city_obj)

        performances.request_performance_current_day_tomorrow(current_datetime)

        parameter_distinct = "name"
        context.update({
            "performances_affiche": performances.get_distinct(parameter_distinct),
            "performances_schedule": performances.request_dates_event_current_day_tomorrow(current_datetime),
        })

        return context
