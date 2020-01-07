from feed.models import Feed
from django import forms

class FeedForm(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"What's on your mind today"}))
	image = forms.ImageField(label='Photos')

	class Meta:
		model = Feed
		fields = ['post','image']