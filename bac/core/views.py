from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from core.serializers import *

class ClientViewSet(viewsets.ModelViewSet):
  queryset = Client.objects.all()
  serializer_class = ClientSerializer
