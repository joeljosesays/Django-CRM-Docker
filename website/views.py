from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You are sucessfully logged in!')
            return redirect('home')
        else:
            messages.success(request,'There was an error')
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request,'You have been logged out.....')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and save
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username ,password=password)
            login(request,user)
            messages.success(request,f"Account successfully created for {username}")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    
def customer_records(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request,"record.html",{"customer_record":customer_record})
    else:
        messages.success(request,"You must be logged in......")
        return redirect('home')

def delete_customer_record(request,pk):
    delete_it = Record.objects.get(id=pk)
    delete_it.delete()
    messages.success(request,f'{delete_it} has been deleted from the database')
    return redirect('home')

@login_required(login_url='home')
def add_customer_record(request):
         if request.method=="POST":
             form = AddRecordForm(request.POST or None)
             if form.is_valid:
                 form.save( )
                 messages.success(request,"Record added.....")
                 return redirect ('home')
         else:
            form = AddRecordForm()
            return render(request,"add_record.html",{'form':form})

@login_required(login_url='home')
def update_customer_record(request,pk):
    update = Record.objects.get(id=pk)
    if request.method=="POST":
        form = AddRecordForm(request.POST or None, instance=update)
        if form.is_valid():
            form.save()
            messages.success(request,"Customer record updated...........")
            return redirect("home")
    else:
        form = AddRecordForm(instance=update)
        return render(request,'update_record.html',{'form':form})
        



    



