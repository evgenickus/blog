from django.db import models
from users.models import User

# Create your models here.


class Article(models.Model):
  name = models.CharField(max_length=250)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

