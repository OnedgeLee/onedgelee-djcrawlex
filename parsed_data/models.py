from django.db import models

# Create your models here.
class BlogData(models.Model):
    title = models.CharField(max_length=500)
    link = models.URLField()
