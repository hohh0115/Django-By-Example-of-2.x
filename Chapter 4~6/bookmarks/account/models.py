from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	"""docstring for Profile"""
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, default='users/default/default_user.png')

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)

class Contact(models.Model):
	"""docstring for Contact"""
	user_from = models.ForeignKey(User, related_name='rel_from_set', on_delete=models.CASCADE)
	user_to = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
	created = models.DateField(auto_now_add=True, db_index=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return '{} follows {}'.format(self.user_from, self.user_to)

# Add following field to User dynamically
User.add_to_class('following',
                   models.ManyToManyField('self',
                                          through=Contact,
                                          related_name='followers',
                                          symmetrical=False))