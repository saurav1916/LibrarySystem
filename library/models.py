from django.db import models

# Create your models here.
class lib(models.Model):
    Book_name=models.CharField(max_length=100)
    Author_name=models.CharField(max_length=120)
