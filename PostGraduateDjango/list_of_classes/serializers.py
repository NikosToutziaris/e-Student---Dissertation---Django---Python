from django.contrib.auth.models import User
from rest_framework import serializers
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from PostGraduateDjango.list_of_classes.models import List_of_classes
from PostGraduateDjango.login.models import Login
from django.contrib.auth.models import User
from django.http import HttpResponse

class List_of_classesSerializer(serializers.ModelSerializer):

    class Meta:
        model = List_of_classes
        fields = ('class_id', 'class_name', 'semester')