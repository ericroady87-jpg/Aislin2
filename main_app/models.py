from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

FuelTypes = (
    ('N', 'Nuclear'),
    ('P', 'Propellant'),
    ('G', 'GN particles'),
)

class Weapons(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('weapon-detail', kwargs={'pk': self.id})

# Create your models here.
class MobileSuit(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    weapons = models.ManyToManyField(Weapons)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('mobile-suit-detail', kwargs={'pk': self.id})

class Fueling(models.Model):
    date = models.DateField("Fueling Date")
    fuel = models.DecimalField(max_digits=10, decimal_places=2)

    mobile_suit = models.ForeignKey(MobileSuit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fuel} gallons on {self.date}"
    
    class Meta:
        ordering = ['-date']