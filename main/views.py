from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse

def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow:",
        "Sitemap: https://robochi.work/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

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
    if not _came_from_home(request):
        return redirect("home")
    return render(request, "how.html")

def policy(request):
    if not _came_from_home(request):
        return redirect("home")

    offer_path = os.path.join(settings.BASE_DIR, "legal", "offer.txt")
    privacy_path = os.path.join(settings.BASE_DIR, "legal", "privacy.txt")

    with open(offer_path, "r", encoding="utf-8") as f:
        offer_text = f.read()

    with open(privacy_path, "r", encoding="utf-8") as f:
        privacy_text = f.read()

    return render(request, "policy.html", {
        "offer_text": offer_text,
        "privacy_text": privacy_text,
    })

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow:",
        "Sitemap: http://robochi.work/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def need_telegram(request, role):
    if not _came_from_home(request):
        return redirect("home")

    if role == "employer":
        telegram_link = "https://t.me/ArtemDiablero"
    elif role == "worker":
        telegram_link = "https://t.me/robochi_work"
    else:
        telegram_link = "https://t.me/robochi_work"

    return render(request, "need_telegram.html", {
        "telegram_link": telegram_link
    })
from django.http import JsonResponse

def chrome_devtools(request):
    return JsonResponse({})
