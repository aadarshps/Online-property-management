from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_cus = models.BooleanField(default=False)

class Owner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='owner')
    Name = models.CharField(max_length=200)
    Phone_No = models.CharField(max_length=10)
    Address = models.CharField(max_length=255)
    Email_Id = models.EmailField()
    Photo = models.ImageField(upload_to='photo')
    Id_Card = models.FileField(upload_to='id')
    approval_status = models.BooleanField(default=False)

    def __str__(self):
        return self.Name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="customer")
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=255)
    Phone_Number = models.CharField(max_length=10)
    Email_Id = models.EmailField()
    Photo = models.ImageField(upload_to='pic')
    Id_Card = models.FileField(upload_to='Id')
    approval_status = models.BooleanField(default=0)

    def __str__(self):
        return self.Name

type = (
    ('Land','Land'),
    ('Home','Home'),
    ('Flat','Flat'),
    ('Villa','Villa'),
    ('Shops','Shops'),
    ('Garrage','Garrage'),
    ('Godown','Godown')
)

class Property(models.Model):
    owner_name = models.ForeignKey(Owner,on_delete=models.CASCADE)
    Property_type = models.CharField(max_length=100,choices=type)
    Location = models.CharField(max_length=100)
    Description = models.TextField()
    Rent_amount = models.CharField(max_length=100)
    Documents = models.FileField(upload_to='docs')
    Image1 = models.ImageField(upload_to='img1')
    Image2 = models.ImageField(upload_to='img2')
    Image3 = models.ImageField(upload_to='img3')
    approval_status = models.BooleanField(default=0)

    def __str__(self):
        return self.Property_type

class Schedule(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    property = models.ForeignKey(Property,on_delete=models.CASCADE)


class Appointment(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='appointment')
    user2 = models.ForeignKey(Owner, on_delete=models.DO_NOTHING,null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

class Bill(models.Model):
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bill_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    paid_on = models.DateField(auto_now=True)
    status = models.IntegerField(default=0)


class CreditCard(models.Model):
    card_no = models.CharField(max_length=30)
    card_cvv = models.CharField(max_length=30)
    expiry_date = models.CharField(max_length=200)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    feedback = models.TextField()
    date = models.DateField()
    reply = models.TextField(null=True, blank=True)







