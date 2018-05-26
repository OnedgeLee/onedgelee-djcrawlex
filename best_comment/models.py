from django.db import models

# Create your models here.

class Article(models.Model):
    article_href = models.URLField()
    article_title = models.CharField(max_length=100)
    article_writer = models.CharField(max_length=64)
    article_comment = models.TextField()
    article_upvote = models.IntegerField()
    article_downvote = models.IntegerField()
    article_crawldate = models.DateTimeField(auto_now_add=True)