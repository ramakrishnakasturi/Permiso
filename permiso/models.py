from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    username=models.EmailField(max_length = 254)
    password=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    phno=models.BigIntegerField(default=9347804746)
    img=models.ImageField(upload_to='pics')
class Lecturer(models.Model):
    name=models.CharField(max_length=100)
    username=models.EmailField(max_length = 254)
    password=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics',)
    phno=models.BigIntegerField(default=9347804746)
    verify=models.BooleanField(default=False)
class Permission(models.Model):
    stu=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    req=models.TextField()
    img=models.ImageField(upload_to='pics')
    grant=models.CharField(max_length=100,default="Not seen")


    