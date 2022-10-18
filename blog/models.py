"""
Add Django models
"""

from django.conf import settings  # Imports Django's loaded settings
from django.db import models # Imports Django's models
from django.utils import timezone
from django.contrib.auth import get_user_model

class PostQuerySet(models.QuerySet):
    """
    Represents a PostQuerySet
    """
    def published(self):
        """
        Published
        """
        return self.filter(status=self.model.PUBLISHED)

    def drafts(self):
        """
        Drafts
        """
        return self.filter(status=self.model.DRAFT)

    def get_authors(self):
        """
        Get Authors
        """
        user = get_user_model()
        # Get the users who are authors of this queryset
        return user.objects.filter(blog_posts__in=self).distinct()

class Topic(models.Model):
    """
    Represents a topic for a blog post
    """

    name = models.CharField(
        max_length=50,
        unique=True,  # No duplicates!
    )

    slug = models.SlugField(unique=True)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    """
    Represents a blog post
    """

    title = models.CharField(max_length=255) #post title
    content = models.TextField(null=True) #article's content

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,
        related_name='blog_posts',
        null=False
    )

    created = models.DateTimeField(auto_now_add=True)  # timestamp set on create
    updated = models.DateTimeField(auto_now=True)  # timestamp updates on each save
    objects = PostQuerySet.as_manager()

    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
    )

    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published',
    )

    slug = models.SlugField(
        null=False,
        help_text='The date & time this article was published',
        unique_for_date='published',  # Slug is unique for publication date
    )

    topics = models.ManyToManyField(
        Topic,
        related_name='blog_posts',
    )

    def publish(self):
        """Publishes this post"""
        self.status = self.PUBLISHED
        self.published = timezone.now()  # The current datetime with timezone

    class Meta:
        """
        Ordering class
        """
        ordering = ['-created']

    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    """
    Represents a comment on a blog post
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100) #commenter's name
    email = models.EmailField(max_length=255) #commenter's email
    text = models.TextField(max_length=400) #comment text
    created = models.DateTimeField(auto_now_add=True)  # timestamp set on create
    updated = models.DateTimeField(auto_now=True)  # timestamp updates on each save

    approved = models.BooleanField(
        default=False,
    )

    class Meta:
        """
        Meta ordering class
        """
        ordering = ['-created']

    def __str__(self):
        return str(self.text)
