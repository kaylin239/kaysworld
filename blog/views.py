"""
Views.py module
"""
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from . import models

class HomeView(TemplateView):
    """
    Home View
    """
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        # Get the parent context
        context = super().get_context_data(**kwargs)

        latest_posts = models.Post.objects.published() \
            .order_by('-published')[:10]

        # Update the context with our context variables
        context.update({'latest_posts': latest_posts})

        return context

class AboutView(TemplateView):
    """
    Class View
    """
    template_name = 'blog/about.html'

class PostListView(ListView):
    """
    Post List View
    """
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects.published().order_by('-published')

class TopicListView(ListView):
    """
    Topic List View
    """
    model = models.Topic
    context_object_name = 'topics'
    queryset = models.Topic.objects.order_by('name')

class PostDetailView(DetailView):
    """
    Post Detail View
    """
    model = models.Post

    def get_queryset(self):
        # Get the base queryset
        queryset = super().get_queryset().published()

        if 'pk' in self.kwargs:
            return queryset

        return queryset.filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )

class TopicDetailView(DetailView):
    """
    Topic Detail View
    """
    model = models.Topic

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

def terms_and_conditions(request):
    """
    Terms and Conditions View
    """
    return render(request, 'blog/terms_and_conditions.html')

class PhotoFormView(CreateView):
    """
    Photo Contest FormView Class
    """
    model = models.Contact
    template_name = 'blog/photo_form.html'
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'photo',
    ]

    def form_valid(self, form):
        # Create a "success" message
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you for submitting your photo!'
        )
        # Continue with default behaviour
        return super().form_valid(form)
