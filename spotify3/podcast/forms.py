from django import forms

class form1(forms.Form):
    email = forms.EmailField(required=False,widget=forms.EmailInput(
        attrs={"paleceholder":"you@gmail.com","class":"mail-box"}
        ))
    episode_per_week = forms.IntegerField(widget=forms.NumberInput(attrs={'min':1,'max':5}))
    favorate_genere = forms.ChoiceField(
        required=False,
        choices=[
            ("music", "music"),
            ("comedy", "comedy"),
            ("TrueCrime", "TrueCrime")
        ],
        widget=forms.RadioSelect,
    )
    notify_new_episodes = forms.BooleanField(required=False,
                                             widget=forms.CheckboxInput,
                                             )
    subscribe_date = forms.DateField(required=False)

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if len(email) < 15:
            raise forms.ValidationError(
                "You entered an invalid gmail thts less than 15 characters."
            )

        if "test" in email.lower():
            raise forms.ValidationError(
                "Your mail must not contain the word test."
            )

        return email

    def clean(self):
        cleaned_data = super().clean()

        var1 = cleaned_data.get("email")
        var2 = cleaned_data.get("favorate_genere")

        if bool(var1) != bool(var2):
            raise forms.ValidationError(
                "Email and favorite genre must be entered together or both left empty."
            )

        return cleaned_data

    