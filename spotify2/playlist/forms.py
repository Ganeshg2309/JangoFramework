from django import forms

class PlayListForm(forms.Form):
    title=forms.CharField()
    discription=forms.CharField(required=False,widget=forms.Textarea)
