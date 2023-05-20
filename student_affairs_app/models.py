from django.db import models

# Create your models here.



####################  Ahmed Adel Start  ####################

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    IDnum = models.CharField(max_length=9)
    birthDate = models.DateField()
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    level = models.PositiveIntegerField()
    dep = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return self.name


####################  Ahmed Adel End    ####################




####################  Mohamed Elmanori Start  ####################


####################  Mohamed Elmanori End    ####################




####################  John Start  ####################
class Admin(models.Model):
    #id = models.AutoField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=128)
    gender = models.CharField(max_length=10)

####################  John End    ####################




####################  Ahmed Younes Start  ####################


####################  Ahmed Younes End    ####################




####################  Sahar Start  ####################


####################  Sahar End    ####################

