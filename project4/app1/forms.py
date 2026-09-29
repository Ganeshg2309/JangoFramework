from django import forms
from .models import model1

class form1(forms.ModelForm):
    class Meta:
        model=model1
        fields=["name","p","r","t",]
