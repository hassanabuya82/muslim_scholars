# Generated by Django 4.2.3 on 2023-08-04 08:27

import blogs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_remove_post_categories_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=blogs.models.post_pics),
        ),
    ]