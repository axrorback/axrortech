from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView , CreateView , ListView
from .models import About , Contact , ContactLinks , Achievement

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
        return context

    def form_valid(self, form):
        messages.success(self.request, "Xabaringiz muvaffaqiyatli yuborildi! Tez orada javob beramiz.")
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