from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def store(request):
    context = {}
    return render(request, 'core/store.html', context)

def cart(request):
    context = {}
    return render(request, 'core/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'core/checkout.html', context)