from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .bot import bot
import telebot
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def telegram_webhook(request):
    if request.method != "POST":
        return JsonResponse({"error": "invalid request"})

    try:
        json_str = request.body.decode("utf-8")

        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])

        return JsonResponse({"ok": True})

    except Exception as e:
        logger.exception("Webhook error")
        return JsonResponse({"ok": False, "error": str(e)})