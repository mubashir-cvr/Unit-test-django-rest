from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from . import serializers
# Create your views here.



class PersonViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.PersonSerializer
    queryset = Person.objects.all()
