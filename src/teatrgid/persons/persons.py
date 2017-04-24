from .models import Actors, Directors


class RequestsPersons(object):
    def __init__(self, city_obj):
        self.requests = None
        self.city_user = city_obj

    def request_actors(self):
        self.requests = Actors.objects.filter(
            city=self.city_user,
        ).order_by("name")

        return self.requests

    def request_directors(self):
        self.requests = Directors.objects.filter(
            city=self.city_user,
        ).order_by("name")

        return self.requests
