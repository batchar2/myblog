"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.contrib.sitemaps.views import sitemap

from filebrowser.sites import site
site.directory = "uploads/"
site.storage.location = 'static/'

# Необходимо импортировать созданные нами классы
from blog.sitemap import PostSitemap, SitePageSitemap

# Далее создать словарь со всеми классами
sitemaps = {
    'post': PostSitemap,
    'sitepage': SitePageSitemap,
    #'static': StaticSitemap,
}

urlpatterns = [
    url(r'^admin/filebrowser/', site.urls),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^comments/', include('django_comments_xtd.urls')),

    url(r'^admin/', admin.site.urls),
    #url(r'^sitemap.xml$',
    # 'django.contrib.sitemaps.views.sitemap',
    # {'sitemaps': sitemaps}),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

    url(r'', include('blog.urls', namespace='blog')),
]
