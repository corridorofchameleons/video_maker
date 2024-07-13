from django.db import models


class Requests(models.Model):
    query = models.TextField()
