from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=100)
    age=models.IntegerField()
    SID=models.IntegerField(primary_key=True)