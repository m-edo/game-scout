# Generated by Django 3.2.7 on 2021-10-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_remove_profile_fake'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_seller',
            field=models.BooleanField(default=False, help_text='Check if user is seller'),
        ),
    ]