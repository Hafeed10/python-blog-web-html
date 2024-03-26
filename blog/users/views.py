from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from users.forms import UserForm

def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('web:index')
            else:
                context['error'] = True
                context['message'] = "Invalid username or password"
        else:
            context['error'] = True
            context['message'] = "Please provide both username and password"

    context['title'] = "Login"
    return render(request, 'users/login.html', context=context)


def logout(request):
    auth_logout(request)
    return redirect('web:index')
    
def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')

            # Create a new user instance
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name')
            )

            # Authenticate and login the user
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('web:index')
    else:
        form = UserForm()

    context['title'] = 'Signup'
    context['form'] = form
    return render(request, 'users/signup.html', context=context)
