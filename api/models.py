from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=64)
    pages = models.PositiveSmallIntegerField(default=1)
