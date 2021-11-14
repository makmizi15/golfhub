# Generated by Django 3.2.9 on 2021-11-14 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_golfgroup_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfgroup',
            name='game_type',
            field=models.CharField(choices=[('2-Man Scramble', '2-Man Scramble'), ('Freeplay', 'Freeplay')], default='f', max_length=50),
        ),
    ]
