#from django.shortcuts import render
#from django.http import JsonResponse
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

#from rest_framework import permissions

from .serializers import SFTaskSerializer, SFOutwardSerializer, SFInwardSerializer, UserSerializer

from .models import SFTask, SFOutward, SFInward

#from django.contrib.auth.models import User

'''
--------------------------------------------------------------------------------------------------------------
API for SFTask
--------------------------------------------------------------------------------------------------------------
'''


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Task List': '/task-list/',
        'Task Create': '/task-create/',
        'Task Detail View': '/task-detail/<str:pk>/',
        'Task Update': '/task-update/<str:pk>/',
        'Task Delete': '/task-delete/<str:pk>/',
        'Outward List': '/outward-list/',
        'Outward Create': '/outward-create/',
        'Outward Detail View': '/outward-detail/<str:pk>/',
        'Outward Update': '/outward-update/<str:pk>/',
        'Outward Delete': '/outward-delete/<str:pk>/',
        'Inward List': '/inward-list/',
        'Inward Create': '/inward-create/',
        'Inward Detail View': '/inward-detail/<str:pk>/',
        'Inward Update': '/inward-update/<str:pk>/',
        'Inward Delete': '/inward-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    tasks = SFTask.objects.all()
    serializer = SFTaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    task = SFTask.objects.get(id=pk)
    serializer = SFTaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = SFTaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    print(serializer)
    return Response(serializer.data)


@api_view(['PUT'])
def task_update(request, pk):
    task = SFTask.objects.get(id=pk)
    serializer = SFTaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):
    task = SFTask.objects.get(id=pk)
    task.delete()

    return Response('Successfully deleted!')


'''
--------------------------------------------------------------------------------------------------------------
API for User authentication
--------------------------------------------------------------------------------------------------------------
'''


@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


'''
--------------------------------------------------------------------------------------------------------------
API for SFOutward
--------------------------------------------------------------------------------------------------------------
'''


@api_view(['GET'])
def outward_list(request):
    outwards = SFOutward.objects.all().order_by('etd').values()
    serializer = SFOutwardSerializer(outwards, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def outward_detail(request, pk):
    outward = SFOutward.objects.get(id=pk)
    serializer = SFOutwardSerializer(outward, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def outward_create(request):
    serializer = SFOutwardSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
    print(serializer.is_valid())
    return Response(serializer.data)


@api_view(['PUT'])
def outward_update(request, pk):
    outward = SFOutward.objects.get(id=pk)
    serializer = SFOutwardSerializer(instance=outward, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def outward_delete(request, pk):
    outward = SFOutward.objects.get(id=pk)
    outward.delete()

    return Response('Successfully deleted!')


'''
--------------------------------------------------------------------------------------------------------------
API for SFInward
--------------------------------------------------------------------------------------------------------------
'''


@api_view(['GET'])
def inward_list(request):
    inwards = SFInward.objects.all().order_by('eta').values()
    serializer = SFInwardSerializer(inwards, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def inward_detail(request, pk):
    inwards = SFInward.objects.get(id=pk)
    serializer = SFInwardSerializer(inwards, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def inward_create(request):
    serializer = SFInwardSerializer(data=request.data)
    #print(request.data)

    if serializer.is_valid():
        serializer.save()
    print(serializer)
    return Response(serializer.data)


@api_view(['PUT'])
def inward_update(request, pk):
    inward = SFInward.objects.get(id=pk)
    serializer = SFInwardSerializer(instance=inward, data=request.data)
    print(request.data)

    if serializer.is_valid():
        serializer.save()
    print(serializer)
    return Response(serializer.data)


@api_view(['DELETE'])
def inward_delete(request, pk):
    outward = SFInward.objects.get(id=pk)
    outward.delete()

    return Response('Successfully deleted!')