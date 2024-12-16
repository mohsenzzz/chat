from django.urls import path
from . import views
urlpatterns=[
    path('users',views.UserChatListView.as_view(),name='users'),
    path('detail/<int:token>',views.UserChatDetailView.as_view(),name='chat_detail'),
]