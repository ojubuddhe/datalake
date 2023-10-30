from django.db import models

# Create your models here.
class lostdeposit(models.Model):
    stateName = models.CharField(max_length=100)
    assemblyNumber = models.IntegerField(max_length=100)
    year = models.IntegerField()
    total_Candidates = models.IntegerField()
    deposit_Lost = models.IntegerField()
