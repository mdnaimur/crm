from django.shortcuts import render,redirect
from .forms import AddRecordForm
from django.contrib import messages
from .models import Record
# Create your views here.

def home(request):
    records = Record.objects.all()
   
    return  render(request,'home.html',locals())


def add_record(request):
    forms = AddRecordForm(request.POST or None)
    
    if request.method == 'POST':
        if forms.is_valid():
            add_record = forms.save()
            messages.success(request,"Record Added.....!")
            return redirect('home')
    return render(request,'add_record.html',locals())


def customer_record(request,pk):
    customer_record = Record.objects.get(id=pk)
    return render(request,'record.html',locals())


def update_record(request,pk):
    current_record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None,instance=current_record)

    if form.is_valid():
        form.save()
        messages.success(request,"Record Has Been Updated")
        return redirect('home')
    return render(request,'update_record.html',locals())


def delete_record(request,pk):
    record = Record.objects.get(id=pk)
    if(record == None ):
        messages.info(request,"Record Not found!!")
        return render(request,'update_record.html')
    record.delete()
    messages.success(request,"Record Deleted Successfully!!")
    return redirect('home')