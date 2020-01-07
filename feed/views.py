from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from feed.models import Feed
from feed.forms import FeedForm
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
		# Validating and Saving the Feed form data to DB
		if feed_form.is_valid():
			model_obj = feed_form.save(commit=False)
			model_obj.user = request.user
			model_obj.save()

			return HttpResponseRedirect(reverse('feed:feed'))
		# else:
		# 	return HttpResponse(feed_form.errors)

	else:
		feed_form = FeedForm()

	return render(request, 'feed/feed.html', locals())
