from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=30, unique=True)
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="active")
    def __str__(self):
        return self.username