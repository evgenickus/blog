from django.db import models

class User(models.Model):
  username = models.CharField(max_length=150)
  first_name = models.CharField(max_length=150)
  last_name = models.CharField(max_length=150)
  email = models.EmailField(max_length=200)
  password = models.CharField(max_length=200)