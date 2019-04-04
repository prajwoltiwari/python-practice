from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 80)
    description = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article-detail', kwargs={'id': self.id})