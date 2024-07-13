from django.db import models


class Request(models.Model):
    query = models.TextField()
