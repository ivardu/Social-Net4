from users.models import SnetUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegForm(UserCreationForm):

	class Meta:
		model = SnetUser
		fields = ['username','email','dob']