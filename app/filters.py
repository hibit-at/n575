import django_filters
from .models import Tweet

class TweetFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='dt', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='dt', lookup_expr='lte')
    usr_contains = django_filters.CharFilter(field_name='usr', lookup_expr='icontains')
    scr_contains = django_filters.CharFilter(field_name='scr', lookup_expr='icontains')
    text_contains = django_filters.CharFilter(field_name='txt', lookup_expr='icontains')

    class Meta:
        model = Tweet
        fields = ['start_date', 'end_date', 'scr_contains', 'text_contains']
