from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from common.views import BaseApiView
from .models import User
from .serializer import UserSerializer, UserSignUpSerializer


class RegisterAPIView(BaseApiView):

    def post(self, request):

        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            extra = {
                'password': make_password(serializer.validated_data.get('password')),
                'username': serializer.validated_data.get('email')
            }
            obj = serializer.save(**extra)
            return self.render_response(
                UserSerializer(obj).data,
                True,
                None,
                data_to_list=False
            )
        else:
            return self.render_response(serializer.errors, False, 'Error while creating a user', status=400)


class LoginAPIView(BaseApiView):

    def post(self, request):
        user = authenticate(
            username=request.data.get('email', ''),
            password=request.data.get('password', '')
        )
        if user and user.is_active:
            token = Token.objects.filter(user=user)
            if token:
                token.delete()
            token = Token.objects.create(user=user)
            return self.render_response(user.first_name, True, "", token=token.key)
        else:
            return self.render_response({}, False, "Incorrect email and password", status=400)
