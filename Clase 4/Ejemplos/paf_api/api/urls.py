from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from api import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegisterView.as_view()),
    path('auth/', auth_views.obtain_auth_token),
    path('user/', views.UserView.as_view()),
    path('user/<int:pk>/', views.UserDetailedView.as_view()),
    path('tuit/', views.TuitView.as_view()),
    path('tuit/<int:pk>/', views.TuitDetailedView.as_view()),
]
