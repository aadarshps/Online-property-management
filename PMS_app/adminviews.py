from django.contrib import messages
from django.shortcuts import render, redirect

from PMS_app.forms import AddBill
from PMS_app.models import Customer, Owner, Property, Appointment, Bill


def view_cus(request):
    data = Customer.objects.all()
    return render(request,'view_cus.html',{'data':data})

def view_owner(request):
    data = Owner.objects.all()
    return render(request,'view_owner.html',{'data':data})

def approve_cus(request,id):
    cus = Customer.objects.get(user_id=id)
    cus.approval_status = True
    cus.save()
    messages.info(request, 'approved')
    return redirect('view_cus')

def del_cus(request,id):
    data = Customer.objects.get(user_id=id)
    data.delete()
    return redirect('view_cus')

def approve_owner(request,id):
    ow = Owner.objects.get(user_id=id)
    ow.approval_status = True
    ow.save()
    messages.info(request, 'approved')
    return redirect('view_owner')

def del_owner(request,id):
    data = Owner.objects.get(user_id=id)
    data.delete()
    return redirect('view_owner')

def view_property_ad(request):
    data = Property.objects.all()
    return render(request,'view_property_ad.html',{'data':data})

def approve_property(request,id):
    ow = Property.objects.get(id=id)
    ow.approval_status = True
    ow.save()
    messages.info(request, 'approved')
    return redirect('view_property_ad')

def del_property(request,id):
    data = Property.objects.get(id=id)
    data.delete()
    return redirect('view_property_ad')


def appointment_adminss(request):
    a = Appointment.objects.all()
    context = {
        'appointment': a,
    }
    return render(request, 'appointment_adminss.html', context)

def generate_bill(request):
    form = AddBill()
    if request.method == 'POST':
        form = AddBill(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_payment_details')
    return render(request, 'generate_bill.html', {'form': form})


def view_payment_details(request):
    bill = Bill.objects.all()
    print(bill)
    return render(request, 'view_payment_details.html', {'bills': bill})



