from django.shortcuts import render,redirect
from speakeasy.config import pagination
from django.db.models import Q
from django.urls import reverse,reverse_lazy
from .models import User,requests,Relationship,People,Room,Message
from .forms import InfoForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from django.utils.safestring import mark_safe
import json

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

    if request.user.is_authenticated:
        if request.method=='POST':
            #create new instance of form
            form= InfoForm(request.POST, instance=request.user.profile)

            if form.is_valid():
                    print("made it here")
                    #save user profile

                    form.save()
                    print("made it here")
                    #redirect to profile
                    return HttpResponseRedirect('/profile/')
            else:
                print(form.errors)
                return HttpResponse("form not valid")
        else:

            #if its not a post method create a new info form
            form= InfoForm(instance=request.user.profile)
            #this is to access form variable from view
            context= {'form': form}
            #return the html file to user with rendered form as context
            return render(request,'main/update.html',context)
    else:
            return HttpResponseRedirect('/accounts/login')



def friend_request(request):
    #get the user you want to send a request to from the post method
    other_user=request.POST.get("oth_user")
    #get the current user making the request
    current_user = request.user.id

    #if they aren't the same person save the data in database and redirect to profile
    if other_user != current_user:
        new_request=requests()
        new_request.sender=current_user
        new_request.receiver=User.objects.get(id=other_user)
        new_request.accepted=False
        new_request.save()
        return HttpResponseRedirect('/profile/')


def show_requests(request):
    #set the template
    template='main/requests.html'
    #Set friend name empty
    friend_name=None
    #get the user making the request
    current_user =request.user

    #if there is a request filter all requests down to the current user
    friend_req= requests.objects.filter(receiver=current_user.id,accepted=False)
    #loop through the requests and find senders name based off of ID
    #set names equal to friend names
    if friend_req:
        for f in friend_req:
            friend_name= User.objects.filter(id=f.sender)

    #if there are friends show the friends and paginate
    if friend_name != None:
        pages=pagination(request,friend_name,num=10)
        #find = lambda a: User.objects.get(id=a)
        context={'items':pages[0],
        'page_range': pages[1],
         }
        return render (request,template,context)
    #if there are no friends return only the template
    else:
        return render(request,template,{})


def accept_request(request):
        #get the user you want to send a request to from the post method
        other_user=request.POST.get("oth_user")
        #get the current user making the request
        current_user = request.user.id
        friend_requests = requests.objects.get(sender=other_user,receiver=current_user)
        #if they aren't the same person save the data in database and redirect to profile
        if friend_requests:
            friend_requests.accepted=True
            friend_requests.save()
            return HttpResponseRedirect('/profile/requests/')



def show_friends(request):

            template='main/chat.html'
            #get the current user
            current_user= request.user
            #get the users relationships
            relationship = Relationship.objects.get(profile=current_user.profile)
            #find the people in the relationship
            peeps = People.objects.get(rel_id=relationship)
            #match the people to the user
            friends=User.objects.filter(id=peeps.friend_id)


            if friends:
                pages=pagination(request,friends,num=10)
                context={'items':pages[0],
                'page_range': pages[1],
                 }
                return render (request,template,context)
            #if there are no friends return only the template
            else:
                return render(request,template,{})




def create_chat_room(request):
    #Get the current user & the User we want to send messages to #
    user1= request.user
    user2=request.POST.get("oth_user")

    # If the room with the given users doesn't exist, automatically create it
    # upon first visit
    room = Room.objects.get(user_1__in=[user1.id,user2],user_2__in=[user1.id,user2])
    if Room.objects.filter(room_name=room.room_name).exists():
        #render existing room
        return redirect(reverse_lazy('profiles:chat_room',  kwargs={'room_name': room.room_name}))
    else:
        new_room = Room.objects.create(user_1=user1.id,user_2=user2)
        #create new room and render it
        return redirect(reverse_lazy('profiles:chat_room',  kwargs={'room_name': new_room.room_name}))


def chat_room(request,room_name):
        room= Room.objects.get(room_name=room_name)

        if request.user.is_authenticated and room.user_1==request.user.id or room.user_2==request.user.id:

            #get the last 50 messages
            messages = reversed(room.messages.order_by('-timestamp')[:50])

            #render the room with the user objects inside of them
            current_user= request.user
            oth_user= None
            if current_user.id == room.user_1:
                oth_user= User.objects.get(id=room.user_2)
            else:
                oth_user=User.objects.get(id=room.user_1)
            return render(request, "main/room.html", {
                'room': room,
                'messages': messages,
                'user': current_user,
                'friend': oth_user
            })
        else:
            return render(request,"error/404.html",{})
