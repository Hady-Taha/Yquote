from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import CreateNewUser,NewLogin,updateProfile,updateUser
from .models import Profile
from quotes.models import Quote
from quotes.forms import AddNewQoute
from django.urls import reverse

# Create your views here.

def register(request):
    form=CreateNewUser()
    if request.method=='POST':
        form=CreateNewUser(request.POST)
        if form.is_valid():
            newuser=form.save(commit=False)
            newuser.set_password(form.cleaned_data['password'])
            newuser.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            vlogin(request,username,password)
            Profile.objects.create(profile_user=User.objects.get_by_natural_key(request.user.username))
            messages.success(request,f'welcome {username} 🎉')
            return redirect('home')
            pass
        pass
    context={
        'title':'register',
        'form':form,
    }
    return render(request,'user/register.html',context)

def vlogin(request,username=None,password=None):
    if request.user.is_authenticated == True:
       return redirect('home')
    form=NewLogin()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'password or username not correct')
            
       
    context={
        'title':'Login',
        'form':form,
    }
    return render(request,'user/Login.html',context)


def vlogout(request):
    if request.user.is_authenticated == False:
       return redirect('login')
       pass
    logout(request)
    context={
        'title':'logout',
    }
    return render(request,'user/logout.html',context)


def profile(request,id):
    if request.user.is_authenticated==False:
        return redirect('website')
    profile=get_object_or_404(Profile,profile_user=id)
    quots=Quote.objects.filter(userp=profile)
    form=AddNewQoute()
    if request.method=='POST':
        form=AddNewQoute(request.POST)
        if form.is_valid():
            newqoute=form.save(commit=False)
            newqoute.userp=Profile.objects.get(profile_user=request.user.id)
            newqoute.save()
    context={
        'title':'Profile',
        'profile':profile,
        'quots':quots,
        'form':form,
    }
    return render(request,'user/profile.html',context)



def vupdateprofile(request,id):
    if id != request.user.id:
        return redirect('home')
        pass
    profile=get_object_or_404(Profile,profile_user=id)
    profileform=updateProfile()
    userform=updateUser()
    if request.method=='POST':
        profileform=updateProfile(request.POST,request.FILES,instance=request.user.profile)
        userform=updateUser(request.POST,instance=request.user)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            messages.success(request, 'update done')
        return redirect(reverse('profile',kwargs={'id':request.user.id}))

    
    context={
        'title':'editprofile',
        'profile':profile,
        'userform':userform,
        'profileform':profileform,
    }
    return render(request,'user/editprofile.html',context)

