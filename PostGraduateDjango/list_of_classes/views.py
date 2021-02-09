from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from PostGraduateDjango.list_of_classes.serializers import List_of_classesSerializer
from PostGraduateDjango.list_of_classes.models import List_of_classes
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
from PostGraduateDjango.list_of_classes.permissions import IsOwnerOrReadOnly
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = List_of_classesSerializer

@api_view(['GET', 'POST'])
def list_of_classes_list(request):
    # List a ll logins, or create a new login.
    if request.method == 'GET':
        logins = List_of_classes.objects.all()
        serializer = List_of_classesSerializer
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = List_of_classesSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def list_of_classes_detail (request, pk):
    #Retrieve, update or delete a snippet instance.
    try:
        list_of_classes = List_of_classes.objects.get(pk=pk)
    except List_of_classes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = List_of_classesSerializer(list_of_classes)
        return Response(serializer)

    elif request.method == 'PUT':
        serializer = List_of_classesSerializer(list_of_classes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        list_of_classes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def list_of_classes_list(request):
    cat = request.GET.get('cat', '')
    try:
        cat = int(cat)
    except:
        cat = False
    if(cat == False):
        list_of_classeses = List_of_classes.objects.filter(created=timezone.now()).order_by('created')
    else:
        list_of_classeses = List_of_classes.objects.filter(created=timezone.now()).filter(category=cat).order_by('created')
        data = serializers.serialize('json', list_of_classeses)
        return HttpResponse(data, content_type='application/json')

def list_of_classes_detail(request, pk):
    list_of_classes = get_object_or_404(List_of_classes, pk=pk)
    return render(request, 'blog/list_of_classes_detail.html', {'list_of_classes': list_of_classes})

class list_of_classes_list(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = List_of_classesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class list_of_classes_detail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = List_of_classesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)