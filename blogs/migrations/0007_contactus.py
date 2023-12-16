# Generated by Django 4.2.3 on 2023-12-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_remove_comment_author_comment_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('subject', models.CharField(max_length=1000, null=True)),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
