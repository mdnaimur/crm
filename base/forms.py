from typing import Any
from .models import Record
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Sing Up form with customazition
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
    last_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your last name'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='User Name'
        self.fields['username'].label=''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	



class AddRecordForm(forms.ModelForm):

    class Meta:
        model = Record
        # fields ='__all__'
        fields =['first_name','last_name','email','phone','division','city','state','zipcode']
        widgets ={
            'first_name':forms.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}),
            'last_name':forms.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}),
            'email':forms.EmailInput(attrs={"placeholder":"Email", "class":"form-control"}),
            'phone':forms.TextInput(attrs={"placeholder":"Phone ","class":"form-control"}),
            'division':forms.Select(attrs={"placeholder":"Division","class":"form-control"}),
            'city':forms.Select(attrs={"placeholder":"City","class":"form-control"}),
            'state':forms.TextInput(attrs={"placeholder":"State", "class":"form-control"}),
            'zipcode':forms.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}),
        }
       