from django.db import models
from datetime import date, datetime


# Create your models here.

class List_of_classes(models.Model):
    class_id = models.IntegerField(default=0)
    class_name = models.CharField(max_length=50)
    semester = models.IntegerField(default=0)
