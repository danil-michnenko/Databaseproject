from django.db import models

# Create your models here.
class Payment(models.Model):
    username = models.CharField(max_length = 255)
    amount_money = models.IntegerField(default = 0)
    comment = models.CharField(max_length = 255, blank = True, null = True) 