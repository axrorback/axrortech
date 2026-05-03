import threading
import sib_api_v3_sdk
from django.template.loader import render_to_string
from django.conf import settings

def send_welcome_email_task(user_email, username):
    def send():
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = settings.BREVO_API_KEY

        api_client = sib_api_v3_sdk.ApiClient(configuration)
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(api_client)

        html_content = render_to_string('emails/welcome_email.html', {'username': username})

        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{"email": user_email}],
            sender={"name": "axror.tech servers!", "email": "welcome@axror.tech"},
            subject="Xush kelibsiz! | axror.tech",
            html_content=html_content
        )

        try:
            api_instance.send_transac_email(send_smtp_email)
        except Exception as e:
            pass

    email_thread = threading.Thread(target=send)
    email_thread.daemon = True
    email_thread.start()