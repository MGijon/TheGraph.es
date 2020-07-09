# Generated by Django 2.2.10 on 2020-06-18 19:00

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
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('collaborator_1', models.CharField(max_length=100)),
                ('collaborator_2', models.CharField(max_length=100)),
                ('abstract', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Open'), (1, 'Closed')], default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('closed_on', models.DateTimeField()),
                ('description', models.TextField()),
                ('key_word_1', models.CharField(max_length=75)),
                ('key_word_2', models.CharField(max_length=75)),
                ('key_word_3', models.CharField(max_length=75)),
                ('key_word_4', models.CharField(max_length=75)),
                ('key_word_5', models.CharField(max_length=75)),
                ('link_1', models.CharField(max_length=150)),
                ('link_2', models.CharField(max_length=150)),
                ('link_3', models.CharField(max_length=150)),
                ('link_4', models.CharField(max_length=150)),
                ('link_5', models.CharField(max_length=150)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]