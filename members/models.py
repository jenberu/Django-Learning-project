from django.db import models
class Member(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=100)

# Create your models here.
