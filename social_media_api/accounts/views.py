from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer

from .serializers import RegisterSerializer, LoginSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response(serializer.errors, status=400)
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)

        if target_user == request.user:
            return Response({"error": "You cannot follow yourself"}, status=400)

        request.user.following.add(target_user)
        return Response(
            {"message": f"You are now following {target_user.username}"}, 
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)

        request.user.following.remove(target_user)
        return Response(
            {"message": f"You unfollowed {target_user.username}"},
            status=status.HTTP_200_OK
        )