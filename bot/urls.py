from django.urls import path
from bot.views import telegram_webhook

urlpatterns = [
    path('webhook/', telegram_webhook),
]