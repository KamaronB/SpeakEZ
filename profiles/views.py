from django.shortcuts import render

# Create your views here.

def pro(request):
    return render(request, 'main/pro.html',{})
