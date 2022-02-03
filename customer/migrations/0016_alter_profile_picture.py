# Generated by Django 3.2.1 on 2022-02-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0015_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, db_column='Image', default='/products/images/a68924_9c96bfe7821a45f391444d6f903809b9mv2.jpeg', help_text='Select a profile picture', null=True, upload_to='profiles/images/'),
        ),
    ]