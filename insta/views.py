# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from .forms import CreateUserForm
from .email import send_welcome_email
from django.contrib import messages
from django .contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def index(request):
    items = Profile.objects.all()
    context = {
        'items': items
    }

    return render(request, 'insta/index.html',context)


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            send_welcome_email(name, email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'registration/index.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        LoginView(request, user)

        # Redirect to a success page.
        return render(request, 'registration/login.html')
    else:
        # Return an 'invalid login' error message.
        return ("Please sign up first to login")

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    # Redirect to a success page.
    return redirect('/')
def user_detail(request):
    form = CreateUserForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user;
            obj.save()
            form = CreateUserForm()
            messages.success(request, "Successfully created")
            send_welcome_email(name='name',email='email')


    return render(request, 'insta/form.html', {'form': form})

class AccountList(ListView):
    model = Profile
    template_name = 'insta/account_list.html'
    context_object_name = 'profile'
    
    def get_queryset(self):
        profile_list = Profile.objects.filter(owner=self.request.user)
        print(profile_list)
        return profile_list


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AccountList, self).dispatch(*args, **kwargs)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })
@login_required
def user_profile(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile,
    }
    print()
    return render(request, 'insta/profile_list.html',context)