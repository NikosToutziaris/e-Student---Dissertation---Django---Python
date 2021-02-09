from django.contrib.auth.models import User
from rest_framework import serializers
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from PostGraduateDjango.show_student_attendances.models import Show_student_attendances
from PostGraduateDjango.login.models import Login
#from PostgraduateDjango.login.serializers import Login
from PostGraduateDjango.list_of_classes.models import List_of_classes
#from PostgraduateDjango.list_of_classes.serializers import List_of_classes
from django.contrib.auth.models import User
from django.http import HttpResponse

class Show_student_attendancesSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('user_id', 'class_id', 'date', ' present_or_not_present')