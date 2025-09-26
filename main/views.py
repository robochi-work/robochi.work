from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect


import os
from django.conf import settings

def _came_from_home(request) -> bool:
    if request.GET.get("from") == "home":
        return True
    ref = request.META.get("HTTP_REFERER", "")
    return ref.endswith("/") or ref.endswith("/#") or ref.endswith("/?")

def home(request):
    return render(request, "home.html")

def how(request):
    return render(request, "how.html")

def policy(request):
    offer_path = os.path.join(settings.BASE_DIR, "legal", "offer.txt")
    privacy_path = os.path.join(settings.BASE_DIR, "legal", "privacy.txt")

    def read_text_safe(path):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()

        return "Упс яка прикра несподіванка. Напевно щось трапилося. Будь ласка, спробуйте пізніше."

    offer_text = read_text_safe(offer_path)
    privacy_text = read_text_safe(privacy_path)

    return render(request, "policy.html", {
        "offer_text": offer_text,
        "privacy_text": privacy_text,
    })

def robots_txt(request):
    sitemap_url = "https://robochi.work/sitemap.xml"
    lines = [
        "User-agent: *",
        "Disallow:",
        f"Sitemap: {sitemap_url}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def need_telegram_root(request):
    return render(request, "need_telegram.html", {
        "telegram_link": None  
    })

def need_telegram(request, role):
    if role == "employer":
        telegram_link = "https://t.me/robochi_work"
    elif role == "worker":
        telegram_link = "https://t.me/robochi_work_vacancy"
    else:
        telegram_link = "https://t.me/robochi_work"

    return render(request, "need_telegram.html", {
        "telegram_link": telegram_link
    })
from django.http import JsonResponse

def chrome_devtools(request):
    return JsonResponse({})
