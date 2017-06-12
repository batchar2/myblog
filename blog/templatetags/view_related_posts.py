from django import template

from blog.models import Post

register = template.Library()

@register.inclusion_tag("blog/tag_view_related_posts.html")
def view_related_posts():
    posts = Post.objects.filter(is_publish=True).all().order_by('?')[:3]
    return {'posts': posts}