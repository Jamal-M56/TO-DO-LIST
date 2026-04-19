from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Profile.models import Profile
from task.models import *
from task.forms import *

# Create your views here.
@login_required
def display(request):
    
    return render(request,'core/display.html',context={
        'tasks':Task.objects.all().filter( user = request.user ),
        'profile':get_object_or_404(Profile, user=request.user)
        })

@login_required
def dashboard(request):
    data = {'completed':Task.objects.filter(user=request.user,status='completed'),
            'in_progress':Task.objects.filter(user=request.user,status='in_progress'),            
            'pending':Task.objects.filter(user=request.user,status='pending'),            
            'delayed':Task.objects.filter(user=request.user,status='delayed'),
            'completed_count':Task.objects.filter(user=request.user,status='completed').count(),
            'in_progress_count':Task.objects.filter(user=request.user,status='in_progress').count(),
            'pending_count':Task.objects.filter(user=request.user,status='pending').count(),
            'delayed_count':Task.objects.filter(user=request.user,status='delayed').count(),


            #get profile for avatar
            'profile':get_object_or_404(Profile, user=request.user)

            }


    return render(request,'core/dashboard.html',data)



@login_required
def update_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        new_status = request.POST.get("status")
        task.status = new_status
        task.save()
        

    return render(request,'core/display.html',context={
        'tasks':Task.objects.all().filter( user = request.user ),

        })


