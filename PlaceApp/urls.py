from django.urls import path
from .views import *

urlpatterns=[
    path('',place),
    path('detail',detail)
]