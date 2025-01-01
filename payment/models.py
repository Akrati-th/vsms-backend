from django.db import models

class Revenue(models.Model):
    date = models.DateField(auto_now_add=True)
    amount = models.FloatField()
    vehicle = models.ForeignKey('inventory.Vehicle', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}: ${self.amount}"