from .models import Record
from django import forms

class AddRecordForm(forms.ModelForm):
    # first_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}),label="")
    # last_name =forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}),label="")
    # email = forms.EmailField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Email...", "class":"form-control"}),label="")
    # phone = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number", "class":"form-control"}),label="")
    # division = forms.Select(required=True,widget=forms.widgets.Select(attrs={"placeholder":"Division", "class":"form-control"}),label="")
    # city =  forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"City ","class":"form-control"}),label="")
    # state =  forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"State ","class":"form-control"}),label="")
    # zipcode = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}),label="")


    class Meta:
        model = Record
        # fields ='__all__'
        fields =['first_name','last_name','email','phone','division','city','state','zipcode']
        widgets ={
            'first_name':forms.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}),
            'last_name':forms.TextInput(attrs={"placeholder":"Lastt Name", "class":"form-control"}),
            'email':forms.EmailInput(attrs={"placeholder":"Email", "class":"form-control"}),
            'phone':forms.TextInput(attrs={"placeholder":"Phone ","class":"form-control"}),
            'division':forms.Select(attrs={"placeholder":"Division","class":"form-control"}),
            'city':forms.Select(attrs={"placeholder":"City","class":"form-control"}),
            'state':forms.TextInput(attrs={"placeholder":"State", "class":"form-control"}),
            'zipcode':forms.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}),
        }
       