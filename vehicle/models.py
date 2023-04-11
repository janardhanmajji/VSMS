from django.db import models
from django.contrib.auth.models import User
from twilio.rest import Client
# Create your models here.


class Category(models.Model):
    categoryname = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryname


class EnquiryType(models.Model):
    enqtypename = models.CharField(max_length=100)

    def __str__(self):
        return self.enqtypename


class Enquiry(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    enqno = models.CharField(max_length=15)
    enqtype = models.ForeignKey(EnquiryType, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    enqdate = models.DateField()
    adminresponse = models.CharField(max_length=500, null=True)
    adminstatus = models.CharField(max_length=50, null=True)
    adminremarkdate = models.DateField(null=True)

    def __str__(self):
        return self.enqno


class Mechanic(models.Model):
    fullname = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=15)
    emailid = models.CharField(max_length=100)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.fullname


class ServiceRequest(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    serviceno = models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vehiclename = models.CharField(max_length=100)
    vehiclemodel = models.CharField(max_length=30)
    vehiclebrand = models.CharField(max_length=50)
    vehicleregno = models.CharField(max_length=15)
    servicedate = models.DateField()
    servicetime = models.TimeField()
    deltype = models.CharField(max_length=50)
    pickupaddr = models.CharField(max_length=300)
    servicereqdate = models.DateField(null=True)
    serviceby = models.ForeignKey(
        Mechanic, on_delete=models.CASCADE, null=True)
    servicecharge = models.CharField(max_length=50, null=True)
    partscharge = models.CharField(max_length=50, null=True)
    othercharge = models.CharField(max_length=50, null=True)
    adminremark = models.CharField(max_length=500, null=True)
    adminstatus = models.CharField(max_length=100, null=True)
    adminremarkdate = models.DateField(null=True)

    def save(self, *args, **kwargs):

        if self.adminstatus == "Accept":
            account_sid = 'AC9a564825e9614bc8d66e6842eab752f4'
            auth_token = '692d91fb43a9cceda2d18b1e685e016a'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body='Your vehicle Service of number  has been Accepted. Thank you',
                from_='+15074686257',
                to='+919392432966'
            )

            print(message.sid)

        if self.adminstatus == "Complete":
            account_sid = 'AC9a564825e9614bc8d66e6842eab752f4'
            auth_token = '692d91fb43a9cceda2d18b1e685e016a'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body='Your vehicle Service has been complete. You can take it back',
                from_='+15074686257',
                to='+919392432966'
            )

            print(message.sid)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.serviceno
