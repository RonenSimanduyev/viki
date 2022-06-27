from unicodedata import category
from django.shortcuts import redirect, render
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .models import Category, Entry

# Create your views here.
def all(request):
    categories = Category.objects.all()
    return render(request,'vikiclone/all.html',{"categories":categories})

def search(request):
    q =  request.GET['q'] if request.GET.get('q') != None else ''
    entries = Entry.objects.filter(
        Q(name__icontains=q)
    )
    return render(request,'vikiclone/search.html',{"entries":entries})

@login_required(login_url='login')
def add(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        category = Category.objects.get(id=request.POST['category'])
        Entry.objects.create(
            name = request.POST['name'],
            imageUrl = request.POST['imageUrl'],
            body = request.POST['body'],
            category = category
        )
        return redirect('home')
    return render(request,'vikiclone/entry-add.html',{"categories":categories})

@login_required(login_url='login')
def edit(request,id):
    entry = Entry.objects.get(id=id)
    categories = Category.objects.all()
    if request.method == 'POST':
        category = Category.objects.get(id=request.POST['category'])
        entry.name = request.POST['name']
        entry.imageUrl = request.POST['imageUrl']
        entry.body = request.POST['body']
        entry.category = category
        entry.save()
        return redirect('one', entry.id)
    return render(request,'vikiclone/entry-edit.html',{"entry":entry,"categories":categories})

def one(request,id):
    entry = Entry.objects.get(id=id)
    return render(request,'vikiclone/entry-one.html',{"entry":entry})

@login_required(login_url='login')
def remove(request,id):
    entry = Entry.objects.get(id=id)
    if request.method == 'POST':
        entry.delete()
        return redirect('home')
    return render(request,'vikiclone/entry-remove.html',{"entry":entry})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            return render(request,'vikiclone/login.html',{"error":"user does not exist"})

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'vikiclone/login.html',{"error":"username or password incorrect"}) 

    return render(request,'vikiclone/login.html',{})

def logout_user(request):
    logout(request)
    return redirect('home')