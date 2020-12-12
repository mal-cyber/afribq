from django.db import models

# Create your models here.
from random import randint
from time import sleep
# Create your models here.
class main_amirs(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField(max_length=15)
class members(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(max_length=15)
class premiers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField(max_length=15)
    reg_no = models.IntegerField(max_length=10)
class ran(models.Model):
    #while True:
        #sleep(600)
        #range = 10**(3)
        #rangee = (10**4)-1
        #x = randint(range,rangee)
    #id_num = x
    id_num = models.CharField(max_length=4)
