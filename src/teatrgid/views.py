from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.generic.base import TemplateView

from teatrgid.geoip import GeoIp

from teatrgid.general_information.models import ListCity


class GeoIpView(TemplateView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            geo_obj = GeoIp(request)
            city_user = ListCity.objects.filter(name=geo_obj.name_city)

            if not city_user:
                return HttpResponseRedirect('https://www.google.ru/')

            city_user_name = city_user.get().name

            try:
                request.session[settings.KEY_CITY_SESSION]
            except KeyError:
                request.session[settings.KEY_CITY_SESSION] = city_user_name
                return super(GeoIpView, self).get(self, request, args, kwargs)

            if city_user_name != request.session[settings.KEY_CITY_SESSION]:
                request.session[settings.KEY_CITY_SESSION] = city_user_name

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
