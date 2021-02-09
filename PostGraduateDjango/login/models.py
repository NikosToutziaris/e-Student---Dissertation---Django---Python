from django.db import models
from datetime import date
# Create your models here.

class Login(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(default=0)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    student_or_professor = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='login', null=True, on_delete=models.CASCADE,)

    class Meta:
        ordering = ('created',)