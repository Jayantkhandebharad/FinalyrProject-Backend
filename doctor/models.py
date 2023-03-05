from django.db import models

# Create your models here.

class doctor(models.Model):
    name=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email_id=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mob_no=models.CharField(max_length=50)
    Speciality=models.TextField(null=True)
    date=models.DateField()  
    password=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name