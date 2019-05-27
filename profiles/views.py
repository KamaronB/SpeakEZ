from django.shortcuts import render
from speakeasy.config import pagination
from django.db.models import Q
from .models import User


# Create your views here.

def pro(request):
    return render(request, 'main/pro.html',{})


def search_user(request):
    ##Template for the main page
    template = 'main/post_list.html'
    # Query by user
    query = request.GET.get("q")
    if query:
        #results of query from Users table to database
        results= User.objects.filter(
        Q(username__icontains=query)|
        Q(last_name__icontains=query)|
        Q(first_name__icontains=query)
        ).distinct()
        pages=pagination(request,results,num=10)


        context={'items':pages[0],
        'page_range': pages[1],
        'query': query,
        }
        return render (request,template,context)
