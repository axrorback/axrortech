from django.contrib import admin
from .models import About , ContactLinks , Contact , Achievement

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')

@admin.register(ContactLinks)
class ContactLinksAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active', 'created_at')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')