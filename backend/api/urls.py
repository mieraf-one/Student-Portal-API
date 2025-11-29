from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views import SignUpView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('signup/', SignUpView.as_view(), name='signup')

]
