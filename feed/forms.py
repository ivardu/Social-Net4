from feed.models import Feed, Likes, Comments
from django import forms

class FeedForm(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"What's on your mind today"}))
	image = forms.ImageField(label='Photos')

	class Meta:
		model = Feed
		fields = ['post','image']

class LikeForm(forms.ModelForm):

	class Meta:
		model = Likes
		fields = ['likes']

class CommentForm(forms.ModelForm):
	comments = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Your comment..!!','class':'small form-control'}))
	class Meta:
		model = Comments
		fields = ['comments']