from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
 
# Create your views here.

def home(request):
    task = Task.objects.all()
    context = {'task':task}
    return render(request, 'tasks/home.html', context)

def createtask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'tasks/create_item.html', context)

def updatetask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'tasks/update.html', context)

def deletetask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)

def registerpage(request):
    
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            logout(request, user)
            return redirect('home')
        else: 
            messages.error(request, 'An error occurred during registration')

    context = {'form':form}
    return render(request, 'tasks/register.html', context)

def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password does not existe!')

    context = {}
    return render(request, 'tasks/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect("home")


