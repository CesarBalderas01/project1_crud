from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'user_email', 'user_phone']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'user_phone': forms.TextInput(attrs={'class': 'form-control'})
        }
    