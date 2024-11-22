from django.db import models
from datetime import timedelta
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=150)
    deadline = models.DateTimeField()

    @property
    def is_overdue(self):
        """
        dynamically check if the task is overdue
        """
        return self.deadline < timezone.now()
    
    @property 
    def remaining_time(self):
        """
        calculate remaining time until deadline
        """
        return self.deadline - timezone.now()
    

class Product(models.Model):
    name = models.CharField(max_length=150)
    is_available = models.BooleanField(default=False)

    @classmethod
    def available_products(cls):
        """
        return all available products
        """
        return cls.objects.filter(is_available=True)
    #how to access it:
    """
    from model_decorators.models import Product
    products = Product.available_products()
    print([obj.name for obj in products])
    """

class Order(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)

    @staticmethod
    def calculate_discount(amount, discount_rate):
        """
        calculate the discount for a given amount
        """
        return amount * (discount_rate/100)

    
    
from django.utils.functional import cached_property

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    @cached_property
    def word_count(self):
        """
        Calculate and cache the word count of the content.
        """
        return len(self.content.split())

# Usage:
# article = Article.objects.get(id=1)
# print(article.word_count)  # Calculates once and caches

