# Generated by Django 3.2.1 on 2022-01-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_rename_product_wishlist_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, db_column='Image', help_text='Select a profile picture', null=True, upload_to='profiles/images/'),
        ),
    ]
