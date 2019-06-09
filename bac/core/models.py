from django.db import models
from django.utils.crypto import get_random_string

class Client(models.Model):
  id          = models.AutoField(primary_key=True)
  name        = models.CharField(max_length=64)
  description = models.CharField(max_length=64)
  address     = models.CharField(max_length=64)
  password    = models.CharField(max_length=255)
