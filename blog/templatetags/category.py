from django import template

from blog.models import Category

register = template.Library()

@register.inclusion_tag("blog/tag_category.html")
def show_category():
    categories = Category.objects.filter(is_publish=True).all()
    return {'categories': categories}