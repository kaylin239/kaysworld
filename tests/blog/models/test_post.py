# tests/blog/test_post.py
"""
Test blog posts
"""
import datetime as dt
import pytest
from freezegun import freeze_time
from model_mommy import mommy
from blog.models import Post

# Mark this test module as requiring the database
pytestmark = pytest.mark.django_db

def test_published_posts_only_returns_those_with_published_status():
    """
    Test published posts should only return published status
    """
    # Create a published Post by setting the status to "published"
    published = mommy.make('blog.Post', status=Post.PUBLISHED)
    # Create a draft Post
    mommy.make('blog.Post', status=Post.DRAFT)

    # We expect only the "publised" object to be returned
    expected = [published]
    # Cast the result as a list so we can compare apples with apples!
    # Lists and querysets are of different types.
    result = list(Post.objects.published())

    assert result == expected

def test_publish_sets_status_to_published():
    """
    Test settting status to published
    """
    post = mommy.make('blog.Post', status=Post.DRAFT)
    post.publish()
    assert post.status == Post.PUBLISHED

@freeze_time(dt.datetime(2030, 6, 1, 12), tz_offset=0)  # Replaces now()
def test_publish_sets_published_to_current_datetime():
    """
    Test published posts log current datetime
    """
    # Create a new post, and ensure no published datetime is set
    post = mommy.make('blog.Post', published=None)
    post.publish()

    # Set the timezone to UTC (to match tz_offset=0)
    assert post.published == dt.datetime(2030, 6, 1, 12, tzinfo=dt.timezone.utc)

def test_get_authors_returns_users_who_have_authored_a_post(django_user_model):
    """
    Test get authors and return users who authored a post
    """
    # Create a user
    author = mommy.make(django_user_model)
    # Create a post that is authored by the user
    mommy.make('blog.Post', author=author)
    # Create another user – but this one won't have any posts
    mommy.make(django_user_model)

    assert list(Post.objects.get_authors()) == [author]

def test_get_authors_returns_unique_users(django_user_model):
    """
    Tets authors returns unique users
    """
    # Create a user
    author = mommy.make(django_user_model)
    # Create multiple posts. The _quantity argument can be used
    # to specify how many objects to create.
    mommy.make('blog.Post', author=author, _quantity=3)

    assert list(Post.objects.get_authors()) == [author]
