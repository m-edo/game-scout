# Generated by Django 3.2.1 on 2022-01-17 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0022_alter_product_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pic',
            field=models.ImageField(blank=True, db_column='Image', help_text='Select a picture for the product', null=True, upload_to='products/images/'),
        ),
    ]
