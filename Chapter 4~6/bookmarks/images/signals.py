from django.db.models.signals import m2m_changed # Sent when a ManyToManyField is changed on a model instance.
from django.dispatch import receiver
from .models import Image

# decorators way to bing the receiver() function to signals
@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
	instance.total_likes = instance.users_like.count()
	instance.save()