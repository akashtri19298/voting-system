# Generated by Django 2.0.3 on 2018-04-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_voter_voter_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='voter_username',
            field=models.CharField(max_length=20),
        ),
    ]