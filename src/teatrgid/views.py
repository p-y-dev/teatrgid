from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView


class SearchCity(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.name_city_user is None:
            return HttpResponseRedirect('http://convertonlinefree.com/WordToPDFRU.aspx')

        return super(SearchCity, self).get(self, request, args, kwargs)


class HomePage(SearchCity):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)

        context.update({
        })

        return context
