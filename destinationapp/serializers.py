
from rest_framework import serializers

from .models import Destination


class Destinationserializer(serializers.ModelSerializer):
    Images = serializers.ImageField(required = False)
    class Meta:
        model = Destination
        fields ='__all__'