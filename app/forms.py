from django import forms


class SignIn(forms.Form):
    user = forms.CharField(label='User', max_length=100)
    passwd = forms.CharField(label='Passwd', max_length=100)
    phone = forms.CharField(label='Phone', max_length=100)