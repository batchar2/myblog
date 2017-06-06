from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import F


from .models import Post, Category, Tag, SitePage

# Create your views here.

def about(request):
	page = get_object_or_404(SitePage, url='about')
	SitePage.objects.filter(url='about').update(number_views=F("number_views") + 1)
	return render(request, 'blog/page_about.html', {'page': page})


def post_list(request):
    posts = Post.objects.filter(is_publish=True).order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    # обновляю счетчик
    Post.objects.filter(slug=slug).update(number_views=F("number_views") + 1)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_list_category(request, slug):
	category = get_object_or_404(Category, slug=slug)

	return render(request, 'blog/post_list_category.html', {'category': category})


def post_list_tag(request, slug):
	tag = get_object_or_404(Tag, slug=slug)

	return render(request, 'blog/post_list_tag.html', {'tag': tag})