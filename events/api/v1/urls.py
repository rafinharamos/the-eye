from django.urls import path
from events.api.v1.views import EventView, EventListView

app_name = 'event'

urlpatterns = [
    path('', EventView.as_view(), name='event'),
    path('list', EventListView.as_view(), name='list-event')
]