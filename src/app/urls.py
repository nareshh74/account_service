from django.urls import path, include
from app.controllers.controllers import login, authorize, sign_up, logout


urlpatterns = [
    path('signUp', sign_up, name='test'),
    path('login', login, name='get user consent'),
    path('logout', logout, name='get user consent'),
    path('token', authorize, name='get access token from auth code'),
]
