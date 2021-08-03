from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )
    tag = models.ManyToManyField(Tag)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.TextField(max_length=1000, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    Product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.status

