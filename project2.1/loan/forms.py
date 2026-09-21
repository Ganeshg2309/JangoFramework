from django import forms

class form1(forms.Form):
    name=forms.CharField(required=False)
    address=forms.CharField(required=False)
    account_number=forms.CharField(required=False)