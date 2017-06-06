from django.conf.urls import url
from . import views

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^about/$', views.about, name='about'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<slug>[-\w]+)/$', views.post_list_category, name='post_list_category'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.post_list_tag, name='post_list_tag'),
]

