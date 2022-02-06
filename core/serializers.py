from rest_framework import serializers
from .models import Person




class PersonSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Person
        fields='__all__'