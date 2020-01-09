from django.db import models
from users.models import SnetUser
from PIL import Image

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

	def __str__(self):
		return f'{self.user} Post'

	def save(self, **kwargs):
		super().save(**kwargs)
		img = Image.open(self.image.path)
		if img.height > 400 and img.width > 400:
			output = (400, 400)
			img.thumbnail(output)
			img.save(self.image.path)


class Likes(models.Model):
	feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
	likes = models.IntegerField()
	user = models.ForeignKey(SnetUser, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.feed} Likes'

class Comments(models.Model):
	comments = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	feed = models.ForeignKey(Feed, on_delete=models.CASCADE) 
	user = models.ForeignKey(SnetUser, on_delete=models.CASCADE)

	class Meta:
		ordering = ['-date']


	def __str__(self):
		return f'{self.user} Comments'