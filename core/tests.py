from django.test import TestCase

from rest_framework.test import APIClient
from django.urls import reverse
from .models import Person
import datetime
from .serializers import PersonSerializer

from rest_framework import status

PERSON_URL = reverse('core:person-list')


class PrivatePersonApiTests(TestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_person(self):
        """Test retrieving tags"""
        Person.objects.create(
            checked=True,
            name='Test Name',
            type='Test Type',
            age=23,
            description='Test Disc',
            date=datetime.datetime.now()
            )

        res = self.client.get(PERSON_URL)

        tags = Person.objects.all().order_by('-name')
        serializer = PersonSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

   