from django.urls import path
from . import views


urlpatterns=[
    path('registerr/',views.RegisterPhoneNumberAPI.as_view(),name='register'),
    path('login/',views.UserLoginAPI.as_view(),name='login'),
    path('profile/',views.ProfileUpdateAPI.as_view(),name='profile'),
    path('profile/update',views.ProfileUpdateAPI.as_view(),name='update-profile'),
]