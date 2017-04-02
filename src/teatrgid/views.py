from django.views.generic.base import TemplateView


class HomePage(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)

        print(self.request.user.userprofile.city.slug)

        context.update({
            "test": "Hello World",
        })

        return context
