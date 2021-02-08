from django.contrib.auth.models import User
from django.db.models.signals import post_save

from accounts.models import Profile


def create_profile(**kwargs):
    if kwargs["created"]:
        Profile.objects.create(user=kwargs["instance"])


post_save.connect(create_profile, sender=User)
