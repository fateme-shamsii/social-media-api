from rest_framework import serializers
from .models import User

class CreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if not password == password2:
            raise serializers.ValidationError("Your Password is not match")
        return attrs
    
    def validate_username(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Your Username is empty")

        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is exit")
        return value

    def validate_email(self, value):
        if not value or not value.strip().lower():
            raise serializers.ValidationError("Your email is empty") 
        
        value = value.strip().lower()

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is exit")
        return value   
