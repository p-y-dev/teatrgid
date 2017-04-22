from django.conf import settings

from ipware.ip import get_ip
from xml.etree import ElementTree
import requests

from teatrgid.general_information.models import ListCity


class GeoIp(object):

    def __init__(self):
        self.ip_address = None

    def get_city_geoip(self, request):
        if settings.DEBUG:
            self.ip_address = settings.TEST_IP
        else:
            self.ip_address = get_ip(request)

        name_city_user_db = self._get_city_name_in_db()

        if name_city_user_db:
            return name_city_user_db

    def add_city_to_session(self, request, cty_name):
        request.session[settings.KEY_CITY_SESSION] = cty_name
        return request.session[settings.KEY_CITY_SESSION]

    def _get_city_name_in_db(self):
        if self.ip_address is None:
            return None

        response = requests.get(settings.URL_IPGEOBASE + self.ip_address)

        if response.status_code != 200:
            return None

        ip_answer = ElementTree.fromstring(response.content)

        try:
            self.name_city = ip_answer.find('ip').find('city').text
        except AttributeError:
            return None

        city_user = ListCity.objects.filter(name=self.name_city)

        if city_user:
            return city_user.get().name
        else:
            return None
