from .models import Performance
from datetime import datetime


class RequestsPerformances(object):
    def __init__(self, request):
        self.q_performance = None
        self.city_user = request.city_obj
        self.request_current_performance_date_gte(datetime.now())

    def request_current_performance_date_gte(self, date_time):
        self.q_performance = Performance.objects.filter(
            city=self.city_user,
            datesevent__date_time__gte=date_time
        )

        return self.q_performance

    def get_distinct(self):
        return self.q_performance.distinct("name")

    def get_sorted_date_time(self):
        return self.q_performance.order_by("datesevent__date_time")
