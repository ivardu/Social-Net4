from users.models import SnetUser, Profile, Friends
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegForm(UserCreationForm):
	# username = forms.CharField(label='username', widget=forms.)
	GENDER_CHOICES = (
			('M','Male'),
			('F','Female'),
			('T','Trans')
		)
	email = forms.CharField(label='Email', widget=forms.EmailInput())
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
	dob = forms.DateField(input_formats=['%d/%m/%Y'])
	first_name= forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	gender = forms.ChoiceField(choices=GENDER_CHOICES)

	class Meta:
		model = SnetUser
		fields = ['username','email','first_name','last_name','dob','gender']
		help_texts ={
			'username':None,
			'password1':None,
			'password2':None
		}

class ProfileForm(forms.ModelForm):
	profile_img = forms.ImageField(label='Profile Pic')

	class Meta:
		model = Profile
		fields = ['profile_img']

class UserUpdateForm(forms.ModelForm):

	class Meta:
		model = SnetUser
		fields = ['first_name','last_name','email','dob']

# class PasswordUpdateForm(forms.models)


class FriendReqForm(forms.ModelForm):

	class Meta:
		model = Friends
		fields = ['friend_req_sent']

class FriendsForm(forms.ModelForm):
	class Meta:
		model = Friends
		fields = ['friends']
