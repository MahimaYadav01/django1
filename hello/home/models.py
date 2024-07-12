from django.db import models


# Create your models here.
class Contact(models.Model):
    # fname=models.CharField(max_length=122)
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phnno=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name

class Signup(models.Model):
    username=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    def __str__(self):
        return self.username

