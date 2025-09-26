from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return ['home', 'how', 'policy']

    def location(self, item):
        return reverse(item)
    
class NeedTelegramRootSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return ['need_telegram_root']

    def location(self, item):
        return reverse(item)
    
class NeedTelegramSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return ['need_telegram_employer', 'need_telegram_worker']

    def location(self, item):
        if item == 'need_telegram_employer':
            return reverse('need_telegram', args=['employer'])
        elif item == 'need_telegram_worker':
            return reverse('need_telegram', args=['worker'])
