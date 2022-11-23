from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(max_length=30, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'token']
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def get_token(self, obj):
        token = Token.objects.get_or_create(user=obj)[0].key
        return token
    
    def create(self, validated_data):
        username = validated_data.get('username')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
        user.save()
        return user