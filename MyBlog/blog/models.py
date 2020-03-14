from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  User
from django.urls import reverse



class post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_Posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail' , kwargs={'pk' : self.pk})
