from .models import TelegramUser

def get_or_create_user(message):
    tg = message.from_user

    user, created = TelegramUser.objects.get_or_create(
        telegram_id=tg.id,
        defaults={
            "username": tg.username,
            "first_name": tg.first_name,
            "last_name": tg.last_name,
        }
    )
    return user