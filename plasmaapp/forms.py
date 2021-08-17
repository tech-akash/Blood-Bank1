from django import forms
from django.forms import fields
from .models import Accept,Donate,Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm






class SignUpform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']











class DateInput(forms.DateInput):
    input_type = 'date'
class AcceptorForm(forms.ModelForm):
    class Meta:
        model=Accept
        fields = ['name','address','phoneno','age','gender','bloodgroup','dayofaccept','status']
        widgets={
            'dayofaccept':DateInput()
        }
        
class DonatorForm(forms.ModelForm):
    class Meta:
        model=Donate
        fields=['name','address','phoneno','age','gender','bloodgroup','dayofdonate','status']
        widgets={
            'dayofdonate':DateInput()
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','address','phoneno','age','gender','bloodgroup','dayofaccept','need','status','prescription']
        widgets={
            'dayofaccept':DateInput()
        }

