from django.shortcuts import render
from todolist.models import Task
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from datetime import date
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core import serializers

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = Task.objects.filter(user=request.user)
    context = {
        "list_task" : data,
        "name" : "Ahmad Hanif Adisetya",
        "npm" : "2106750603",
        "last_login" : request.COOKIES["last_login"]
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def add_ajax(request):
    if request.method == "POST":
        title = request.POST.get("title")
        deskripsi = request.POST.get("description")
        task = Task.objects.create(title=title,description=deskripsi,user=request.user)
        data = {
            "fields":{
                "title":task.title,
                "date":task.date,
                "description":task.description,
                "status":task.is_finished,
            },
            "pk":task.pk
        }
        return JsonResponse(data)

def delete_ajax(request, id):
    if request.method == "DELETE":
        task = Task.objects.get(pk=id)
        task.delete()
        data = {
            "fields":{
                "title":task.title,
                "date":task.date,
                "description":task.description,
                "status":task.is_finished,
            },
            "pk":task.pk
        }
        return JsonResponse(data)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account is successfully made!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username or Password is incorrect!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

class TaskForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description", widget=forms.Textarea())

@login_required(login_url='/todolist/login/')
def new_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task_data = Task(
                user = request.user,
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
            )
            task_data.save()
            return redirect('todolist:show_todolist')

    context = {"form":form}
    return render(request, "new_task.html", context)

@login_required(login_url='/todolist/login/')
def is_finished_status(request, id_task):
    task = Task.objects.get(pk=id_task)
    task.is_finished = not(task.is_finished)
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def remove(request, id_task):
    Task.objects.get(pk=id_task).delete()
    return redirect('todolist:show_todolist')
