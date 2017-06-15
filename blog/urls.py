from django.conf.urls import url
from . import views

from django.conf.urls import (
    handler404, handler500
)

handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.server_error'

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^about/$', views.about, name='about'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<slug>[-\w]+)/$', views.post_list_category, name='post_list_category'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.post_list_tag, name='post_list_tag'),
    url(r'^googledfac55627724f996.html$', views.google_page, name='google_page'),
]
