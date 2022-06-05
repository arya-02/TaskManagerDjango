from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    task = models.Tasks.objects.all()
    return render(request,'home.html',{'task' : task})


def AddTask(request):
    return render(request,'add.html')


def AddedTask(request):
    cont = request.POST['contents']
    newtask = models.Tasks(content = cont)
    newtask.save()
    return redirect('/')

def Getupdate(request,id):
    task = models.Tasks.objects.get(id=id)
    return render(request,'update.html',{'task':task})


def Updating(request,id):
    cont = request.POST['contents']
    task = models.Tasks.objects.get(id=id)
    task.content = cont
    task.save()
    return redirect('/')

def deleteTask(request,id):
    task = models.Tasks.objects.get(id=id)
    task.delete()
    return redirect('/')