from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from asosiy.tasks import send_post_email


@receiver(post_save, sender=Post)
def notify_users_on_new_post(sender, instance, created, **kwargs):

    if created:
        post_url = f"https://axror.tech/blog/detail/{instance.slug}/"
        send_post_email.delay(
            title=instance.title,
            content=instance.content[:200],
            url=post_url
        )