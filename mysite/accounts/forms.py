from django import forms
from .models import CustomUser


class Signup(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['first_name' , 'last_name','username', 'email']  



