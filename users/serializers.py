from rest_framework import serializers
from .models import User
from rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_student', 'is_teacher')


class CustomeRegisterSerializer(RegisterSerializer):
    is_student = serializers.BooleanField()
    is_teacher = serializers.BooleanField()
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_student', 'is_teacher')