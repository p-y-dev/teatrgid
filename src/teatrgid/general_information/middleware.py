from django.conf import settings
from django.http import HttpResponseRedirect

from teatrgid.geoip import GeoIp

from teatrgid.general_information.models import ListCity


class CityMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        admin_url = "/admin"

        if request.path[:len(admin_url)] == admin_url:
            return self.get_response(request)

        if not request.user.is_authenticated():
            GeoIp(request).adding_city_to_session(request)
            name_city_user = request.session[settings.KEY_CITY_SESSION]

        else:
            try:
                name_city_user = request.user.city.name

            except AttributeError:
                name_city_user = None

        if name_city_user is None:
            return HttpResponseRedirect('http://convertonlinefree.com/WordToPDFRU.aspx')
        else:
            city = ListCity.objects.filter(name=name_city_user).get()
            request.city_obj = city

        return self.get_response(request)
