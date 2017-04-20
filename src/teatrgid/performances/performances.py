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

    def request_performance_today(self, date_time):
        self.requests = Performance.objects.filter(
            city=self.city_user,
            datesevent__date_time__gte=date_time,
            datesevent__date_time__lte=date_time.replace(hour=23, minute=59)
        )

        return self.requests

    def request_dates_event_current_day_tomorrow(self, date_time):
        self.requests = DatesEvent.objects.filter(
            performance__city=self.city_user,
            date_time__gte=date_time,
            date_time__lte=date_time.replace(hour=23, minute=59) + timedelta(days=1)
        ).order_by("date_time")

        return self.requests

    def request_dates_event_current_today(self, date_time):
        self.requests = DatesEvent.objects.filter(
            performance__city=self.city_user,
            date_time__gte=date_time,
            date_time__lte=date_time.replace(hour=23, minute=59)
        ).order_by("date_time")

        return self.requests

    def request_week_ahead(self, date_time):
        self.requests = Performance.objects.filter(
            city=self.city_user,
            datesevent__date_time__gte=date_time.replace(hour=00, minute=00) + timedelta(days=1),
            datesevent__date_time__lte=date_time.replace(hour=23, minute=59) + timedelta(days=8)
        )

        return self.requests

    def get_distinct(self, parameter_distinct):
        self.requests = self.requests.distinct(parameter_distinct)
        return self.requests

    def get_affiche(self, current_datetime, day_tomorrow=False):
        if day_tomorrow:
            self.requests = self.request_performance_current_day_tomorrow(current_datetime)
        else:
            self.requests = self.request_performance_today(current_datetime)

        return self.requests.distinct("name")

    def get_schedule(self, current_datetime, day_tomorrow=False):
        if day_tomorrow:
            return self.request_dates_event_current_day_tomorrow(current_datetime)

        return self.request_dates_event_current_today(current_datetime)

    def get_top_today(self, date_time):
        self.requests = self.request_performance_today(date_time)
        self.requests = self.requests.filter(top="today")
        return self.requests.distinct("name")

    def get_week_ahead(self, date_time):
        self.requests = self.request_week_ahead(date_time)
        self.requests = self.requests.filter(top="soon")
        return self.requests.distinct("name")
