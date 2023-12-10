from django.db import models
from django.contrib.auth.models import User


class BankAccount(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    balance = models.IntegerField()

    def __str__(self):
        return self.name
        

