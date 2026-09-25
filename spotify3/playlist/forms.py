from django import forms
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError

class PlayListForm(forms.Form):
    title=forms.CharField()
    discription=forms.CharField(required=False,widget=forms.Textarea)

def SpecialCharValidator(value):
    if "@" in value or "#" in value or "$" in value or "%" in value:
        raise ValidationError("dont use special character in searching ")

class SongRequestForm(forms.Form):
    song_name=forms.CharField(
        validators = [ MinLengthValidator(2), MaxLengthValidator(100),SpecialCharValidator] ,error_messages={"required":"please tell us which song you want"}
        )
    requester_email=forms.EmailField()
    votes_requested=forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])


