from django.views.generic.base import TemplateView


class HomePage(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context.update({
            "test_ip": "dwa",
        })

        return context
