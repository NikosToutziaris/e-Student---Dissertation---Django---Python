from django.contrib.auth.models import User
from rest_framework import serializers
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from PostGraduateDjango.save_class_attendances.models import Save_class_attendances
from django.contrib.auth.models import User
from django.http import HttpResponse
from PostGraduateDjango.login.models import Login
from PostGraduateDjango.list_of_classes.models import List_of_classes

class Save_class_attendancesSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('user_id', 'class_id', 'semester', 'date', ' present_or_not_present')