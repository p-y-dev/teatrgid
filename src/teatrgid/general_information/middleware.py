from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse, resolve

from teatrgid.geoip import GeoIp

from teatrgid.general_information.models import ListCity


class CityMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        url_name = resolve(request.path_info).url_name
        if url_name == "select_city" or url_name == "set_user_city":
            return self.get_response(request)

        admin_url = "/admin"
        if request.path[:len(admin_url)] == admin_url:
            return self.get_response(request)

        if request.user.is_authenticated():
            is_authenticated = True

        else:
            is_authenticated = False

        if is_authenticated:
            try:
                name_city_user = request.user.city.name

            except AttributeError:
                name_city_user = None
        else:
            name_city_user = request.session.get(settings.KEY_CITY_SESSION)

            if name_city_user is None:
                print("GEOIPPIPIPIPIPIPIPIPIP")
                geoip = GeoIp()
                name_city_user = geoip.get_city_geoip(request)
                geoip.add_city_to_session(request, name_city_user)

        if name_city_user is None:
            return HttpResponseRedirect(reverse("select_city"))

        else:
            city = ListCity.objects.filter(name=name_city_user).get()
            request.city_obj = city

        return self.get_response(request)
