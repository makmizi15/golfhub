# Generated by Django 3.2.9 on 2021-11-19 08:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfgroup',
            name='members',
            field=models.ManyToManyField(null=True, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]