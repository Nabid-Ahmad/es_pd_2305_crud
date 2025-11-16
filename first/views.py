from django.shortcuts import render, redirect
from .models import Human
from django.db.models import Q
import os


def first_func(request):


    return render(request, 'new.html', locals())


def delete_data(request, id):
   
    return redirect('/')


def update_data(request, id):
    
    return render(request, 'update.html', locals())


def new():
    pass
