from django.contrib.auth.models import User
from django.db import models


class Device(models.Model):
    name = models.CharField('Name', max_length=100)
    model = models.CharField('Model', max_length=100)
    desc = models.TextField('Description')
    price = models.CharField('Price', max_length=50)
    image = models.ImageField('Image', null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    count = models.PositiveIntegerField('Count')
