from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

# Create your views here.

@login_required
def profile(request): 
    get_profile =get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=get_profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=get_profile)
        if form.is_valid():
            form.save()

    return render(request,'Profile/profile.html',context={
        'profile':get_profile,
        'form':form
    })