from django.shortcuts import render
from speakeasy.config import pagination
from django.db.models import Q
from .models import User,requests
from .forms import InfoForm
from django.http import HttpResponseRedirect

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
    else:
        #if no query return users with 'a' in name
        results = User.objects.filter(Q(username__icontains="a"))

    pages=pagination(request,results,num=10)
    context={'items':pages[0],
    'page_range': pages[1],
    'query': query,
     }
    return render (request,template,context)


def update_account(request):

    if request.method=='POST' and request.user.is_authenticated:

        #create new instance of form
        form= InfoForm(request.POST, instance=request.user.profile)

        if form.is_valid():

                #save user profile
                form.save()

                #redirect to profile
                return HttpResponseRedirect('/profile/')
    else:
        if request.user.is_authenticated:
            #if its not a post method create a new info form
            form= InfoForm(instance=request.user.profile)
            #this is to access form variable from view
            context= {'form': form}
            #return the html file to user with rendered form as context
            return render(request,'main/update.html',context)
        else:
            return HttpResponseRedirect('/accounts/login')


def friend_request(request):
    other_user=request.POST.get("oth_user")
    current_user = request.user.id
    if other_user != current_user:
        new_request=requests()
        new_request.sender=current_user
        new_request.receiver=User.objects.get(id=other_user)
        new_request.accepted=False
        new_request.save()
        return HttpResponseRedirect('/profile/')

def show_requests(request):
    #get all results of current user
    current_user = request.user.id
    friend_req= 2
