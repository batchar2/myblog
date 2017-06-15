from django.contrib.sitemaps import Sitemap
from blog.models import Post, SitePage

class PostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.filter(is_publish=True)

    def lastmod(self, obj):
        return obj.published_date


class SitePageSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return SitePage.objects.all()

    def lastmod(self, obj):
        return obj.created_date
