from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


# Create your models here.

# UserCreation Model 
class SnetUser(AbstractUser):
	GENDER_CHOICES = (
			('M','Male'),
			('F','Female'),
			('T','Trans')
		)
	dob = models.DateField()
	gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'




# Profile Image Storage Locatiom
def profile_image(instance, filename):
	return f'{instance.user.username}/profile_pics/{filename}'

# Profile Image Model
class Profile(models.Model):
	profile_img = models.ImageField(default='default.png/', upload_to=profile_image)
	user = models.OneToOneField(SnetUser, on_delete=models.CASCADE) 

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save(*args,**kwargs)
		img = Image.open(self.profile_img.path)
		if img.width > 400 and img.height >400:
			output = (200,200)
			img.thumbnail(output)
			img.save(self.profile_img.path)
