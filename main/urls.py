from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_register_view, name='login_register'),
]
