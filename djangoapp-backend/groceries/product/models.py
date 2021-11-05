from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.


class Category(models.Model):
    category_title = models.CharField(max_length=200)
    category_description = models.CharField(max_length=200)

    def __str__(self):
        return self.category_title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=CASCADE)
    product_title = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200)

    def __str__(self):
        return self.product_title
