# Generated by Django 3.2.1 on 2022-01-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0025_alter_product_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pic',
            field=models.ImageField(blank=True, db_column='Image', default='/media/products/images/a68924_9c96bfe7821a45f391444d6f903809b9mv2.jpeg', help_text='Select a picture for the product', null=True, upload_to='products/images/'),
        ),
    ]
