from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate , login
from django.urls import reverse 
from .forms import Signup

def index(request):
    form = Signup()
    err = ''
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if 'login' in request.POST:
            if user is not None:
                login(request, user)
                return redirect(reverse('main:main'))
            else:
                err = 'register first'
                
        elif 'createuser' in request.POST:
            if CustomUser.objects.filter(username=username).exists():
                err = 'User with this username already exists'
            else:
                err = True
                render(request, 'index.html', context={'err':err,'form':form})
        elif 'signup' in request.POST:
            form = Signup(request.POST)
            password = request.POST.get('password')
            if form.is_valid():
                firs_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                new_user = CustomUser(username=username,first_name=firs_name,last_name=last_name,password=password,email=email)
                new_user.save()
                login(request, new_user)
            return redirect(reverse('main:main'))
    
    return render(request, 'index.html', context={'err':err,'form':form })

