# Generated by Django 4.0 on 2022-01-08 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_profile_seller_ratings_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='sold_keys',
        ),
    ]
