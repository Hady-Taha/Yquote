from django.shortcuts import render,redirect,HttpResponse
from .models import Quote
from user.models import Profile
from .forms import AddNewQoute
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    if request.user.is_authenticated == False:
        return redirect('website')
        pass
    quotes=Quote.objects.all()
    profiles=Profile.objects.all()
    #to add Qoute
    form=AddNewQoute()
    if request.method=='POST':
        form=AddNewQoute(request.POST)
        if form.is_valid():
            newqoute=form.save(commit=False)
            newqoute.userp=Profile.objects.get(profile_user=request.user.id)
            newqoute.save()
            
    #to remove Qoute
    
        
    context={
        'title':'Home',
        'quotes':quotes,
        'profiles':profiles,
        'form':form,
    }
    return render(request,'quotes/home.html',context)


def detail(request):
    if request.user.is_authenticated == False:
        return redirect('website')
    context={
        'title':'detail'
    }
    return render(request,'quotes/detail.html',context)


def vdelete(request,id):
    if request.method=='POST':
        Quote.objects.get(id=id).delete()
        x=messages.info(request,'delete done')
        HttpResponse(x)
    return redirect('home') 
        
    


def indexWeb(request):
    if request.user.is_authenticated==True:
        return redirect('home')
    context={
        'title':'Yquoets',
    }
    return render(request,'quotes/noneLogin.html',context)