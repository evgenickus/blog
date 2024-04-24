from django.db import models

# Create your models here.

class User(models.Model):
  username = models.CharField(max_length=150)
  first_name = models.CharField(max_length=150)
  last_name = models.CharField(max_length=150)
  email = models.EmailField(max_length=200)
  password = models.CharField(max_length=200)

class Article(models.Model):
  name = models.CharField(max_length=250)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
  text = models.TextField()
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

