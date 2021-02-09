from django.db import models
from datetime import date
from PostGraduateDjango.login.models import Login
from PostGraduateDjango.list_of_classes.models import List_of_classes
# Create your models here.

class Show_student_attendances(models.Model):
    user_id = models.ForeignKey(Login, on_delete=models.CASCADE,)
    class_id = models.ForeignKey(List_of_classes, on_delete=models.CASCADE,)
    semester = models.IntegerField(default=0)
    date = models.DateField()
    present_or_not_present = models.BooleanField(default=True)