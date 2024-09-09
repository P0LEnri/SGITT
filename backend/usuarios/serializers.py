from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Alumno, Profesor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

class AlumnoSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profesor
        fields = '__all__'