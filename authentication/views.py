
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate

from todo.views import home
# Create your views here.
def usersignup(req):
    if req.method == "GET":
        return render(req,'signup.html',{'form':UserCreationForm()})
    else:
        #print(req.POST['username'],req.POST['password1'],req.POST['password2'])
        if req.POST['password1'] == req.POST['password2']:
            try:
                user = User.objects.create_user(req.POST['username'],password = req.POST['password1'])
                user.save()
                login(req,user)
                return redirect('home')
                
            except IntegrityError:
                return render(req,'signup.html',{'form':UserCreationForm(),'UserExistsError':"UserName Already Exists"})

        else:
            return render(req,'signup.html',{'form':UserCreationForm(),'error':"Password Does't Match"})

def userlogin(req):
    if req.method == 'GET':
        return render(req,'login.html',{'form':AuthenticationForm()})
    else:
         user = authenticate(username = req.POST["username"],password = req.POST["password"],)
         if user == None:
            return render(req,'login.html',{'form':AuthenticationForm(),'error':"Username and Password Doesn't Match"})
         else:
            login(req,user)
            return redirect('home')


def userlogout(req):
    logout(req)
    return redirect('userlogin')


