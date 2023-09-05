

from rest_framework.views import APIView
from .models import UserProfile
from .serializers import CustomUserSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView


# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            UserProfile.objects.create(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user