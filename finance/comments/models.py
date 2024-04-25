from django.db import models
from users.models import User
from articles.models import Article

# Create your models here.


class Comment(models.Model):
  text = models.TextField()
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

