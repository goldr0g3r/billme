from django.http import JsonResponse, HttpResponse
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import User
from authentication.serializers import RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

# Create your views here.


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = (AllowAny,)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()


@api_view(["GET"])
def profile(request):

    # check if user is authenticated
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)

    user = request.user
    return HttpResponse(
        f"Welcome {user.first_name} {user.last_name}, you are a {user.role}",
    )


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                "Successfully logged out", status=status.HTTP_205_RESET_CONTENT
            )
        except:
            return Response("Invalid token", status=status.HTTP_400_BAD_REQUEST)
