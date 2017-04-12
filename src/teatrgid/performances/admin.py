from django.contrib import admin
from .models import Performance


class PerformanceAdmin(admin.ModelAdmin):
    exclude = ("publication_date", )


admin.site.register(Performance, PerformanceAdmin)
