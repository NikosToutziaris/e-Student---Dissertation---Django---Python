from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from PostGraduateDjango.save_class_attendances.serializers import Save_class_attendancesSerializer
from PostGraduateDjango.save_class_attendances.models import Save_class_attendances
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
from PostGraduateDjango.login.permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = Save_class_attendancesSerializer

@api_view(['GET', 'POST'])
def save_class_attendances_list(request):
    # List a ll logins, or create a new login.
    if request.method == 'GET':
        save_class_attendanceses = Save_class_attendances.objects.all()
        serializer = Save_class_attendancesSerializer
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Save_class_attendancesSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def save_class_attendances_datail(request, pk):
    save_class_attendances = get_object_or_404(Save_class_attendances, pk=pk)
    return render(request, 'blog/login_detail.html', {'login': save_class_attendances})

class save_class_attendances_list(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = Save_class_attendancesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class save_class_attendances_detail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = Save_class_attendancesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
