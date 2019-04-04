from django.db import models
from django.urls import reverse

# Create your models here.

class Neo(models.Model):
    name        = models.CharField(max_length=80)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        # return f'{self.id}'
        return reverse('neo_create_id', kwargs={'my_id': self.id})
