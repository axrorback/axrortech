import sib_api_v3_sdk
from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

User = get_user_model()


@shared_task
def send_post_email(title, content, url):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY

    api = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    emails = list(User.objects.exclude(email="").values_list("email", flat=True))

    if not emails:
        return "Foydalanuvchilar topilmadi"

    to_emails = [{"email": e} for e in emails]

    html_content = render_to_string("emails/new_post.html", {
        "title": title,
        "content": content,
        "url": url
    })

    email_data = sib_api_v3_sdk.SendSmtpEmail(
        to=to_emails,
        sender={
            "email": "news@axror.tech",
            "name": "axrorback"
        },
        subject=f"Yangi maqola: {title}",
        html_content=html_content
    )

    try:
        api.send_transac_email(email_data)
        return f"{len(emails)} ta foydalanuvchiga yuborildi."
    except Exception as e:
        return f"Xatolik yuz berdi: {str(e)}"


@shared_task
def send_donation_thanks_email(user_email, user_name, amount):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY
    api = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    html_content = render_to_string("emails/donation_thanks.html", {
        "user_name": user_name,
        "amount": amount,
    })

    email_data = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": user_email}],
        sender={"email": 'donate@axror.tech', "name": "Donat uchun Rahmat!"},
        subject="Katta rahmat! Qo'llab-quvvatlaganingiz uchun tashakkur",
        html_content=html_content
    )

    try:
        api.send_transac_email(email_data)
        return f"Rahmatnoma yuborildi: {user_email}"
    except Exception as e:
        return f"Email yuborishda xatolik: {str(e)}"