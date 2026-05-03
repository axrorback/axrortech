#Bu adapterni ishlatmadim !

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)

        extra_data = sociallogin.account.extra_data

        user.email = extra_data.get("email", user.email)
        user.first_name = extra_data.get("given_name", user.first_name)
        user.last_name = extra_data.get("family_name", user.last_name)

        user.save()
        return user