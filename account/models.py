from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
	user = models.ForeignKey(User)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	dob = models.DateTimeField(default=now())
	telephone = models.CharField(max_length=15)

	def __unicode__(self):
		return self.username




