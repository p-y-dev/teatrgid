import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
import datetime

from .geoip import GeoIp
from .thirdparty_resources.models import ThirdpartyResources
from .performances.performances import RequestsPerformances
from .general_information.models import ListCity, ListAgeRestrictions, ListGenres
from .theaters.theaters import RequestsTheaters
from .persons.persons import RequestsPersons


def home_page(request):
    current_datetime = datetime.datetime.now()
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

    performances_affiche = RequestsPerformances(city_obj)
    performances_schedule = RequestsPerformances(city_obj)

    context_data = {}

    if "date" in filter_data:
        date = datetime.datetime.strptime(filter_data["date"], "%d.%m.%Y").date()
        time = datetime.datetime.now().time()

        if date == datetime.datetime.now().date():
            current_datetime = datetime.datetime.combine(date, time)

        else:
            current_datetime = datetime.datetime.combine(date, datetime.time(0, 0, 0))

        performances_affiche.get_affiche(current_datetime, day_tomorrow=False)
        performances_schedule.get_schedule(current_datetime, day_tomorrow=False)
        context_data["current_date"] = current_datetime.date()
    else:
        current_datetime = datetime.datetime.now()
        performances_affiche.get_affiche(current_datetime, day_tomorrow=True)
        performances_schedule.get_schedule(current_datetime, day_tomorrow=True)

    if "rating" in filter_data:
        performances_affiche.filter_affiche_bay_rating(filter_data["rating"])
        performances_schedule.filter_schedule_bay_rating(filter_data["rating"])

    if "age_from" in filter_data:
        performances_affiche.filter_affiche_bay_age_from(filter_data["age_from"])
        performances_schedule.filter_schedule_bay_age_from(filter_data["age_from"])

    if "age_to" in filter_data:
        performances_affiche.filter_affiche_bay_age_to(filter_data["age_to"])
        performances_schedule.filter_schedule_bay_age_to(filter_data["age_to"])

    if "theaters" in filter_data:
        performances_affiche.filter_affiche_bay_theaters(filter_data["theaters"])
        performances_schedule.filter_schedule_bay_theaters(filter_data["theaters"])

    if "genres" in filter_data:
        performances_affiche.filter_affiche_bay_genres(filter_data["genres"])
        performances_schedule.filter_schedule_bay_genres(filter_data["genres"])

    if "actors" in filter_data:
        performances_affiche.filter_affiche_bay_actors(filter_data["actors"])
        performances_schedule.filter_schedule_bay_actors(filter_data["actors"])

    if "directors" in filter_data:
        performances_affiche.filter_affiche_bay_directors(filter_data["directors"])
        performances_schedule.filter_schedule_bay_directors(filter_data["directors"])

    context_data["performances_affiche"] = performances_affiche.requests.distinct("name")
    context_data["performances_schedule"] = performances_schedule.requests
    html_filtered_list_performances = render_to_string(
        'home/list-performances.html',
        context_data
    )

    return JsonResponse({
        "status": "success",
        "filtered_data": html_filtered_list_performances,
    })
