from django.urls import path

from .views import UserRegister, MyTokenObtainPairView


urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='login')
]