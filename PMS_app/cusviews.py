from django.contrib import messages
from django.shortcuts import render, redirect

from PMS_app.forms import SearchForm
from PMS_app.models import Owner, Property, Schedule, Customer, Appointment, Bill, CreditCard


def own_view(request):
    data = Owner.objects.all()
    return render(request,'own_view.html',{'data':data})

# def view_property_cus(request):
#     data = Property.objects.filter(approval_status=1)
#     return render(request,'view_property_cus.html',{'data':data})

def view_property_cus(request):
    Location=request.GET.get('Location')
    property=Property.objects.filter(approval_status=1)
    if Location:
        property=property.filter(Location__icontains=Location)
    context={
        'form':SearchForm(),
        'data':property
    }
    return render(request,'view_property_cus.html', context)


def view_schedule_customer(request):
    s = Schedule.objects.all()
    context = {
        'schedule': s
    }
    return render(request, 'view_schedule_customer.html', context)



def take_appointment(request, id):
    s = Schedule.objects.get(id=id)
    c = Customer.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=c, schedule=s)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect('view_schedule_customer')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = c
            obj.schedule = s
            obj.save()
            messages.info(request, '[-Appointment Booked Successfully')
            return redirect('appointment_view')
    return render(request, 'take_appointment.html', {'schedule': s})


def appointment_view(request):
    c = Customer.objects.get(user=request.user)
    a = Appointment.objects.filter(user=c)
    return render(request, 'appointment_view.html', {'appointment': a})


def view_bill_user(request):
    u = Customer.objects.get(user=request.user)
    print(u)
    bill = Bill.objects.filter(name=u)
    print(bill)
    return render(request, 'view_bill_user.html', {'bills': bill})


def pay_bill(request, id):
    bi = Bill.objects.get(id=id)
    # form = PayBillForm()
    if request.method == 'POST':
        card = request.POST.get('card')
        c = request.POST.get('cvv')
        da = request.POST.get('exp')
        CreditCard(card_no=card, card_cvv=c, expiry_date=da).save()
        bi.status = 1
        bi.save()
        messages.info(request, 'Bill Paid  Successfully')
        return redirect('bill_history')

        # form = PayBillForm(request.POST)
        # if form.is_valid():
        #     pay = form.save(commit=False)
        #     pay.bill = bi
        #     pay.save()
        #     bi.status = 1
        #     bi.save()

    return render(request, 'pay_bill.html', )


def pay_in_direct(request, id):
    bi = Bill.objects.get(id=id)
    bi.status = 2
    bi.save()
    messages.info(request, 'Choosed to Pay Direct')
    return redirect('bill_history')


def bill_history(request):
    u = Customer.objects.get(user=request.user)
    bill = Bill.objects.filter(name=u, status__in=[1, 2])

    return render(request, 'view_bill_history.html', {'bills': bill})
