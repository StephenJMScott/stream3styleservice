from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm, PersonalForm
from django.contrib.auth.decorators import login_required

def get_index(request):
    return render(request, 'index.html')
    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('home')
    
def login(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        
        
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username_or_email'],
                                     password=form.cleaned_data['password'])
            
            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                
                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(profile)
                
            else:
                form.add_error(None, "Your Username or Password was not recognised")
            
            
    else:
        form = UserLoginForm()
        
        
    return render(request, "login.html", {'form': form})

def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        personalform= PersonalForm()
        
        if form.is_valid() and personalform.is_valid():
            form.save()
            personalform.save()
            
            
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password1'])
                                     
            if user is not None:
                auth.login(request, user)
                return redirect('profile.html')
    else:
        form = UserRegistrationForm()
        personalform= PersonalForm()

    
    return render(request, "register.html", {'form':form, 'personalform':form})
 
@login_required() 
def profile(request):
     return render(request, 'profile.html')
