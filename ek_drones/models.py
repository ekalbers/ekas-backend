from django.db import models
from django.urls import reverse


class InfoRequest(models.Model):
    name = models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.company}'
    #
    # def get_absolute_url(self):
    #     return reverse('info_request_detail', args=[str(self.id)])
