"""
A simple function-based view
"""

from django.http import HttpResponse

def index(request):
    """
    This view generates a simple HTTP response using the
    HttpResponse constructor imported from the http library
    of the Django framework.
    """
    return HttpResponse('Hello world!')
