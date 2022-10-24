"""
Context Processors
"""
from django.db.models import Count
from . import models

def base_context(request):
    """
    Query to populate author context
    """

    top_topics = models.Topic.objects.annotate(Count('blog_posts')) \
        .order_by('-blog_posts__count')[:10]

    topic_list = models.Topic.objects.order_by('name')

    authors = models.Post.objects.published() \
        .get_authors() \
        .order_by('first_name')

    return {'top_topics': top_topics,
            'topic_list': topic_list,
            'authors': authors,}
