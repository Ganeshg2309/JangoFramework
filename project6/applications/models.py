from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    status=models.CharField(max_length=200)
    applied_date=models.DateField()

    def __str__(self):
        return self.company