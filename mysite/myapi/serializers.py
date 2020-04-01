from rest_framework import serializers
from .models import Application

class ApplicationSerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'key')