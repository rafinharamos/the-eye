from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from events.tasks import create_event

from events.api.v1.serializers import EventSerializer
from events.models import Event


class EventView(APIView):
    """
    post:
    Create a new event instance.
    """

    serializer_class = EventSerializer

    def post(self, request, *args, **kwargs):
        create_event.delay(request.data)
        return Response('Event will be created')


class EventListView(ListAPIView):
    """
    Get a list of events
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filter_fields = ['session_id', 'category', 'timestamp']
