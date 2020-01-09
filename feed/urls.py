from django.urls import path
from feed import views as feed_view

app_name = 'feed'

urlpatterns = [
	path('',feed_view.HomeView.as_view(), name='home'),
	path('feed/',feed_view.feedlist, name='feed'),
	path('myposts/<int:pk>/',feed_view.MyPostsList.as_view(), name='myposts'),
	path('edit/<int:pk>/',feed_view.EditPost.as_view(),name='edit'),
]