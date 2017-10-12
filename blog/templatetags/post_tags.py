from django import template
from django.db.models import Count

from blog.models import Post, Tag, Category

register = template.Library()


@register.simple_tag
def get_recent_post(*args, **kwargs):
    return Post.objects.all()[:5]


@register.simple_tag
def get_tags(*args, **kwargs):
    return Tag.objects.annotate(post_num=Count('post')).filter(post_num__gt=0)


@register.simple_tag
def get_categories(*args, **kwargs):
    return Category.objects.all()


@register.simple_tag
def get_posts(num=None, *args, **kwargs):
    return Post.objects.all()[:num]
