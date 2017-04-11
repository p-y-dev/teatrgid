from django.conf import settings
from teatrgid.geoip import GeoIp


class CityMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated():
            GeoIp(request)
            request.name_city_user = request.session[settings.KEY_CITY_SESSION]

        else:
            try:
                request.name_city_user = request.user.city.name
            except AttributeError:
                request.name_city_user = None

        response = self.get_response(request)
        return response
