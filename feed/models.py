from django.db import models
from users.models import SnetUser

# Create your models here.

def feed_images(instance, filename):
	return f'{instance.user.username}/{filename}'

class Feed(models.Model):
	post = models.CharField(max_length=255)
	image = models.ImageField(upload_to=feed_images)
	user = models.ForeignKey(SnetUser, on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)