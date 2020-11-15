from django import forms
from django.contrib.auth.models import User
from .models import Profile
# Create your forms here.

class CreateNewUser(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','password','password2')
    

    username=forms.CharField(
        max_length=25,
        min_length=4,
        required=True,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'user name'}
            )
        )

    email=forms.EmailField(required=True,widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'email'}
        )
    )

    password=forms.CharField(
        min_length=8, 
        required=True,
        widget=forms.PasswordInput(
            attrs={'type':'password','class':'form-control','placeholder':'password'}
            )
        )


    password2=forms.CharField(
        min_length=8, 
        required=True,
        widget=forms.PasswordInput(
            attrs={'type':'password','class':'form-control','placeholder':'confirm password'}
            )
        )

 

    




    def clean(self):
        cd=self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password not match')


        if User.objects.filter(username=cd['username']):
            raise forms.ValidationError('username already exists')


        if User.objects.filter(email=cd['email']):
            raise forms.ValidationError('email already exists') 





class NewLogin(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password')
    
    
    username=forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'user name'}
            )
        )

    password=forms.CharField( 
        required=True,
        widget=forms.PasswordInput(
            attrs={'type':'password','class':'form-control','placeholder':'password'}
            )
        )


    
class updateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('profile_img','bio')

    
    bio=forms.CharField(
        widget=forms.TextInput(
            
            attrs={'class':'form-control','placeholder':'bio'}
            ),required=False
        )
    
    pass


class updateUser(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name',)

    first_name=forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'name','id':'FormControlname'}
            )
        )
    pass