from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    message=models.CharField(max_length=150)
class Profile(models.Model):
    linkedin=models.CharField(max_length=255,blank=True,null=True)
    github=models.CharField(max_length=255,blank=True,null=True)

