from django.shortcuts import render
from .models import Patients
from django.contrib import messages

def home(request):
    patients=Patients.objects.all()
    return render(request,'home.html',{'patients':patients})

def addUserInfo(request):
    if request.method == 'POST':
        name=request.POST['name'].strip()
        dob=request.POST['dob']
        email=request.POST['email'].strip()
        phone=request.POST['phone'].strip()

        if Patients.objects.filter(phone=phone).exists() | Patients.objects.filter(email=email).exists():
            messages.success(request,'The Phone number or Email address already exists. Please Try Again')
        else:
            Patients.objects.create(name=name,dob=dob,email=email,phone=phone)
            messages.success(request,'Patient has been registered successfully')    
    return render(request,'add.html')

def fetchUserInfo(request):
    phone=request.GET.get('phone')
    foundPatients=""
    if(phone):
        phone=phone.strip()
        foundPatients=Patients.objects.all().filter(phone=phone)
    return render(request,'findUser.html',{'foundPatients':foundPatients, 'phone':phone})

