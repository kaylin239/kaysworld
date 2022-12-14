"""
comment posts
"""
# Generated by Django 4.1.1 on 2022-10-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    migrations class
    """

    dependencies = [
        ('blog', '0002_alter_post_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(related_name='comments', to='blog.comment'),
        ),
    ]
