from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import UserCreateSerializer, UserValidateSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView




class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        User.objects.create_user(username=username, password=password)
        return Response(status=status.HTTP_201_CREATED)

class LoginAPIVIew(APIView):
    def post(self, request):
        serializer = UserValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={
                                'message': 'User credentials are wrong!'
                            })
        token, created = Token.objects.get_or_create(user=user)
        print(created)
        return Response(data={'key': token.key})





