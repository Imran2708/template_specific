from django.shortcuts import render

def func(request):
    return render(request,'h1.html')

def func1(request):
    return render(request,'h2.html')