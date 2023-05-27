from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=256)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=256, blank=True)
    phone = models.CharField(max_length=256, blank=True)
    email = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name


class Warranty(models.Model):
    option = [
        ('Year', 'YEAR'),
        ('Month', 'MONTH'),
    ]
    value = models.IntegerField(default=0)
    time = models.CharField(max_length=6, choices=option, default='YEAR')

    def __str__(self):
        return str(self.value) +' ' + self.time


class Discount(models.Model):
    name = models.CharField(max_length=256, default='Regular')
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name + ' - ' + str(self.value)


class Product(models.Model):
    category = models.ManyToManyField(Category)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete = models.CASCADE)
    warranty = models.ForeignKey(Warranty, on_delete = models.SET_NULL, null = True)
    discount = models.ForeignKey(Discount, on_delete = models.SET_NULL, null = True)

    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default=None, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name