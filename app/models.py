# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Account(models.Model):
    user =  models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.user +" | "+ self.passwd + " | " + self.phone


class Address(models.Model):
    street = models.CharField(max_length=60)
    address2 = models.CharField(max_length=60)
    city = models.CharField(max_length=10)
    zip = models.CharField(max_length=10)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.street +" | "+ self.state + " | " + self.phone + " | " + self.zip

class PayDetails(models.Model):
    paynumber = models.CharField(max_length=16)
    expmonth = models.CharField(max_length=2)
    expyear = models.CharField(max_length=4)
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return self.paynumber +" | "+ self.cvv +" | "+ self.expmonth +" | "+ self.expyear

class Lead(models.Model):
    user = models.CharField(max_length=35)
    passwd = models.CharField(max_length=20)
    phone = models.CharField(max_length=16)
    street = models.CharField(max_length=60)
    address2 = models.CharField(max_length=60)
    city = models.CharField(max_length=10)
    zip = models.CharField(max_length=10)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=10)
    paynumber = models.CharField(max_length=16)
    expmonth = models.CharField(max_length=2)
    expyear = models.CharField(max_length=4)
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return self.user +" | "+ self.passwd + " | " + self.phone + " | " +  self.street +" | "+ self.state + " | " + self.phone + " | " + self.zip + " | " + self.paynumber +" | "+ self.cvv +" | "+ self.expmonth +" | "+ self.expyear
