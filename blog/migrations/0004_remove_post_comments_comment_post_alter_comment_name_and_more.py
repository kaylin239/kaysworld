"""
remove comments
"""
# Generated by Django 4.1.1 on 2022-10-04 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """
    migration class
    """

    dependencies = [
        ('blog', '0003_comment_post_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
            related_name='comments', to='blog.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=400),
        ),
    ]