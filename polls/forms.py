from django import forms

from .models import Voter

class RegisterForm(forms.ModelForm):

    class Meta:
        model = Voter
        fields = ('voter_name', 'voter_roll','voter_email','voter_username','voter_password')