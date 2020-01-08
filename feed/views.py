from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from feed.models import Feed
from feed.forms import FeedForm, CommentForm, LikeForm
from django.contrib.auth.decorators import login_required
# Create your views here.


# This view is for the Home Page of the Social Net with List of the Feed by ready-only
class HomeView(ListView):
	template_name = 'feed/home.html'
	model = Feed

# This view is for the Feed page which will display the feed form, like and comment
@login_required
def feedlist(request):
	# Feed objects all list 
	feed_list = Feed.objects.all()

	if request.method == 'POST':
		feed_form = FeedForm(request.POST, request.FILES) 
		likes_form = LikeForm(request.POST)
		comments_form = CommentForm(request.POST)
		if request.POST.get('post_id'):
			feed_obj = Feed.objects.get(pk=request.POST.get('post_id'))
			already_liked = feed_obj.likes_set.filter(user=request.user) and True or False
		# Validating and Saving the Feed form data to DB
		if feed_form.is_valid():
			feed_model_obj = feed_form.save(commit=False)
			feed_model_obj.user = request.user
			feed_model_obj.save()

			return HttpResponseRedirect(reverse('feed:feed'))

		# Validating the like form
		elif likes_form.is_valid() and already_liked==False:
			likes_model_obj = likes_form.save(commit=False)
			likes_model_obj.feed = feed_obj
			likes_model_obj.user = request.user
			likes_model_obj.likes = request.POST['likes']
			likes_model_obj.save()

			return HttpResponseRedirect(reverse('feed:feed'))

		# Validating the Comment form
		elif comments_form.is_valid():
			comments_model_obj = comments_form.save(commit=False)
			comments_model_obj.feed = feed_obj
			comments_model_obj.user = request.user
			comments_model_obj.save()

			return HttpResponseRedirect(reverse('feed:feed')) 

		else:
			return HttpResponseRedirect(reverse('feed:feed'))

	else:
		feed_form = FeedForm()
		likes_form = LikeForm()
		comments_form = CommentForm()

	return render(request, 'feed/feed.html', locals())
