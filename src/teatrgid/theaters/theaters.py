from .models import Theaters


class RequestsTheaters(object):
    def __init__(self, city_obj):
        self.requests = None
        self.city_user = city_obj

    def request_theaters(self):
        self.requests = Theaters.objects.filter(
            city=self.city_user,
        ).order_by("name")

        return self.requests
