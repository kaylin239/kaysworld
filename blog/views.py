"""
Views.py module
"""
from django.shortcuts import render
from django.db.models import Count
from . import models

def home(request):
    """
    Home Request
    """
    # Get last 10 posts
    latest_posts = models.Post.objects.published().order_by('-published')[:10]
    authors = models.Post.objects.published().get_authors().order_by('first_name')
    topics = models.Topic.objects.annotate(Count('blog_posts')).order_by('-blog_posts__count')[:10]

    context = {
        'authors': authors,
        'latest_posts': latest_posts,
        'topics': topics
    }
    return render(request, 'blog/home.html', context)
