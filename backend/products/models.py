from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, default=99.99, decimal_places=2)


class Book(models.Model):
    title = models.CharField(max_length=240)
    author = models.CharField(max_length=150)
    publish_date = models.DateField()
    
