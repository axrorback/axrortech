from django.urls import path
from .views import *
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('robots.txt',robots_txt,name='robots'),
    path('profile/<str:username>/',profile_view,name='profile'),
    path('donate/',donate_page,name='donate'),
    path('callback-donate/',donation_callback,name='callback_donate')
]