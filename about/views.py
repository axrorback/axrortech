from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView , CreateView , ListView
from .models import About , Contact , ContactLinks , Achievement
import requests
from django.conf import settings

class AboutDetailView(DetailView):
    model = About
    template_name = 'about/hero.html'
    context_object_name = 'about'
    def get_object(self, queryset=None):
        return About.objects.filter(is_active=True).first()

class ContactCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'message']
    template_name = 'about/contact.html'
    success_url = reverse_lazy('contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['links'] = ContactLinks.objects.first()

        context['RECAPTCHA_SITE_KEY'] = settings.RECAPTCHA_SITE_KEY

        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        if self.request.user.is_authenticated:
            form.fields.pop('name')
            form.fields.pop('email')

        return form

    def form_valid(self, form):
        request = self.request

        token = request.POST.get('g-recaptcha-response')

        if not token:
            messages.error(request, "Captcha topilmadi.")
            return self.form_invalid(form)

        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': token
        }

        try:
            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data=data,
                timeout=5
            )
            result = r.json()
        except requests.RequestException:
            messages.error(request, "Captcha tekshirishda xatolik.")
            return self.form_invalid(form)

        if not result.get('success') or result.get('score', 0) < 0.5:
            messages.error(request, "Captcha tasdiqlanmadi.")
            return self.form_invalid(form)

        if request.user.is_authenticated:
            form.instance.name = (
                request.user.get_full_name()
                or request.user.username
            )
            form.instance.email = request.user.email

        messages.success(
            request,
            "Xabaringiz muvaffaqiyatli yuborildi! Tez orada javob beramiz."
        )

        return super().form_valid(form)

class AchievementListView(ListView):
    model = Achievement
    template_name = 'achievements/achievement_list.html'
    context_object_name = 'achievements'
    paginate_by = 6

    def get_queryset(self):
        return Achievement.objects.filter(is_active=True).order_by('-created_at')

class AchievementDetailView(DetailView):
    model = Achievement
    template_name = 'achievements/achievement_detail.html'
    context_object_name = 'achievement'