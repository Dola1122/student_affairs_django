from django.db import models

# Create your models here.



####################  Ahmed Adel Start  ####################


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

