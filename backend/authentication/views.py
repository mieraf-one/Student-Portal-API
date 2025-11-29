from rest_framework.generics import CreateAPIView
from .serializers import SignUpSerializer


class SignUpView(CreateAPIView):
    serializer_class = SignUpSerializer