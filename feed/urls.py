from django.urls import path
from feed import views as feed_view

app_name = 'feed'

urlpatterns = [
	path('',feed_view.HomeView.as_view(), name='home'),
	path('feed/',feed_view.feedlist, name='feed'),
]