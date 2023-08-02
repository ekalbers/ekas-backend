from django.db import models
from django.urls import reverse


class InfoRequest(models.Model):
    name = models.CharField(max_length=32, default='None')
    company = models.CharField(max_length=32, default='None')
    email = models.CharField(max_length=32, default='None')
    phone = models.CharField(max_length=16, default='None', blank=True)
    message = models.TextField(default='None', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.company}'
