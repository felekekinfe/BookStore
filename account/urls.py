from django.urls import path
from .views import UserRegisterView,UserLoginView


urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('login_page/',UserLoginView.as_view(),name='login_page')
]
