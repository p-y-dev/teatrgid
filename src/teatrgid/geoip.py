from django.conf import settings

from ipware.ip import get_ip
from xml.etree import ElementTree
import requests

from teatrgid.general_information.models import ListCity


class GeoIp(object):

    def __init__(self, request):
        self.city_name_user = None
        self.name_city = None

        if settings.DEBUG:
            self.ip_address = settings.TEST_IP
        else:
            self.ip_address = get_ip(request)

        if self.ip_address is not None:
            response = requests.get(settings.URL_IPGEOBASE + self.ip_address)
            if response.status_code == 200:
                ip_answer = ElementTree.fromstring(response.content)
                try:
                    self.name_city = ip_answer.find('ip').find('city').text
                except AttributeError:
                    self.name_city = None

                city_user = ListCity.objects.filter(name=self.name_city)

                if city_user:
                    self.city_name_user = city_user.get().name

    def add_name_city_in_session(self, request):
        city_name_session = request.session.get(settings.KEY_CITY_SESSION)

        if not city_name_session or city_name_session != self.city_name_user:
            request.session[settings.KEY_CITY_SESSION] = self.city_name_user
