from django.contrib import admin
from bot.models import UserMessage , TelegramUser

@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'created_at')

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'username', 'created_at',)