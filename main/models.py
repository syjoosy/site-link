from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    long_link = models.URLField(verbose_name="Длинная ссылка", max_length=250)
    short_link = models.CharField(verbose_name="Сокращенная ссылка", max_length=250, unique=True)

    def __str__(self):
        return self.short_link

    def get_absolute_url(self):
        return reverse('redirect-link', kwargs={'slug': self.short_link})
