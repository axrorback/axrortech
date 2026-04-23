from django.urls import path
from .views import *

urlpatterns = [
    path('',AboutDetailView.as_view(),name='about'),
    path('contact/',ContactCreateView.as_view(),name='contact'),
    path('achievement/',AchievementListView.as_view(),name='achievement'),
    path('achievement/detail/<int:pk>/',AchievementDetailView.as_view(),name='achievement_detail'),
]