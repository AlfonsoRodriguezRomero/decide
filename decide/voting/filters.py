from django.contrib.admin import SimpleListFilter
from datetime import datetime

class StartedFilter(SimpleListFilter):
    title = 'started'
    parameter_name = 'started'

    def lookups(self, request, model_admin):
        return [
            ('NS', 'Not started'),
            ('S', 'Started'),
            ('R', 'Running'),
            ('F', 'Finished'),
        ]

    def queryset(self, request, queryset):
        today = datetime.now()
        print(today)
        if self.value() == 'NS':
            return queryset.filter(start_date__gte=today)
        if self.value() == 'S':
            return queryset.filter(start_date__lte=today, end_date__gte=today)
        if self.value() == 'R':
            return queryset.filter(start_date__lte=today, end_date__gte=today)
        if self.value() == 'F':
            return queryset.filter(start_date__isnull=False,end_date__lte=today)
        else:
            return queryset.all()
