from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(
        queryset=User.objects.all(), message="Email already exist")])
    password = serializers.CharField(required=True)
    contact_number = serializers.CharField(required=True)
    company_name = serializers.CharField(required=True)
    designation = serializers.CharField(required=True)
    membership_id = serializers.CharField(required=False)
    nationality = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'contact_number',
                  'company_name', 'designation', 'membership_id', 'nationality']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'contact_number',
                  'company_name', 'designation', 'membership_id', 'nationality']
