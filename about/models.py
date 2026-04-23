from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class About(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    content = CKEditor5Field(config_name='default')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/axror/', blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at']



class ContactLinks(models.Model):
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    github_username = models.CharField(max_length=200)
    telegram_username = models.CharField(max_length=200)
    website_url = models.URLField()
    linkedin_url = models.URLField()
    instagram_url = models.URLField()
    facebook_url = models.URLField()
    twitter_url = models.URLField()

    def __str__(self):
        return self.phone_number


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    answer = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    achievement_year = models.IntegerField()
    description = CKEditor5Field(config_name='default')
    image = models.ImageField(upload_to='media/axror/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title