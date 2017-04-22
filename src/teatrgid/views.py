from django.shortcuts import render
from datetime import datetime

from .thirdparty_resources.models import ThirdpartyResources
from .performances.performances import RequestsPerformances
from .general_information.models import ListCity


def home_page(request):
    current_datetime = datetime.now()

    performances = RequestsPerformances(request.city_obj)
    top_today_performances = performances.get_top_today(current_datetime)

    performances = RequestsPerformances(request.city_obj)
    week_ahead_performances = performances.get_week_ahead(current_datetime)

    performances = RequestsPerformances(request.city_obj)
    performances_affiche = performances.get_affiche(current_datetime, day_tomorrow=True)
    performances_schedule = performances.get_schedule(current_datetime, day_tomorrow=True)

    thirdparty_resources = ThirdpartyResources.objects.filter(city=request.city_obj).order_by('?').first()

    return render(request, 'home/index.html', {
        "top_today_performances": top_today_performances,
        "week_ahead_performances": week_ahead_performances,
        "performances_affiche": performances_affiche,
        "performances_schedule": performances_schedule,
        "thirdparty_resources": thirdparty_resources,
    })


def select_city(request):
    list_city = ListCity.objects.all().order_by("name")

    return render(request, 'select_city.html', {
        "list_city": list_city,
    })
