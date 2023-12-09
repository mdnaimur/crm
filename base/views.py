from django.shortcuts import render,redirect
from .forms import AddRecordForm
from django.contrib import messages
# Create your views here.

def home(request):
   
    return  render(request,'home.html')


def add_record(request):
    forms = AddRecordForm(request.POST or None)
    
    if request.method == 'POST':
        if forms.is_valid():
            add_record = forms.save()
            messages.success(request,"Record Added.....!")
            return redirect('home')
    return render(request,'add_record.html',locals())