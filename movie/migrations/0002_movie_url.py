# Generated by Django 3.2 on 2021-04-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
