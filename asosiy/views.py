import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from asosiy.tasks import send_donation_thanks_email
from blog.models import Post
from about.models import About
from django.contrib.auth.models import User
import requests
from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse
from django.db.models import Sum
from .models import Donation
from django.contrib import messages
from django.conf import settings

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = Post.objects.filter(is_active=True).count()
        context['latest_posts'] = Post.objects.filter(is_active=True).order_by('-created_at')[:7]
        context['about_short'] = About.objects.filter(is_active=True).first()
        return context

def robots_txt(request):
    return render(
        request,
        "robots.txt",
        content_type="text/plain"
    )
@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    social = user.socialaccount_set.filter(provider="google").first()
    context = {
        "user_obj": user,
        "profile": profile,
        "social": social,
    }
    return render(request, "users/profile.html", context)

@login_required
def donate_page(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        message = request.POST.get("message")
        token = request.POST.get("g-recaptcha-response")

        if not token:
            messages.error(request, "Captcha topilmadi.")
            return redirect("donate")

        data = {
            "secret": settings.RECAPTCHA_SECRET_KEY,
            "response": token
        }

        try:
            r = requests.post(
                "https://www.google.com/recaptcha/api/siteverify",
                data=data,
                timeout=5
            )
            result = r.json()
        except requests.RequestException:
            messages.error(request, "Captcha tekshirishda xatolik.")
            return redirect("donate")

        if not result.get("success") or result.get("score", 0) < 0.5:
            messages.error(request, "Captcha tasdiqlanmadi.")
            return redirect("donate")

        full_name = (
            f"{request.user.first_name} {request.user.last_name}".strip()
            or request.user.username
        )

        callback_url = request.build_absolute_uri(reverse("callback_donate"))

        payload = {
            "amount": amount,
            "purpose": "donation",
            "reference_id": f"donate_{request.user.username}",
            "user_id": str(request.user.id),
            "callback_url": callback_url,
        }

        try:
            res = requests.post(
                "https://pay.axror.tech/payment/create/",
                json=payload,
                timeout=15
            )
            data = res.json()

            Donation.objects.create(
                user=request.user,
                full_name=full_name,
                amount=amount,
                message=message,
                order_id=str(data.get("order_id")),
                status=Donation.Status.PENDING
            )

            return redirect(data["payment_url"])

        except Exception:
            messages.error(request, "To'lov xizmati vaqtincha ishlamayapti.")
            return redirect("donate")

    top_donators = Donation.objects.filter(
        status=Donation.Status.SUCCESS
    ).order_by('-amount')[:10]

    total_sum = Donation.objects.filter(
        status=Donation.Status.SUCCESS
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, "donate.html", {
        "top_donators": top_donators,
        "total_sum": total_sum,
        "RECAPTCHA_SITE_KEY": settings.RECAPTCHA_SITE_KEY
    })

@csrf_exempt
def donation_callback(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed. POST only."}, status=405)

    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, TypeError):
        return JsonResponse({"error": "Invalid JSON format"}, status=400)

    order_id = str(data.get("order_id"))
    status = data.get("status")

    donation = Donation.objects.filter(order_id=order_id).first()

    if not donation:
        return JsonResponse({"error": f"Donation with order_id {order_id} not found"}, status=404)

    if status == "success":
        donation.status = Donation.Status.SUCCESS
        donation.save()

        if donation.user and donation.user.email:
            send_donation_thanks_email.delay(
                user_email=donation.user.email,
                user_name=donation.user.get_full_name() or donation.user.username,
                amount=float(donation.amount)
            )
    else:
        donation.status = Donation.Status.FAILED
        donation.save()

    return JsonResponse({"ok": True, "message": "Status updated successfully"})


def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)