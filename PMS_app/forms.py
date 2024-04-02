from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from PMS_app.models import User, Customer, Owner, Property, Schedule,CreditCard,Bill


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class UserReg(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password',widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = ('username','password1','password2')

class Customer_reg(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('user','approval_status')

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        exclude=('user','approval_status')

class PropertyForm(forms.ModelForm):
    class Meta:
        model=Property
        exclude = ('owner_name','approval_status')

class SearchForm(forms.Form):
    Location = forms.CharField(max_length=100)

class SchdeuleForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput, )
    end_time = forms.TimeField(widget=TimeInput, )

    class Meta:
        model = Schedule
        fields = ('date', 'start_time', 'end_time')

class AddBill(forms.ModelForm):
    # name = forms.ModelChoiceField(queryset=Customers.objects.filter(role='customer'))

    class Meta:
        model = Bill
        exclude = ('status', 'paid_on')


class PayBillForm(forms.ModelForm):
    card_no = forms.CharField(validators=[RegexValidator(regex='^.{16}$', message='Please Enter a Valid Card No')])
    card_cvv = forms.CharField(widget=forms.PasswordInput,
                               validators=[RegexValidator(regex='^.{3}$', message='Please Enter a Valid CVV')])
    expiry_date = forms.DateField(widget=DateInput(attrs={'id': 'example-month-input'}))

    class Meta:
        model = CreditCard
        fields = ('card_no', 'card_cvv', 'expiry_date')
