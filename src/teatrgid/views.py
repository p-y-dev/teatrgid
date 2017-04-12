from django.views.generic.base import TemplateView


class HomePage(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)

        print(self.request.city_obj.name)
        print(self.request.city_obj.slug)

        context.update({
        })

        return context
