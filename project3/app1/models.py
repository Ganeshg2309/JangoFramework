from django.db import models

# Create your models here.
class model1(models.Model):
    name=models.CharField()
    principle=models.FloatField()
    rate=models.FloatField()
    time=models.IntegerField()

