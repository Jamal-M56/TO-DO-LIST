from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        data = TaskForms(request.POST)
        if data.is_valid():
            data.save()
            return redirect('dashboard')
    return render(request,'task/create.html',context={'form':TaskForms()})



@login_required
def update(request,id):

    get_object_by_id = Task.objects.get(id=id)

    if request.method== 'POST':
        update_task = TaskForms(request.POST,instance=get_object_by_id)
        if update_task.is_valid():
            update_task.save()
    
    form = TaskForms(instance=get_object_by_id)

    return render(request,'task/update.html',context={'form':form,'name':get_object_by_id.title})

@login_required
def delete(request,id):

        
    get_object_by_id = Task.objects.get(id=id)

    if request.method == 'POST':
        get_object_by_id.delete()
        return redirect('home')

    return render(request,'task/delete.html',{'name':get_object_by_id.title})
