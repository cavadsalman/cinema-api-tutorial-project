from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from .serializers import (
    User, RegisterSerializer
)
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status

class RegisterAV(RetrieveAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    
@api_view(['GET'])
def say_my_name(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    return Response({'first_name': first_name, 'last_name': last_name})

@api_view(['POST'])
def login_view(request):
    username, password = request.data.get('username'), request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token_data = Token.objects.get_or_create(user=user)
        print(token_data)
        token = token_data[0].key
        return Response(token)
    else:
        return Response({'message': 'Username or password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_202_ACCEPTED)