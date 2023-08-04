# Generated by Django 4.0.7 on 2023-08-03 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0004_userquery_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_title', models.CharField(max_length=150)),
                ('playlist_url', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoid', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=100)),
                ('videourl', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000, null=True)),
                ('slug', models.SlugField(blank=True, default='', max_length=150, null=True)),
                ('featured_image', models.ImageField(null=True, upload_to='Media/featured_img')),
            ],
        ),
    ]