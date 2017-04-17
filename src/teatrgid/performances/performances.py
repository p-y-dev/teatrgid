from django.db.models import Q

from .models import Performance
from datetime import datetime


class PerfrmancesObjs(object):
    def __init__(self, request):
        self.q_performance = None
        self.city_user = request.city_obj
        self.request_current_performance(datetime.now())

    def request_current_performance(self, date_time):
        self.q_performance = Performance.objects.filter(
            Q(city=self.city_user) and \
            Q(datesevent__date_time__gte=date_time)
        )

        return self.q_performance

    def get_distinct(self):
        return self.q_performance.distinct("name")

    def get_sorted_date_time(self):
        return self.q_performance.order_by("datesevent__date_time")
