from django.urls import path
from django_app.views import (
    HomePage,
    RegisterPage,
    LoginPage,
    LogoutPage
)

urlpatterns = [
    path('', HomePage, name="home"),
    path('register/', RegisterPage, name="register"),
    path('login/', LoginPage, name="login"),
    path('logout/', LogoutPage, name="logout"),
]
