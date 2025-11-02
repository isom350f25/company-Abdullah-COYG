from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    joined_on = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=8)
    joined_on = models.DateField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}.{self.name} - {self.position}"


# Create your models here.
