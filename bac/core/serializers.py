from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import *

class ClientSerializer(serializers.HyperlinkedModelSerializer):
  password = serializers.CharField(style={'input_type': 'password'})
  class Meta:
    model = Client
    fields = ('id', 'name', 'description', 'address', 'password')
