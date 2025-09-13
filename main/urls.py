from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("how/", views.how, name="how"),
    path("policy/", views.policy, name="policy"),
    path("need-telegram/<str:role>/", views.need_telegram, name="need_telegram"),
    path(".well-known/appspecific/com.chrome.devtools.json",
         views.chrome_devtools,
         name="chrome_devtools"),
]
