from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from .utils import send_welcome_email_task


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    profile, _ = Profile.objects.get_or_create(user=instance)
    profile.save()

@receiver(user_logged_in)
def update_google_user(request, user, **kwargs):
    social = user.socialaccount_set.filter(provider='google').first()

    if social:
        data = social.extra_data
        user.email = data.get("email", user.email)
        user.save()

@receiver(post_save, sender=User)
def auto_welcome_email(sender, instance, created, **kwargs):

    if created and instance.email:
        send_welcome_email_task(instance.email, instance.username)