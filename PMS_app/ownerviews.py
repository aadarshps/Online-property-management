from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect, render

from PMS_app.forms import PropertyForm, SchdeuleForm
from PMS_app.models import Owner, Property, Customer, Schedule, Appointment, Bill


def property_add(request):
    user = request.user
    form = PropertyForm()
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                owner, created = Owner.objects.get_or_create(user=user)  # Get or create Owner instance
                data = form.save(commit=False)
                data.owner_name = owner  # Assign the Owner instance to the owner_name field
                data.save()
                return redirect('property_view_ow')
            except IntegrityError:
                # Handle integrity error, maybe log it or show a meaningful message to the user
                pass
    return render(request, 'property_add.html', {'form': form})

def property_view_ow(request):
    u= Owner.objects.get(user=request.user)
    data = Property.objects.filter(owner_name=u)
    return render(request,'property_view_ow.html',{'data':data})

def update_property(request,id):
    detail = Property.objects.get(id=id)
    form = PropertyForm(request.POST or None, instance=detail)
    if form.is_valid():
        form.save()
        messages.info(request, 'property Details Updated Successfully')
        return redirect('property_view_ow')
    return render(request,'update_property.html',{'form':form})

def del_property_ow(request,id):
    data = Property.objects.get(id=id)
    data.delete()
    return redirect('property_view_ow')

def cus_view_ow(request):
    data = Customer.objects.all()
    return render(request,'cus_view_ow.html',{'data':data})


def schedule_add(request):
    form = SchdeuleForm()
    if request.method == 'POST':
        form = SchdeuleForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.owner = Owner.objects.get(user=request.user)
            form.save()
            messages.info(request, 'schedule added successful')
            return redirect('schedule_view')
    return render(request, 'schedule_add.html', {'form': form})



def schedule_view(request):
    owner = Owner.objects.get(user=request.user)
    s = Schedule.objects.filter(owner=owner)
    context = {
        'schedule': s
    }
    return render(request, 'schedule_view.html', context)



def schedule_update(request, id):
    s = Schedule.objects.get(id=id)
    if request.method == 'POST':
        form = SchdeuleForm(request.POST or None, instance=s)
        if form.is_valid():
            form.save()
            messages.info(request, 'schdeule updated')
            return redirect('schedule_view')
    else:
        form = SchdeuleForm(instance=s)
    return render(request, 'schedule_update.html', {'form': form})



def schedule_delete(request, id):
    s = Schedule.objects.filter(id=id)
    if request.method == 'POST':
        s.delete()
        return redirect('schedule_view')

def appointment_admin(request):
    a = Appointment.objects.all()
    context = {
        'appointment': a,
    }
    return render(request, 'appointment_admin.html', context)



def approve_appointment(request, id):
    a = Appointment.objects.get(id=id)
    a.status = 1
    a.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_admin')



def reject_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_admin')

def view_bill_owner(request):
    bill = Bill.objects.all()
    print(bill)
    return render(request, 'view_bill_owner.html', {'bills': bill})