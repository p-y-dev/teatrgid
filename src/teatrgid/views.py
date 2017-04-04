from django.views.generic.base import TemplateView
from ipware.ip import get_ip
from django.contrib.gis.geoip2 import GeoIP2


class HomePage(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)

        ip = get_ip(self.request)

        context.update({
            "test_ip": ip,
        })

        return context
