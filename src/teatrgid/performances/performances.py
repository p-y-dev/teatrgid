from .models import Performance, DatesEvent
from datetime import timedelta


class RequestsPerformances(object):
    def __init__(self, city_obj):
        self.requests = None
        self.city_user = city_obj

    def display_name(self):
        names = ""
        for performance in self.requests:
            names += performance.name + ", "

        return names

    def request_performance_current_day_tomorrow(self, date_time):
        self.requests = Performance.objects.filter(
            city=self.city_user,
            datesevent__date_time__gte=date_time,
            datesevent__date_time__lte=date_time.replace(hour=23, minute=59) + timedelta(days=1)
        )

        return self.requests

    def request_dates_event_current_day_tomorrow(self, date_time):
        self.requests = DatesEvent.objects.filter(
            performance__city=self.city_user,
            date_time__gte=date_time,
            date_time__lte=date_time.replace(hour=23, minute=59) + timedelta(days=1)
        ).order_by("date_time")

        return self.requests

    def request_performance_today(self, date_time):
        self.requests = Performance.objects.filter(
            city=self.city_user,
            datesevent__date_time__gte=date_time,
            datesevent__date_time__lte=date_time.replace(hour=23, minute=59)
        )

        return self.requests

    def get_distinct(self, parameter_distinct):
        self.requests = self.requests.distinct(parameter_distinct)
        return self.requests
