from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from PostGraduateDjango.show_student_attendances.serializers import Show_student_attendancesSerializer
from PostGraduateDjango.show_student_attendances.models import Show_student_attendances
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from PostGraduateDjango.show_student_attendances.permissions import IsOwnerOrReadOnly
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = Show_student_attendancesSerializer

@api_view(['GET', 'POST'])
def show_student_attendances_list(request):
    # List all show student attendances, or create a new show student attendances.
    if request.method == 'GET':
        show_student_attendanceses = Show_student_attendances.objects.all()
        serializer = Show_student_attendancesSerializer
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Show_student_attendancesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def show_student_attendances_detail (request, pk):
    #Retrieve, update or delete a show student attendances instance.
    try:
        show_student_attendances = Show_student_attendances.objects.get(pk=pk)
    except Show_student_attendances.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Show_student_attendancesSerializer(show_student_attendances)
        return Response(serializer)

    elif request.method == 'PUT':
        serializer = Show_student_attendancesSerializer(show_student_attendances, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        show_student_attendances.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class show_student_attendances_list(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = Show_student_attendancesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class show_student_attendances_detail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = Show_student_attendancesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

