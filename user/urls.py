from django.urls import path
from . import views


urlpatterns=[
    path('registerr/',views.RegisterPhoneNumberAPI.as_view(),name='register'),
    path('login/',views.UserLoginAPI.as_view(),name='login'),
]