from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

Article.objects.create(
    title = "좋은날",
    content = "눈물이 차 올라서 고갤 들어",
)
