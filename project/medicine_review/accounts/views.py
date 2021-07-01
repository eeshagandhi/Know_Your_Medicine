from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users
from display.decorators import admin_only
from .forms import userinfo
# Create your views here.
@unauthenticated_user
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        error_message=None
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("main")
        else:
            error_message="Invalid Credentials"
            return render(request,'login.html',{'error':error_message})

    else:
        return render(request,'login.html')    

@unauthenticated_user
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        #validation
        value={
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email
        }
        error_message=None
        if password1:
            if len(password1)<8:
                error_message="Password must be atleast 8 characters long"
                return render(request,'register.html',{'error':error_message,'values':value})
        if password1==password2:
            if len(first_name) < 2:
                error_message="First name is too short"
                return render(request,'register.html',{'error':error_message,'values':value})
            elif len(last_name) < 2:
                error_message="Last name is too short"
                return render(request,'register.html',{'error':error_message,'values':value})
            elif User.objects.filter(username=username).exists():
                error_message="Username taken"
                return render(request,'register.html',{'error':error_message,'values':value})
            elif User.objects.filter(email=email).exists():
                error_message="Email taken"
                return render(request,'register.html',{'error':error_message,'values':value})
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.success(request,'Your account has been created successfully')
                return redirect('login')

        else:
            error_message="Passwords don't match"
            return render(request,'register.html',{'error':error_message,'values':value})
        return render(request,'register.html',{'error':error_message,'values':value})
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')  
@login_required(login_url='login')
@admin_only
def adminsite(request):
    return render(request, 'adminsite.html')
def users(request):
    set=User.objects.all()
    context={
        "set":set,    
    }
    return render(request, 'users.html',context)
