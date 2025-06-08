import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    min_date = django_filters.DateTimeFilter(field_name="sent_at", lookup_expr='gte')
    max_date = django_filters.DateTimeFilter(field_name="sent_at", lookup_expr='lte')
    sender = django_filters.CharFilter(field_name="sender__username", lookup_expr='iexact')

    class Meta:
        model = Message
        fields = ['conversation', 'sender', 'min_date', 'max_date']
