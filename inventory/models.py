# models.py
from django.db import models

class Component(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    repair_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.model} ({self.vin})"


class Issue(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name="issues", on_delete=models.CASCADE)
    description = models.TextField()
    component_choice = models.CharField(max_length=10, choices=[('new', 'New Components'), ('repair', 'Repair Services')])
    component = models.ForeignKey(Component, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Issue for {self.vehicle.vin}: {self.description}"

