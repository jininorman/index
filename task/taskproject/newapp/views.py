from django.contrib import messages, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import NewUserForm

# Create your views here.
def register(request):
   if request.method == "POST":
       form = NewUserForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request,'Registration successfull.')
           return redirect("/")
       messages.error(request,"Unsuccessfull registration.Invalid information")
   form = NewUserForm
   return render(request,'register.html',{"register_form": form})

def login_request(request):
    if request.method == "POST":
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f'you are now logged in as {username}.')

                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")
    form=AuthenticationForm()
    return render(request,"login.html",{"login_form":form})

def logout_request(request):
    auth.logout(request)
    return redirect("/")
