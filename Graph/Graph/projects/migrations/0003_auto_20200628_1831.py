# Generated by Django 2.2.10 on 2020-06-28 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200618_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(0, 'Secret'), (1, 'Open'), (2, 'Closed')], default=0),
        ),
    ]