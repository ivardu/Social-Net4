from django.db import models
from users.models import SnetUser

# Create your models here.

def feed_images(instance, filename):
	return f'{instance.user.username}/{filename}'

class Feed(models.Model):
	post = models.CharField(max_length=255)
	image = models.ImageField(upload_to=feed_images)
	user = models.ForeignKey(SnetUser, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date']


class Likes(models.Model):
	feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
	likes = models.IntegerField()
	user = models.ForeignKey(SnetUser, on_delete=models.CASCADE)

class Comments(models.Model):
	comments = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	feed = models.ForeignKey(Feed, on_delete=models.CASCADE) 
	user = models.ForeignKey(SnetUser, on_delete=models.CASCADE)

	class Meta:
		ordering = ['-date']