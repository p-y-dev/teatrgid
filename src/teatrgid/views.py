from django.views.generic.base import TemplateView
from .performances.performances import RequestsPerformances


class HomePage(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)

        performances = RequestsPerformances(self.request)

        context.update({
            "performances_affiche": performances.get_distinct(),
            "performances_schedule": performances.get_sorted_date_time(),
        })

        return context
