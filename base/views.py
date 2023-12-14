from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import AddRecordForm
from .forms import CustomUserCreationForm
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
   
    return  render(request,'home.html',locals())

#loging
def login_user(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        #Authenticate
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have been logged in')
            return redirect('home')
        else:
            messages.warning(request,'Username or Password does not match')
            return render(request,'login.html')
            
    return render(request,'login.html')

#Logout User
def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')   

#Registraion
def register_user(request):
    if request.method=='POST':
       form = CustomUserCreationForm(request.POST)
       if form.is_valid():
           form.save()

           #Authenticate and login
           username = form.cleaned_data['username']
           password = form.cleaned_data['password1']
           user = authenticate(request,username=username,password=password)
           login(request,user)
           messages.success(request,'You have successfully restringraion. Welcome')
           return redirect('home')
    
    else:
        form = CustomUserCreationForm()
        return render(request,'register.html',locals())

    return render(request,'register.html',locals())


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