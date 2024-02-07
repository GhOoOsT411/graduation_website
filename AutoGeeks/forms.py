from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    # Meta class defines the model and fields for the form
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'phone_number', 'birth_date', 'gender', 'password', 'country', 'city', 'postal_code']
        widgets = {
            'gender': forms.RadioSelect(),
        }

    # Custom form field for re-entering the password
    re_password = forms.CharField(widget=forms.PasswordInput, label='Repeat Your Password', required=True)

    # Clean method to perform additional validation
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password and password != re_password:
            raise forms.ValidationError("Passwords do not match. Please enter matching passwords.")

        return cleaned_data

class LoginForm(forms.Form):
    # Form fields for the login form
    email = forms.EmailField(label='Enter the Email')
    password = forms.CharField(widget=forms.PasswordInput)
