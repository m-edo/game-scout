# Generated by Django 3.2.7 on 2021-10-13 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_profile_fake'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fake',
        ),
    ]