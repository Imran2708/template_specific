from django.shortcuts import render

def pp(request):
    return render(request,'h1.html')

def cc(request):
    return render(request,'h2.html')
    
