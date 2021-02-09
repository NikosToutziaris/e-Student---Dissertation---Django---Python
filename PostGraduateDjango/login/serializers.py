from django.contrib.auth.models import User
from rest_framework import serializers
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from PostGraduateDjango.login.models import Login
#from PostgraduateDjango.list_of_classes.models import List_of_classes
from django.contrib.auth.models import User
from django.http import HttpResponse


class LoginSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(allow_blank=False, write_only=True)

    class Meta:
      model = Login
      fields = ['created', 'user_id', 'username', 'password', 'fullname', 'student_or_professor', 'owner']