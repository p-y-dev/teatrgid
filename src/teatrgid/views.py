import random
from django.views.generic.base import TemplateView
from .performances.performances import RequestsPerformances

from datetime import datetime

from .thirdparty_resources.models import ThirdpartyResources


class HomePage(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)

        current_datetime = datetime.now()

        performances = RequestsPerformances(self.request.city_obj)
        top_today_performances = performances.get_top_today(current_datetime)

        performances = RequestsPerformances(self.request.city_obj)
        week_ahead_performances = performances.get_week_ahead(current_datetime)

        performances = RequestsPerformances(self.request.city_obj)
        performances_affiche = performances.get_affiche(current_datetime, day_tomorrow=True)
        performances_schedule = performances.get_schedule(current_datetime, day_tomorrow=True)

        thirdparty_resources = ThirdpartyResources.objects.filter(city=self.request.city_obj).order_by('?').first()

        print(thirdparty_resources)

        context.update({
            "top_today_performances": top_today_performances,
            "week_ahead_performances": week_ahead_performances,
            "performances_affiche": performances_affiche,
            "performances_schedule": performances_schedule,
            "thirdparty_resources": thirdparty_resources
        })

        return context
