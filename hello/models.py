from django.db import models

# Create your models here.

class User(models.Model):

    class ProfileChoices(models.TextChoices):
        STUDENT = 'ST', 'Student'
        TEACHER = 'FA', 'Faculty'
        ADMIN = 'OT', 'Other'
        STAFF = 'SF', 'Staff'
        VISITOR = 'VI', 'Visitor'

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    profile = models.CharField(
        max_length=2,
        choices=ProfileChoices.choices,
        default=ProfileChoices.STUDENT,
    )

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.profile}"
    

class lostdeposit(models.Model):
    stateName = models.CharField(max_length=100)
    assemblyNumber = models.IntegerField(max_length=100)
    year = models.IntegerField()
    total_Candidates = models.IntegerField()
    deposit_Lost = models.IntegerField()