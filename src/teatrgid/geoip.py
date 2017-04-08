from django.conf import settings

from ipware.ip import get_ip
from xml.etree import ElementTree
import requests


class GeoIp(object):

    ip_address = None
    name_city = None

    def __init__(self, request):
        if settings.DEBUG:
            self.ip_address = settings.TEST_IP
        else:
            self.ip_address = get_ip(request)

        if self.ip_address is not None:
            response = requests.get("http://ipgeobase.ru:7020/geo?ip="+self.ip_address)
            if response.status_code == 200:
                ip_answer = ElementTree.fromstring(response.content)
                try:
                    self.name_city = ip_answer.find('ip').find('city').text
                except AttributeError:
                    self.name_city = None
