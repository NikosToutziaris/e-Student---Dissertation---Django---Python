from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from PostGraduateDjango.login.serializers import LoginSerializer#, List_of_classesSerializer, Show_student_attendancesSerializer
from PostGraduateDjango.login.models import Login
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
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = LoginSerializer

@api_view(['GET', 'POST'])
def login_list(request):
    # List a ll logins, or create a new login.
    if request.method == 'GET':
        logins = Login.objects.all()
        serializer = LoginSerializer
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoginSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def login_detail (request, pk):
    #Retrieve, update or delete a login instance.
    try:
        login = Login.objects.get(pk=pk)
    except Login.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoginSerializer(login)
        return Response(serializer)

    elif request.method == 'PUT':
        serializer = LoginSerializer(login, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        login.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def login_list(request):
    cat = request.GET.get('cat', '')
    try:
        cat = int(cat)
    except:
        cat = False
    if(cat == False):
        logins = Login.objects.filter(created=timezone.now()).order_by('created')
    else:
        logins = Login.objects.filter(created=timezone.now()).filter(category=cat).order_by('created')
        data = serializers.serialize('json', logins)
        return HttpResponse(data, content_type='application/json')

def login_detail(request, pk):
    login = get_object_or_404(Login, pk=pk)
    return render(request, 'blog/login_detail.html', {'login': login})

class login_list(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    erializer_class = LoginSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class login_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
