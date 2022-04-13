from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    #.CharField는 html의 input 태그와 비슷함. 최대 길이 제한이 있음.
    content = models.TextField()
    #.TextField는 html의 text area 태그와 비슷함.

    def __str__(self):
        return self.title
