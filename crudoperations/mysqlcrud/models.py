from django.db import models


# Create your models here.

class Employee(models.Model):
    eid = models.CharField(max_length=32)
    ename = models.CharField(max_length=32)
    esal = models.IntegerField()

    
    # eemail = models.EmailField()
    # eimage= models.ImageField()

    class Meta:
        db_table = "employee"

'''
class User(models.Model):
    vid=models.CharField(max_length=20)
    vname=models.CharField(max_length=100)
    vsal=models.IntegerField()

    class Meta:
        db_table:"User"'''