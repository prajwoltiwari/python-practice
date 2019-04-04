from django.db import models

# Create your models here.

class Product(models.Model):
    name        = models.CharField(max_length=80)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    summary     = models.TextField(blank=False, null=False)
    verified    = models.BooleanField(default=False)

    def  __str__(self):
        return self.name
