from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control bg-light', 'placeholder': 'Ism'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control bg-light', 'placeholder': 'Familiya'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-light', 'placeholder': 'Email'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        widgets = {
            'avatar': forms.URLInput(attrs={'class': 'form-control bg-light', 'placeholder': 'Avatar URL'}),
            'bio': forms.Textarea(attrs={'class': 'form-control bg-light', 'rows': 3, 'placeholder': 'O‘zingiz haqingizda...'}),
        }