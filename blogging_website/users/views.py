from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  
from django.contrib.auth import login, logout

def register(request): # i have created this function to be used for registering the user
    if request.method == 'POST': # if the request method is post
        form = UserCreationForm(request.POST) # then the form will be the UserCreationForm
        if form.is_valid():     # if the form is valid
            user = form.save() # then the user will be saved
            login(request, user) # and the user will be logged in
            return redirect('home') # and the user will be redirected to the home page
    else:
        form = UserCreationForm() # if the request method is not post then the form will be the UserCreationForm
    return render(request, 'register.html', {'form': form}) # and the user will be rendered to the register.html page

def user_login(request): # i have created this function to be used for logging in the user
    if request.method == 'POST': # if the request method is post
        form = AuthenticationForm(data=request.POST) # then the form will be the AuthenticationForm
        if form.is_valid(): # if the form is valid
            user = form.get_user() # then the user will be the form.get_user
            login(request, user) # and the user will be logged in
            return redirect('home') # and the user will be redirected to the home page
    else: 
        form = AuthenticationForm() # if the request method is not post then the form will be the AuthenticationForm
    return render(request, 'login.html', {'form': form}) # and the user will be rendered to the login.html page

@login_required # this decorator is used to ensure that the user is logged in before they can log out
def user_logout(request): # i have created this function to be used for logging out the user
    logout(request) # this will log out the user
    return redirect('home') # and the user will be redirected to the home page