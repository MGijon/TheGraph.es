# Generated by Django 2.2.10 on 2020-07-14 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=200, unique=True)),
                ('post_slug', models.SlugField(max_length=200, unique=True)),
                ('post_content', models.TextField()),
                ('post_status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('post_created_on', models.DateTimeField(auto_now_add=True)),
                ('post_updated_on', models.DateTimeField(auto_now=True)),
                ('post_key_word_1', models.CharField(default='Artificial Intelligence', max_length=75)),
                ('post_key_word_2', models.CharField(blank=True, max_length=75)),
                ('post_key_word_3', models.CharField(blank=True, max_length=75)),
                ('post_image_1', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('post_image_2', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('post_image_3', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('post_image_4', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('post_image_5', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-post_created_on'],
            },
        ),
    ]
