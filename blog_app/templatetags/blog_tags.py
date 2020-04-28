from django import template
from ..models import Post
from django.db.models import Count

register = template.Library()

"""Processes dara and returns values"""
@register.simple_tag #to registrate a new tag
def total_posts():
    return Post.published.count() #returns the amount of published posts

'''Processes data and returns generated fragment of the template'''
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

"""The result of the process will be saved into a variable so it can be used repeatedly
and without recalculation"""
@register.simple_tag
def get_most_commented_posts(count=5): #to show maximum 5 posts
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    
# method annotate adds the amount of cooments to every post 
