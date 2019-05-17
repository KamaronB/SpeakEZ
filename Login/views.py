from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


def main(request):
    #return the root html file
    return render(request,'main.html',{})

def register(request):
    ##if the method is post
    if request.method == "POST":
        #send input data to form variable
        form=UserCreationForm(request.POST)
        #if form input is valid
        if form.is_valid():
            #save the information
            form.save()
            #save username from form in variable
            username= form.cleaned_data['username']
            #save password from form in variable
            password= form.cleaned_data['password1']
            #create a User variable
            user = authenticate(username=username,password=password)
            #Login the referenced user
            login(request,user)
            #redirect to main page
            return HttpResponseRedirect('/')
    else:
        #if its not a post method create a new registration form
        form = UserCreationForm()
        #this is to access form variable from view
        context= {'form': form}
        #return the html file to user with rendered form as context
        return render(request,'registration/register.html',context)

def about(request):
    return render(request,'about.html',{})
