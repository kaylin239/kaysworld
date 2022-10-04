"""
Expose models in the Django admin
"""

from django.contrib import admin
from . import models
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    """
    Customize Comment
    """

    list_display = (
        'name',
        'email',
        'text',
        'created',
        'updated',
        'approved',
    )

    search_fields = (
        'name',
        'email',
        'text',
    )

    list_filter = (
        'approved',
    )

admin.site.register(models.Comment, CommentAdmin)

class CommentInline(admin.StackedInline):
    """
    Inline model admin for Comment model
    """
    model = Comment
    extra = 0
    readonly_fields = ('name','email','text',)
    fields = ('name','email','text','approved',)

class PostAdmin(admin.ModelAdmin):
    """
    Customize Post
    """

    list_display = (
        'title',
        'author',
        'created',
        'updated',
    )

    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    list_filter = (
        'status',
        'topics',
    )

    prepopulated_fields = {'slug': ('title',)}

    inlines = [
        CommentInline,
    ]

admin.site.register(models.Post, PostAdmin)

class TopicAdmin(admin.ModelAdmin):
    """
    Customize Topic
    """

    list_display = (
        'name',
        'slug',
    )

    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Topic, TopicAdmin)
