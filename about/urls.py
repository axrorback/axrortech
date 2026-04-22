from django.urls import path
from .views import *

urlpatterns = [
    path('',AboutDetailView.as_view(),name='about'),
]