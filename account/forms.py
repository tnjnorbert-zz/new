from account.models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = UserProfile
		fields = ('first_name', 'last_name', 'address', 'dob', 'telephone')