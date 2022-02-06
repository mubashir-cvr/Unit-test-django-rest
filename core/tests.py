from django.test import TestCase

from rest_framework.test import APIClient
from django.urls import reverse
from .models import Person
import datetime
from .serializers import PersonSerializer

from rest_framework import status

PERSON_URL = reverse('core:person-list') ## API URL



class PrivatePersonApiTests(TestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.client = APIClient() ## API CLIENT by Django TO TEST

    def test_retrieve_person(self):  ## Method for testing retrive (GET Operation)
        """Test retrieving tags"""
        Person.objects.create(
            checked=True,
            name='Test Name',
            type='Test Type',
            age=23,
            description='Test Disc',
            date=datetime.datetime.now()
            )  ## Creating Test PERSON

        res = self.client.get(PERSON_URL) ## Taking Data through API URL

        persons = Person.objects.all().order_by('-name')  ## Collecting Data from Person Model to Validate with res(Data Retrived through API Client) 
        serializer = PersonSerializer(persons, many=True) ## Serielize The data 
        self.assertEqual(res.status_code, status.HTTP_200_OK)  ## Check API is Worked 
        self.assertEqual(res.data, serializer.data) ## Check Datas are same 

   

    def test_create_person_successful(self): # Test For Create Person
        payload = {'checked':True,'name': 'Simple','type':'Type1','age':23,'description':'description1','date':datetime.datetime.now()} ## Payload Data
        self.client.post(PERSON_URL, payload) ## Call Post MEthod

        exists = Person.objects.filter(
            name=payload['name']
        ).exists()
        self.assertTrue(exists)  ## Check data is Posted And Exist 

  


