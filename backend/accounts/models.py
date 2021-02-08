from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to="assets/images", default="no-img.jpg", blank=True
    )
    bio = models.TextField(default="", help_text=_("Write something about yourself!"))

    def __str__(self):
        return self.user.username


def create_profile(**kwargs):
    if kwargs["created"]:
        Profile.objects.create(user=kwargs["instance"])


post_save.connect(create_profile, sender=User)
