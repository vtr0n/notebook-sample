from django.db import models


class Notebook(models.Model):
    """Notebook model"""
    message = models.CharField(max_length=512, default='')
