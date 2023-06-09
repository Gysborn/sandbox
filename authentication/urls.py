from django.urls import path
from rest_framework.authtoken import views

from authentication.views import UserCreateView, UserListView, UserRetrieveView, UserUpdateView, UserDestroyView

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', UserRetrieveView.as_view(), name='user'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDestroyView.as_view(), name='user_del'),

]
