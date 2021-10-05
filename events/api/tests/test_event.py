from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from events.models import Session, Event


class EventTests(APITestCase):
    def setUp(self):
        session = Session.objects.create(id='6f1e1a94-aa38-4152-a452-b8c45255abec')
        self.event = Event.objects.create(
            session=session,
            category='page setup',
            name='page setup',
            data={
                'host': 'www.consumeraffairs.com',
                'path': '/',
            },
            timestamp=timezone.now()
        )

    def test_create_event(self):
        data = {
            "session": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "form interaction",
            "name": "submit",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/",
                "form": {
                    "first_name": "John",
                    "last_name": "Doe"
                }
            },
            "timestamp": "2021-01-01 09:15:27.243860"
        }
        response = self.client.post("/events/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 'Event will be created')

    def test_create_event_invalid_data(self):
        data = {
            "name": "submit",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/",
                "form": {
                    "first_name": "John",
                    "last_name": "Doe"
                }
            },
            "timestamp": "2021-01-01 09:15:27.243860"
        }
        response = self.client.post("/events/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 'Event will be created')

    def test_create_event_empty_data(self):
        data = {
            'session': {'id': 'e2085be5-9137-4e4e-80b5-f1ffddc25423'},
            'category': 'page interaction',
            'name': 'cta click',
            'data': {},
            'timestamp': "2021-01-01 09:15:27.243860"
        }
        response = self.client.post("/events/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 'Event will be created')

    def test_list_event(self):
        response = self.client.get("/events/list")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data[0]['session']), self.event.session.id)
        self.assertEqual(response.data[0]['name'], self.event.name)
