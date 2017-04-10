from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.generic.base import TemplateView

from teatrgid.geoip import GeoIp


class GeoIpView(TemplateView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            geo_obj = GeoIp(request)

            if geo_obj.city_name_user is None:
                return HttpResponseRedirect('https://www.google.ru/')

            geo_obj.add_name_city_in_session(request)

        return super(GeoIpView, self).get(self, request, args, kwargs)

    def get_context_data(self, **kwargs):
        context = super(GeoIpView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            city_user = self.request.user.city.name
        else:
            city_user = self.request.session[settings.KEY_CITY_SESSION]

        context.update({
            "city_user": city_user,
        })

        return context


class HomePage(GeoIpView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)

        context.update({
            "test_ip": "dwa",
        })

        return context
