# Generated by Django 2.2.10 on 2020-06-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='closed_on',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='collaborator_1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='collaborator_2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='key_word_2',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='project',
            name='key_word_3',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='project',
            name='key_word_4',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='project',
            name='key_word_5',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='project',
            name='link_1',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='project',
            name='link_2',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='project',
            name='link_3',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='project',
            name='link_4',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='project',
            name='link_5',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
