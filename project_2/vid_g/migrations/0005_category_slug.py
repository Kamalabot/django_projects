# Generated by Django 4.0.7 on 2023-08-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vid_g', '0004_remove_video_thumbnail_link_video_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=100, null=True),
        ),
    ]
