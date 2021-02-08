from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to="assets/images", default="no-img.jpg", blank=True
    )
    bio = models.TextField(default="", help_text=_("Write something about yourself!"))

    def __str__(self):
        return self.user.username
