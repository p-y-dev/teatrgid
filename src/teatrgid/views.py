from django.views.generic.base import TemplateView
from .performances.models import Performance


class HomePage(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)

        performances = Performance.objects.filter(city=self.request.city_obj)

        context.update({
            "performances": performances,
        })

        return context
