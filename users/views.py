from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .froms import *

# Create your views here.

def sign_up(request):

    if request.method=='POST':
        new_user = SignUpFrom(request.POST)
        if new_user.is_valid():
            new_user.save()
            return redirect('login')
    
    form = SignUpFrom()
    return render(request,'registration\signup.html',context={'form':form})