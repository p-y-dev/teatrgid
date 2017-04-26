import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from datetime import datetime

from .geoip import GeoIp
from .thirdparty_resources.models import ThirdpartyResources
from .performances.performances import RequestsPerformances
from .general_information.models import ListCity, ListAgeRestrictions, ListGenres
from .theaters.theaters import RequestsTheaters
from .persons.persons import RequestsPersons


def home_page(request):
    current_datetime = datetime.now()
    city_obj = request.city_obj

    performances = RequestsPerformances(city_obj)
    top_today_performances = performances.get_top_today(current_datetime)

    performances = RequestsPerformances(city_obj)
    week_ahead_performances = performances.get_week_ahead(current_datetime)

    performances = RequestsPerformances(city_obj)

    persons = RequestsPersons(city_obj)

    return render(request, 'home/index.html', {
        "top_today_performances": top_today_performances,
        "week_ahead_performances": week_ahead_performances,
        "performances_affiche": performances.get_affiche(current_datetime, day_tomorrow=True),
        "performances_schedule": performances.get_schedule(current_datetime, day_tomorrow=True),
        "thirdparty_resources": ThirdpartyResources.objects.filter(city=city_obj).order_by('?').first(),
        "list_age_restrictions": ListAgeRestrictions.objects.all().order_by('age'),
        "theaters": RequestsTheaters(city_obj).request_theaters(),
        "genres": ListGenres.objects.all(),
        "actors": persons.request_actors(),
        "directors": persons.request_directors(),
    })


def select_city(request):
    return render(request, 'select_city.html', {
    })


def set_user_city(request, city_slug=None):
    city = get_object_or_404(ListCity, slug=city_slug)

    if request.user.is_authenticated():
        request.user.city = city
        request.user.save()
    else:
        geoip = GeoIp()
        geoip.add_city_to_session(request, city.name)

    return HttpResponseRedirect(reverse("home"))


def filter_performances(request):
    filter_data = json.loads(request.POST.get("filter_data"))
    city_obj = request.city_obj

    if "date" in filter_data:
        date = datetime.strptime(filter_data["date"], "%d.%m.%Y").date()
        time = datetime.now().time()
        current_datetime = datetime.combine(date, time)

        performances = RequestsPerformances(city_obj)

        html_filtered_list_performances = render_to_string('home/list-performances.html', {
            "performances_affiche": performances.get_affiche(current_datetime, day_tomorrow=False),
            "performances_schedule": performances.get_schedule(current_datetime, day_tomorrow=False),
            "current_date": current_datetime.date(),
        })

        return JsonResponse({
            "status": "success",
            "filtered_data": html_filtered_list_performances,
        })
