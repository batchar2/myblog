from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import F


from .models import Post, Category, Tag, SitePage

def about(request):
    page = get_object_or_404(SitePage, url='about')
    SitePage.objects.filter(url='about').update(number_views=F("number_views") + 1)
    return render(request, 'blog/page_about.html', {'page': page})


def post_list(request):
    #posts = Post.objects.filter(is_publish=True).order_by('-created_date')
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # обновляю счетчик
    Post.objects.filter(slug=slug).update(number_views=F("number_views") + 1)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_list_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'blog/post_list_category.html',
                    {'category': category})


def post_list_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    return render(request, 'blog/post_list_tag.html', {'tag': tag})

# 404
def page_not_found(request):
    return render(request, 'blog/404.html')

# 500
def server_error(request):
    return render(request, 'blog/500.html')

def google_page(request):
    return render(request, 'blog/google_page.html')
