from django.urls import path
from .views import *

urlpatterns=[
    path('',my_login),
    path('/logout',my_logout),
    path('/register',my_register),
    path('/foruser',foruser),
]