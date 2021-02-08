from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ("user", "id")


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "last_login",
            "username",
            "email",
            "date_joined",
            "first_name",
            "last_name",
            "profile",
        )
