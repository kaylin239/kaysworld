"""
inital.py
"""
# Generated by Django 4.1.1 on 2022-10-04 01:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """
    Migration class
    """

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'),
                ('published', 'Published')],
                default='draft',
                help_text='Set to "published" to make this post publicly visible',
                max_length=10)),
                ('published', models.DateTimeField(blank=True,
                help_text='The date & time this article was published', null=True)),
                ('slug', models.SlugField(help_text='The date & time this article was published',
                unique_for_date='published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('topics', models.ManyToManyField(related_name='blog_posts', to='blog.topic')),
            ],
        ),
    ]
