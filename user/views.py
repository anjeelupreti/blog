
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login , logout
from django.contrib import messages
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


from .form import RegisterUser 



def register_user(request):
    form=RegisterUser()
    if(request.method=='POST'):
        form=RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/login')
        else:
            print (form.errors)
                
    context={
        'form':form
    }
    return render(request,'users/register.html', context)
                



def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/blog/')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context) 

