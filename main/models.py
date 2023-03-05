from django.db import models

# Create your models here.

class Users(models.Model):
    name=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    medical_history=models.TextField(null=True)
    age=models.IntegerField()
    weight=models.IntegerField()
    blood_grp=models.CharField(max_length=50)
    email_id=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mob_no=models.CharField(max_length=50)
    offer=models.CharField(max_length=50) 
    date=models.DateField()  
    password=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name
