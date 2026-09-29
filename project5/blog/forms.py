from .models import post
from django import forms

class postform(forms.ModelForm):
    class Meta:
        model=post
        fields=['title','content','author']
