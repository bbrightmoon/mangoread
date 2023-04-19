from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginAPIVIew.as_view()),
    ]