from django.db import models

# Create your models here.
class Contact(models.Model):
    fname=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phnno=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
