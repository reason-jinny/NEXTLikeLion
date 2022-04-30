from django.db import models

# Create your models here.

# class Person(models.Model):
#     name = models.CharField(max_length=10)
#     address = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(null=True, max_length=100)
    content = models.TextField()
    date = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.title
