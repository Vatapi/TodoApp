from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm , BookForm
from django import forms
from .models import ToDoList
from django.utils import timezone

def SignUp(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            email = userObj['email']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username , email , password)
                auth_user = authenticate(username= username , password=password)
                login(request , auth_user)
                return HttpResponseRedirect('/todos/detail')
            else:
                forms.ValidationError(message="User with same email or username exists")
    else:
        form = UserRegistrationForm()
        return render(request , 'todos/signup.html' , {'form':form})

@login_required
def ToDoCreate(request):
    if request.method == 'POST':
        form = BookForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = User.objects.get(id = request.user.id)
            instance.save()
            return redirect('/todos/detail')
    else:
        form = BookForm()
    return render(request, 'todos/todocreate.html' , {'form':form})

@login_required
def ToDoDetail(request):
    user_id = request.user.id
    todos = ToDoList.objects.filter(user = user_id).order_by('todo_date')
    return render(request , 'todos/tododetail.html' , {'object_list':todos})

@login_required
def ToDoUpdate(request , pk):
    todo_update = ToDoList.objects.get(id=pk)
    form = BookForm(request.POST , instance=todo_update)
    if form.is_valid():
        form.save()
        return redirect(to='/todos/detail')
    return render(request , 'todos/todocreate.html' , {'form':form})

@login_required
def ToDoDelete(request , pk):
    todo_delete = get_object_or_404(ToDoList , pk=pk)
    todo_delete.delete()
    return redirect(to='/todos/detail')
