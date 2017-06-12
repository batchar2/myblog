from django import template

from blog.models import Post

register = template.Library()

@register.inclusion_tag("blog/tag_popular_posts.html")
def popular_post():
    posts = Post.objects.filter(is_publish=True).order_by('-number_views')[0:5]
    return {'posts': posts}