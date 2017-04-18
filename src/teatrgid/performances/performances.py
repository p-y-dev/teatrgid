from .models import Performance
from datetime import timedelta


class RequestsPerformances(object):
    def __init__(self, city_obj):
        self.q_performance = None
        self.last_q = None
        self.city_user = city_obj

    def display_name(self):
        names = ""
        for performance in self.last_q:
            names += performance.name + ", "

        return names

    def request_current_performance_date_gte(self, date_time):
        self.q_performance = Performance.objects.filter(
            city=self.city_user,
            datesevent__date_time__gte=date_time
        )

        return self.q_performance

    def request_performance_today(self, date_time):
        self.q_performance = Performance.objects.filter(
            city=self.city_user,
            datesevent__date_time__gte=date_time,
            datesevent__date_time__lte=date_time.replace(hour=23, minute=59)
        )

        return self.q_performance

    def get_top_today(self):
        self.last_q = self.q_performance.filter(top_today=True)
        return self.last_q

    def get_distinct(self):
        self.last_q = self.q_performance.distinct("name")
        return self.last_q

    def get_sorted_date_time(self):
        self.last_q = self.q_performance.order_by("datesevent__date_time")
        return self.last_q
