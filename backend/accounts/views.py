from django.contrib.auth.models import User

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from accounts.serializers import ProfileSerializer, UserSerializer


class ProfileRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
