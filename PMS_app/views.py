from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from PMS_app.forms import UserReg, Customer_reg, OwnerForm


# Create your views here.
def homepage(request):
    return render(request,'index.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('adminpage')
        elif user is not None and user.is_cus:
            if user.customer.approval_status == 1:
                login(request, user)
                return redirect('cuspage')
            else:
                messages.info(request, "Your Are Not Approved To Login")
        elif user is not None and user.is_owner:
            if user.owner.approval_status == 1:
                login(request,user)
                return redirect('ownerpage')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request,'loginpage.html')

def ownerreg(request):
    form1 = UserReg()
    form2 = OwnerForm()
    if request.method == 'POST':
        form1 = UserReg(request.POST)
        form2 = OwnerForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_owner = True
            user.save()
            owner = form2.save(commit=False)
            owner.user = user
            owner.save()
            messages.info(request, 'Succesfully Registered')
            return redirect('loginpage')
    return render(request,'ownerreg.html',{'form1':form1,'form2':form2})

def cusreg(request):
    form1 = UserReg()
    form2 = Customer_reg()
    if request.method == 'POST':
        form1 = UserReg(request.POST)
        form2 = Customer_reg(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_cus = True
            user.save()
            customer = form2.save(commit=False)
            customer.user = user
            customer.save()
            messages.info(request, 'Succesfully Registered')
            return redirect('loginpage')
    return render(request,'cusreg.html',{'form1':form1,'form2':form2})

def adminpage(request):
    return render(request,'adminpage.html')

def ownerpage(request):
    return render(request,'ownerpage.html')

def cuspage(request):
    return render(request,'cuspage.html')

def logout_view(request):
    logout(request)
    return redirect('homepage')