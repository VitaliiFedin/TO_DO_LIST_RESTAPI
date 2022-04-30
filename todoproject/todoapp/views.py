from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework import serializers
from rest_framework import status
from datetime import datetime
from django.views.generic import ListView
from django.utils import timezone


@api_view(['GET'])
def TaskOverview(request):
    api_urls = {
        'All tasks': '/all',
        'Single task': '/task/pk',
        'Create': '/create',
        'Update': '/update/pk',
        'Delete': '/task/delete/pk',
        'Overdue': 'task/overdue/'
    }
    deadline_check = Task.objects.filter(deadline__lte=timezone.now()).exclude(status='Done').update(status='Overdue')


    return Response(api_urls)


@api_view(['POST'])
def add_tasks(request):
    task = TaskSerializer(data=request.data)

    if Task.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if task.is_valid():
        task.save()
        return Response(task.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_tasks(request):
    # serializer = TaskSerializer(tasks,many=True)
    if request.query_params:
        tasks = Task.objects.filter(**request.query_param.dict())
    else:
        # tasks = Task.objects.all().order_by("-task_priority")
        tasks = Task.objects.all().order_by("-status", 'task_priority')

        # tasks = Task.objects.all().filter(status='Overdue',task_priority=%d)

    if tasks:
        # data = TaskSerializer(tasks)
        return Response(TaskSerializer(tasks, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    data = TaskSerializer(task, data=request.data, partial=True)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_tasks(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def view_task(request, pk):
    tasks = Task.objects.get(pk=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def overdue_tasks(request):
    # serializer = TaskSerializer(tasks,many=True)
    if request.query_params:
        tasks = Task.objects.filter(**request.query_param.dict())
    else:
        tasks = Task.objects.all().filter(status='Overdue').order_by('task_priority')
    if tasks:
        # data = TaskSerializer(tasks)
        return Response(TaskSerializer(tasks, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
